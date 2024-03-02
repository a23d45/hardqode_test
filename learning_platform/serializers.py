from rest_framework import serializers

from accounts.models import User
from learning_platform.models import Product, Lesson
from learning_platform import services


class AuthorSerializer(serializers.ModelSerializer):
    """Сериализатор для автора"""
    class Meta:
        model = User
        fields = ('id', 'username')


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор модели Product"""
    number_of_lessons = serializers.SerializerMethodField()
    number_of_students = serializers.IntegerField(required=False)
    filling_out_group = serializers.FloatField(required=False)
    product_purchase = serializers.FloatField(required=False)

    author = AuthorSerializer(read_only=True)
    
    class Meta:
        model = Product
        exclude = ('students', )

    def get_number_of_lessons(self, obj: Product) -> int:
        return services.get_number_of_lessons_for_product(obj)
    

class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор модели Lesson"""

    class Meta:
        model = Lesson
        fields = '__all__'


class AddStudentToProduct(serializers.Serializer):
    student_id = serializers.IntegerField()
    product_id = serializers.IntegerField()

