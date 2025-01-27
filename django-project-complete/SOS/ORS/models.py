from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    loginId = models.EmailField()
    password = models.CharField(max_length=20)
    confirmPassword = models.CharField(max_length=20, default='')
    dob = models.DateField(max_length=20)
    address = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=50, default='')
    mobileNumber = models.CharField(max_length=50, default='')
    roleId = models.IntegerField()
    roleName = models.CharField(max_length=50)

    def get_key(self):
        return str(self.id)

    def get_value(self):
        return self.name

    class Meta:
        db_table = 'sos_user'


class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def get_key(self):
        return str(self.id)

    def get_value(self):
        return self.name

    class Meta:
        db_table = 'sos_role'

class Attribute(models.Model):
    display=models.CharField(max_length=50)
    datatype=models.CharField(max_length=50)
    isActive=models.CharField(max_length=40)
    description=models.CharField(max_length=30)

    def get_key(self):
        return str(self.id)

    def get_value(self):
        return self.datatype

    class Meta:
        db_table='sos_attribute'

class Initiative(models.Model):
    initiativeName=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    startDate=models.DateField(max_length=25)
    version=models.IntegerField()


    def get_key(self):
        return str(self.id)

    def get_value(self):
        return self.initiativeName

    class Meta:
        db_table='sos_initiative'


class Employee(models.Model):
    fullName=models.CharField(max_length=50)
    userName=models.EmailField()
    birthDate=models.DateField(max_length=30)
    contactNumber=models.CharField(max_length=15, default='')

    def get_key(self):
        return str(self.id)

    def get_value(self):
        return self.fullName

    class Meta:
        db_table='sos_employee'

