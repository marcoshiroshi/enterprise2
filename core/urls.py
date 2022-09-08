from django.urls import re_path, path
from core.views import *

urlpatterns = [
    re_path(r'^.*\.*', Framework.as_view(), name='framework_dashboard')
]
