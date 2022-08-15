from django.urls import path, re_path
from core.views import Framework

urlpatterns = [

    path('', Framework.as_view(), name='framework'),
    re_path(r'^.*\.*', Framework.as_view(), name='framework_dashboard'),
]
