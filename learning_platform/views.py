from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.response import Response

from learning_platform import serializers
from learning_platform import models
from learning_platform import services


class ProductListView(generics.ListAPIView):
    """Получение списка продуктов"""
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        return services.get_products()


class LessonsListView(generics.ListAPIView):
    """Получение списка уроков по продукту"""
    serializer_class = serializers.LessonSerializer

    def get_queryset(self):
        student_id = self.kwargs.get('student_id')
        product_id = self.kwargs.get('product_id')
        return services.\
            get_lessons_for_student_on_product(student_id, product_id)


class AddStudentToProductView(generics.CreateAPIView):
    """Добавление студента к продукту"""
    serializer_class = serializers.AddStudentToProduct

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student_id = request.data.get('student_id')
        product_id = request.data.get('product_id')
        
        try:
            services.add_student_to_product(student_id, product_id)
        except ObjectDoesNotExist:
            return Response(status=400, data={'success': False})
        
        return Response(status=200, data={'success': True})

