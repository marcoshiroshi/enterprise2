from django.urls import path
from .views import *


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("client/", ClientView.as_view(), name="create_client"),
    path("function/", FuntionView.as_view(), name="create_function"),
    path("employee/", EmployeeView.as_view(), name="create_employee"),
    path("status/", StatusView.as_view(), name="create_status"),

]
