from django.shortcuts import render
from django.template.loader import get_template

from SOS.ORS.ctl.BaseCtl import BaseCtl
from SOS.ORS.utility.DataValidator import DataValidator
from SOS.ORS.utility.HTMLUtility import HTMLUtility


class InitiativeCtl(BaseCtl):

    def preload(self, request, params):
        self.form['type'] = request.POST.get('type', '')


        if (params['id'] > 0):
            obj=self.get_service().get(params['id'])
            self.form["type"]=obj.type

        self.static_preload={"Automatic":"Automatic","Manually":"Manually"}

        self.form["preload"]["type"]=HTMLUtility.get_list_from_dict(
            'type',
            self.form["type"],
            self.static_preload
        )


    def request_to_form(self, requestForm):
        self.form['id']=requestForm['id']
        self.form['initiativeName'] = requestForm['initiativeName']
        self.form['type'] = requestForm['type']
        self.form['startDate'] = requestForm['startDate']
        self.form['version'] = requestForm['version']

    def form_to_model(self, obj):
        pk=int(self.form['id'])
        if pk>0:
            obj.id=pk
        obj.initiativeName=self.form['initiativeName']
        obj.type=self.form['type']
        obj.startDate=self.form['startDate']
        obj.version=self.form['version']
        return obj

    def model_to_form(self, obj):
        if obj is None:
            return
        self.form['id']=obj.id
        self.form['initiativeName']=obj.initiativeName
        self.form['type']=obj.type
        self.form['startDate']=obj.startDate
        self.form['version']=obj.version

    def input_validation(self):
        super().input_validation()
        inputError=self.form['inputError']

        if(DataValidator.isNull(self.form['initiativeName'])):
            inputError['initiativeName']="Initiative Name should not be null "
            self.form['error']=True
        else:
            if(DataValidator.isAlphaCheck(self.form['initiativeName'])):
                inputError['initiativeName']="Initiative Name should contains letters only"
                self.form['error']=True

        if(DataValidator.isNull(self.form['type'])):
            inputError['type']="Type should not be Null"
            self.form['error']=True

        if(DataValidator.isNull(self.form['startDate'])):
            inputError['startDate']="Start Date should not be Null"
            self.form['error']=True
        else:
            if(DataValidator.isDate(self.form['startDate'])):
                inputError['startDate']="Enter correct Date it should be in YYYY-MM-DD"

        if(DataValidator.isNull(self.form['version'])):
            inputError['version']="Version Should not be Null"
            self.form['error']=True
        else:
            if(DataValidator.isInteger(self.form['version'])):
                inputError['version']="Version Contains Number only"
                self.form['error']=True

        return self.form['error']

    def display(self, request, params={}):
        if(params['id']>0):
            obj=self.get_service().get(params['id'])
            self.model_to_form(obj)
        res= render(request,get_template(),{'form':self.form})
        return res

    def submit(self, request, params={}):
        r=self.form_to_model()

