from django.shortcuts import render, redirect

from .BaseCtl import BaseCtl
from ..service.UserService import UserService
from ..utility.DataValidator import DataValidator


class LoginCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form["loginId"] = requestForm["loginId"]
        self.form["password"] = requestForm["password"]

    def display(self, request, params={}):
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def input_validation(self):
        super().input_validation()

        inputError = self.form["inputError"]

        if (DataValidator.isNull(self.form["loginId"])):
            inputError["loginId"] = "Login ID is required"
            self.form["error"] = True
        else:
            if (DataValidator.isEmail(self.form['loginId'])):
                inputError['loginId'] = "Login Id must be email"
                self.form['error'] = True

        if (DataValidator.isNull(self.form["password"])):
            inputError["password"] = "Password is required"
            self.form["error"] = True

        return self.form["error"]

    def submit(self, request, params={}):
        user = self.get_service().authenticate(self.form)
        if (user is None):
            self.form['error'] = True
            self.form['message'] = "Login ID & password is Invalid"
            res = render(request, self.get_template(), {'form': self.form})
        else:
            request.session["user"] = user.firstName
            res = redirect('/Welcome/')
        return res

    def get_template(self):
        return "Login.html"

    def get_service(self):
        return UserService()
