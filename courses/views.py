from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Course


class ManagerCourseListView(ListView):
    model = Course
    template_name = 'course/manage/course/list.html'

    def get_queryset(self):
        qs = super(ManagerCourseListView, self).get_queryset()
        return qs.filter(owner=self.request.user)

# Create your views here.
