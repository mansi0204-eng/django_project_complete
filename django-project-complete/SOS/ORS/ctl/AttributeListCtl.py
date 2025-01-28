from django.shortcuts import render, redirect

from .BaseCtl import BaseCtl
from ..models import Attribute
from ..service.AttributeService import AttributeService


class AttributeListCtl(BaseCtl):
    count=1

    def request_to_form(self, requestForm):
        self.form['display']=requestForm.get("display",None)
        self.form['datatype']=requestForm.get("datatype",None)
        self.form['isActive']=requestForm.get("isActive",None)
        self.form['description']=requestForm.get("description",None)
        self.form['ids']=requestForm.get("ids",None)

    def display(self, request, params={}):
        AttributeListCtl.count=self.form['pageNo']
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        self.form['lastId'] = Attribute.objects.last().id
        res=render(request,self.get_template(),{'pageList':self.page_list,'form':self.form})
        return res

    def next(self,request, params={}):
        AttributeListCtl.count +=1
        self.form['pageNo']=AttributeListCtl.count
        records = self.get_service().search(self.form)
        self.page_list=records['data']
        self.form['lastId']=Attribute.objects.last().id
        res = render(request, self.get_template(), {"pageList": self.page_list, "form": self.form})
        return res

    def previous(self,request, params={}):
        AttributeListCtl.count -= 1
        self.form['pageNo']=AttributeListCtl.count
        records = self.get_service().search(self.form)
        self.page_list=records['data']
        self.form['lastId']=Attribute.objects.last().id
        res = render(request, self.get_template(), {"pageList": self.page_list, "form": self.form})
        return res

    def new(self, request, params={}):
        res= redirect("/Attribute/")
        return res

    def deleteRecord(self, request, params={}):
        if not self.form['ids']:
            self.form['error']=True
            self.form['message']="Please select at least one checkbox"
        else:
            for id in self.form['ids']:
                id=int(id)
                record=self.get_service().get(id)
                if record:
                    self.get_service().delete(id)
                    self.form['message']="Data has been deleted successfully"
                else:
                    self.form['error']=True
                    self.form['message']="Data is not deleted"
        self.form['pageNo']=1
        records=self.get_service().search(self.form)
        self.page_list= records['data']
        self.form['lastId']=Attribute.objects.last().id
        return  render(request, self.get_template(),{'pageList':self.page_list,'form':self.form})

    def submit(self, request, params={}):
        AttributeListCtl.count = 1
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        if self.page_list == []:
            self.form['message'] = "No record found"
        res = render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})
        return res

    def get_template(self):
        return "AttributeList.html"

    def get_service(self):
        return AttributeService()

