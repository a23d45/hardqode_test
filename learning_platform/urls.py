from django.urls import path

from learning_platform import views


urlpatterns = [
    path('products/', views.ProductListView.as_view()),
    path(
        'lessons/<int:student_id>/<int:product_id>/', 
        views.LessonsListView.as_view()
    ),
    path('add_student_to_product/', views.AddStudentToProductView.as_view())
]