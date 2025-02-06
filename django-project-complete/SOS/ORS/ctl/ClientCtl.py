from django.shortcuts import render

from ..ctl.BaseCtl import BaseCtl
from ..models import Client
from ..service.ClientService import ClientService
from ..utility.DataValidator import DataValidator
from ..utility.HTMLUtility import HTMLUtility


class ClientCtl(BaseCtl):


    def preload(self, request, params):

        self.form["illness"] = request.POST.get('illness', '')


        if (params['id'] > 0):
            obj = self.get_service().get(params['id'])
            self.form["illness"] = obj.illness

        self.static_preload = {"Common cold": "Common cold", "Asthma": "Asthma"}

        self.form["preload"]["illness"] = HTMLUtility.get_list_from_dict(
            'illness',
            self.form["illness"],
            self.static_preload
        )

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['fullName'] = requestForm['fullName']
        self.form['appointmentDate'] = requestForm['appointmentDate']
        self.form['contactNumber'] = requestForm['contactNumber']
        self.form['illness'] = requestForm['illness']

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.fullName = self.form['fullName']
        obj.appointmentDate = self.form['appointmentDate']
        obj.contactNumber = self.form['contactNumber']
        obj.illness = self.form['illness']
        return obj

    def model_to_form(self, obj):
        if obj is None:
            return
        self.form['id'] = obj.id
        self.form['fullName'] = obj.fullName
        self.form['appointmentDate'] = obj.appointmentDate
        self.form['contactNumber'] = obj.contactNumber
        self.form['illness'] = obj.illness

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['fullName'])):
            inputError['fullName'] = "full name is required"
            self.form['error'] = True
        else:
            if (DataValidator.isAlphaCheck(self.form['fullName'])):
                inputError['fullName'] = "full name contains letter only"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['appointmentDate'])):
            inputError['appointmentDate'] = "appointment date is required"
            self.form['error'] = True
        else:
            if (DataValidator.isAppointmentDate(self.form['appointmentDate'])):
                inputError['appointmentDate'] = "enter correct date"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['contactNumber'])):
            inputError['contactNumber'] = "contact number is required"
            self.form['error'] = True
        else:
            if (DataValidator.isPhoneCheck(self.form['contactNumber'])):
                inputError['contactNumber'] = "enter correct contact number"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['illness'])):
            inputError['illness'] = "specify the illness"
            self.form['error'] = True
        else:
            if (DataValidator.isAlphaCheck(self.form['illness'])):
                inputError['illness'] = "illness contain letter only"
                self.form['error'] = True

        return self.form['error']

    def display(self, request, params={}):
        if (params['id'] > 0):
            obj = self.get_service().get(params['id'])
            self.model_to_form(obj)
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def submit(self, request, params={}):
        r = self.form_to_model(Client())
        self.get_service().save(r)
        self.form['message'] = "Data Saved successfully"
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def get_service(self):
        return ClientService()

    def get_template(self):
        return "Client.html"
