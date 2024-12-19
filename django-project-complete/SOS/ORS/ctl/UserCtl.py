from django.shortcuts import render

from ..ctl.BaseCtl import BaseCtl
from ..models import User
from ..service.UserService import UserService
from ..utility.DataValidator import DataValidator


class UserCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm.get('id', None)
        self.form['firstName'] = requestForm.get('firstName', '')
        self.form['lastName'] = requestForm.get('lastName', '')
        self.form['loginId'] = requestForm.get('loginId', '')
        self.form['password'] = requestForm.get('password', '')
        self.form['confirmPassword'] = requestForm.get('confirmPassword', '')
        self.form['dob'] = requestForm.get('dob', '')
        self.form['address'] = requestForm.get('address', '')
        self.form['gender'] = requestForm.get('gender', None)
        self.form['mobileNumber'] = requestForm.get('mobileNumber', '')
        self.form['roleId'] = 2
        self.form['roleName'] = 'Student'

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.firstName = self.form['firstName']
        obj.lastName = self.form['lastName']
        obj.loginId = self.form['loginId']
        obj.password = self.form['password']
        obj.confirmPassword = self.form['confirmPassword']
        obj.dob = self.form['dob']
        obj.address = self.form['address']
        obj.gender = self.form['gender']
        obj.mobileNumber = self.form['mobileNumber']
        obj.roleId = self.form['roleId']
        obj.roleName = self.form['roleName']
        return obj

    def model_to_form(self, obj):
        if obj is None:
            return
        self.form['firstName'] = obj.firstName
        self.form['lastName'] = obj.lastName
        self.form['loginId'] = obj.loginId
        self.form['password'] = obj.password
        self.form['confirmPassword'] = obj.confirmPassword
        self.form['dob'] = obj.dob
        self.form['address'] = obj.address
        self.form['gender'] = obj.gender
        self.form['mobileNumber'] = obj.mobileNumber
        self.form['roleId'] = 2
        self.form['roleName'] = 'Student'

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['firstName'])):
            inputError['firstName'] = "First Name is required"
            self.form['error'] = True
        else:
            if (DataValidator.isAlphaCheck(self.form['firstName'])):
                inputError['firstName'] = "First Name only contains Letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['lastName'])):
            inputError['lastName'] = "Last Name is required"
            self.form['error'] = True
        else:
            if (DataValidator.isAlphaCheck(self.form['lastName'])):
                inputError['lastName'] = "Last Name only contains Letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['loginId'])):
            inputError['loginId'] = "Login ID is required"
            self.form['error'] = True
        else:
            if (DataValidator.isEmail(self.form['loginId'])):
                inputError['loginId'] = "Login Id should be like abc@gmail.com"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['password'])):
            inputError['password'] = "Password  is required"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['confirmPassword'])):
            inputError['confirmPassword'] = "Confirm Password  is required"
            self.form['error'] = True
        else:
            if (DataValidator.isNotNull(self.form['confirmPassword'])):
                if self.form['password'] != self.form['confirmPassword']:
                    inputError['confirmPassword'] = "Confirm Password & Password should be same"
                    self.form['error'] = True

        if (DataValidator.isNull(self.form['dob'])):
            inputError['dob'] = "DOB is required"
            self.form['error'] = True
        else:
            if (DataValidator.isDate(self.form['dob'])):
                inputError['dob'] = "Incorrect Date, should be YYYY-MM-DD"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['address'])):
            inputError['address'] = "Address is required"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['gender'])):
            inputError['gender'] = "Gender is required"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['mobileNumber'])):
            inputError['mobileNumber'] = "Mobile Number is required"
            self.form['error'] = True
        else:
            if (DataValidator.isMobileCheck(self.form['mobileNumber'])):
                inputError['dob'] = "Enter Correct Numerxb h3y `ytrew4t321"
                self.form['error'] = True
        return self.form['error']

    def display(self, request, params={}):
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def submit(self, request, params={}):
        r = self.form_to_model(User())
        self.get_service().save(r)
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def get_template(self):
        return "User.html"

    def get_service(self):
        return UserService()
