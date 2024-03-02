from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from learning_platform import models 
from learning_platform.management.commands import _data
from learning_platform.services import add_student_to_product

User = get_user_model()


class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми данными'

    def handle(self, *args, **options):
        
        User.objects.all().delete()
        models.Product.objects.all().delete()
        models.Lesson.objects.all().delete()
        models.Group.objects.all().delete()   

        for author in _data.author_data:
            User.objects.create(username=author['username'], role=1)
        
        for product in _data.product_data:
            current_product = models.Product.objects.create(
                name=product['name'], 
                price=product['price'], 
                author=User.objects.get(username=product['author_username'])
            )
            if (product.get('max_number_users_in_group')):
                current_product.max_number_users_in_group \
                    = product['max_number_users_in_group']
                current_product.save()



        # for students in _data.student_data:
        #     current_user = User.objects.create(username=students['username'], role=0) 
        #     add_student_to_product(current_user, current_product)

        for lesson in _data.lesson_data:
            models.Lesson.objects.create(
                name=lesson['name'],
                product=models.Product.objects.get(name=lesson['product_name']),
                link=lesson['link']
            )

        self.stdout.write(self.style.SUCCESS('Данные успешно добавлены в базу данных.'))

