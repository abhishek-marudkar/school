from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from main.serializers import SchoolSerializer, StudentSerializer, SchoolStudentSerializer, StudentsDataSerializer
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from main.models import School
from main.forms import *
from django.urls import reverse_lazy
from django.views import View
# Create your views here.


def home(request):
    return redirect("list_school")


class SchoolCreate(CreateView):
    model = School
    form_class = SchoolForm
    template_name = "school/create.html"
    success_url = reverse_lazy("list_school")


class SchoolListView(ListView):
    model = School
    paginate_by = 100
    template_name = "school/list.html"
    context_object_name = "schools"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SchoolUpdate(UpdateView):
    model = School
    form_class = SchoolForm
    pk_url_kwarg = 'id'
    template_name = "school/update.html"
    success_url = reverse_lazy("list_school")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_pk'] = self.kwargs['id']
        return context


class SchoolDelete(View):

    def post(self, request):
        school_id = request.POST.get("school")
        school = School.objects.get(id=school_id)
        school.delete()
        return redirect("list_school")


class StudentsCreate(CreateView):
    model = Students
    form_class = StudentForm
    template_name = "students/create.html"
    success_url = reverse_lazy("list_students")


class StudentsListView(ListView):
    model = Students
    paginate_by = 100
    template_name = "students/list.html"
    context_object_name = "students"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class StudentsUpdate(UpdateView):
    model = Students
    form_class = StudentForm
    pk_url_kwarg = 'id'
    template_name = "students/update.html"
    success_url = reverse_lazy("list_students")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_pk'] = self.kwargs['id']
        return context


class StudentsDelete(View):

    def post(self, request):
        student_id = request.POST.get("student")
        student = Students.objects.get(id=student_id)
        student.delete()
        return redirect("list_students")


class SchoolDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return School.objects.get(pk=pk)
        except School.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        school = self.get_object(pk)
        serializer = SchoolSerializer(school)
        response = {
            'status': status.HTTP_200_OK,
            'message': "School details",
            'data': serializer.data
        }
        return Response(response)


class StudentDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Students.objects.get(pk=pk)
        except Students.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, context={
            'request': request,
        })
        response = {
            'status': status.HTTP_200_OK,
            'message': "Student details",
            'data': serializer.data
        }
        return Response(response)


# class SchoolStudentDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """

#     def get_object(self, pk):
#         try:
#             return School.objects.filter(pk=pk).prefetch_related('students_set').all()
#         except School.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         school = self.get_object(pk)
#         serializer = SchoolStudentSerializer(school, context={
#             'request': request,
#         })
#         response = {
#             'status': status.HTTP_200_OK,
#             'message': "Student details",
#             'data': serializer.data
#         }
#         return Response(response)
