from django.shortcuts import render

from ..ctl.BaseCtl import BaseCtl
from ..models import Employee
from ..service.EmployeeService import EmployeeService

from ..utility.DataValidator import DataValidator



class EmployeeCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['fullName'] = requestForm['fullName']
        self.form['userName'] = requestForm['userName']
        # self.form['password'] = requestForm['password']
        self.form['birthDate'] = requestForm['birthDate']
        self.form['contactNumber'] = requestForm['contactNumber']

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.fullName = self.form['fullName']
        obj.userName = self.form['userName']
        # obj.password = self.form['password']
        obj.birthDate = self.form['birthDate']
        obj.contactNumber = self.form['contactNumber']
        return obj

    def model_to_form(self, obj):
        if obj is None:
            return
        self.form['id'] = obj.id
        self.form['fullName'] = obj.fullName
        self.form['userName'] = obj.userName
        self.form['password'] = obj.password
        self.form['birthDate'] = obj.birthDate.strftime("%Y-%m-%d")
        self.form['contactNumber'] = obj.contactNumber

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['fullName'])):
            inputError['fullName'] = "FullName is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isAlphaCheck(self.form['fullName'])):
                inputError['fullName'] = 'full name only contain letter'
                self.form['error'] = True

        if (DataValidator.isNull(self.form['userName'])):
            inputError['userName'] = "UserName is Required"
            self.form['error'] = True
        else:
            if (DataValidator.isEmail(self.form['userName'])):
                inputError['userName'] = "Login ID must be like student@gmail.com"
                self.form['error'] = True

        if (DataValidator.isNull(self.form["birthDate"])):
            inputError["birthDate"] = "birth date can not be null"
            self.form["error"] = True
        else:
            if (DataValidator.isDate(self.form["birthDate"])):
                inputError["birthDate"] = "enter correct date, YYYY-MM-DD "
                self.form["error"] = True

        if (DataValidator.isNull(self.form["contactNumber"])):
            inputError["contactNumber"] = "contact number can not be null"
            self.form["error"] = True
        else:
            if (DataValidator.isMobileCheck(self.form["contactNumber"])):
                inputError["contactNumber"] = "enter correct contact number"
                self.form["error"] = True

        return self.form["error"]

    def display(self, request, params={}):
        if (params['id'] > 0):
            obj = self.get_service().get(params['id'])
            self.model_to_form(obj)
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def submit(self, request, params={}):
        r=self.form_to_model(Employee())
        self.get_service().save(r)
        self.form['message']="Data Saved Successfully"
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def get_template(self):
        return "Employee.html"

    def get_service(self):
        return EmployeeService()
