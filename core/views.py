from django.views.generic import TemplateView
from django.template import loader
from accounts.models import *


class Framework(TemplateView):
    def get_template_names(self):
        path = self.request.path.replace("/framework", "")

        if path == "/":
            load_template = "/dashboard.html"
        else:
            load_template = path

        template = loader.get_template('00_framework' + load_template)
        self.template_name = template

        return self.template_name


class Home(TemplateView):
    template_name = '01_base/home.html'

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            costumers=PersonModel.objects.count(),
            employees=EmployeeModel.objects.count()
        )
