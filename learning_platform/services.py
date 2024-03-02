from django.db.models import Avg, Count, F
from django.db.models.query import QuerySet
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from learning_platform.models import Group, Product


User: AbstractUser = get_user_model()

def create_new_group(
        student: AbstractUser, 
        number_of_groups: int, 
        product: Product
    ) -> None:
    """Создает новую группу и добавляет в нее студента"""
    new_group = Group.objects.create(
        name=f'Группа {number_of_groups + 1}',
        product=product
    )
    new_group.students.add(student)


def add_student_to_started_product(
        student: AbstractUser, 
        product: Product,
        groups: QuerySet,
        number_of_groups: int
    ) -> None:
    """
    Добавляет студента к продукту и в группу, если продукт уже запустился.
    """
    product.students.add(student)

    if number_of_groups > 0:
        min_group = groups.order_by('number_of_students').first()
        if (min_group.number_of_students < 
            product.max_number_users_in_group):
            min_group.students.add(student)
            return
            
    create_new_group(student, number_of_groups, product)


def add_student_to_product(
        student_id: AbstractUser, 
        product_id: Product
    ) -> None:
    """
    Добавляет студента к продукту. 
    Если студент и продукт не существуют, то вызывается исключение.
    """
    student = User.objects.get(id=student_id, role=False)
    product = Product.objects.get(id=product_id)

    groups_for_product = Group.objects.filter(product_id=product.id).\
        annotate(
            number_of_students=Count('students', distinct=True)
        )
    
    number_of_groups = groups_for_product.count()
    add_student_to_started_product(
        student, 
        product, 
        groups_for_product,
        number_of_groups
    )


def get_number_of_lessons_for_product(product: Product) -> int:
    """Возвращает количество уроков для заданного проодукта"""
    return product.lessons.count()


def get_lessons_for_student_on_product(
        student_id: int, 
        product_id: int
    ) -> QuerySet | list:
    """Возвращает уроки, если они доступны студенту по продукту"""
    product = Product.objects.\
        filter(id=product_id).first()
    if product and product.students.filter(id=student_id).exists():
        return product.lessons.all()
    return []


def get_products(calc_extra_information: bool = True):
    """Возвращает список продуктов"""
    products = Product.objects.\
                select_related('author').\
                    prefetch_related('lessons').all()
    if calc_extra_information:
        number_of_all_students_in_platform =\
                User.objects.filter(role=False).count()
        products = products.annotate(
            number_of_students=Count('students', distinct=True)
        ).\
        annotate(
            product_purchase=F('number_of_students') \
                / number_of_all_students_in_platform
        )
    return products


def get_number_of_students_in_product(product: Product):
    """Возвращает количество студентов, которые добавлены к продукту"""
    return product.number_of_students