from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from accounts.models import *
from accounts.forms import EmployeeForm


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ClientView(CreateView):
    model = PersonModel
    template_name = '01_base/create_client.html'
    fields = "__all__"
    success_url = reverse_lazy("home")


class FuntionView(CreateView):
    model = FunctionModel
    template_name = '01_base/create_function.html'
    fields = "__all__"
    success_url = reverse_lazy("home")


class StatusView(CreateView):
    model = StatusEmployeeModel
    template_name = '01_base/create_status.html'
    fields = "__all__"
    success_url = reverse_lazy("home")


class EmployeeView(CreateView):
    model = EmployeeModel
    template_name = '01_base/create_employee.html'
    form_class = EmployeeForm
    success_url = reverse_lazy("home")


'teste de commit'