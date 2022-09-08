from django.db import models


class FunctionModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class StatusEmployeeModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PersonModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    fone = models.CharField(max_length=50)
    adress = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EmployeeModel(models.Model):
    person = models.ForeignKey(PersonModel, models.DO_NOTHING, related_name='person_employee')
    function = models.ForeignKey(FunctionModel, models.DO_NOTHING, related_name='function_employee')
    status_employee = models.ForeignKey(StatusEmployeeModel, models.DO_NOTHING, related_name='status_employee')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.person.name
