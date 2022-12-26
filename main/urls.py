from django.contrib import admin
from django.urls import path, include
from main import views
urlpatterns = [
    path('', views.home, name="home"),
    path('school/', views.SchoolListView.as_view(), name="list_school"),
    path('school/create/', views.SchoolCreate.as_view(), name="create_school"),
    path('school/<int:id>', views.SchoolUpdate.as_view(), name="update_school"),
    path('school/delete',
         views.SchoolDelete.as_view(), name="delete_school"),
    path('students/', views.StudentsListView.as_view(), name="list_students"),
    path('students/create/', views.StudentsCreate.as_view(), name="create_students"),
    path('students/<int:id>', views.StudentsUpdate.as_view(), name="update_students"),
    path('students/delete',
         views.StudentsDelete.as_view(), name="delete_students"),
    # API routers
    path('api/school/<int:pk>/', views.SchoolDetail.as_view()),
    path('api/student/<int:pk>/', views.StudentDetail.as_view()),
]
