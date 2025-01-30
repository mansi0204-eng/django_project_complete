from django.shortcuts import render, redirect
from .BaseCtl import BaseCtl

from ..models import Initiative
from ..service.InitiativeService import InitiativeService


class InitiativeListCtl(BaseCtl):
    count = 1

    def request_to_form(self, requestForm):
        self.form['initiativeName'] = requestForm.get('initiativeName', None)
        self.form['type'] = requestForm.get('type', None)
        self.form['startDate'] = requestForm.get('startDate', None)
        self.form['version'] = requestForm.get('version', None)
        self.form['ids'] = requestForm.getlist('ids', None)

    def display(self, request, params={}):
        InitiativeListCtl.count = self.form['pageNo']
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        # self.form['lastId'] = Initiative.objects.last().id
        res = render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})
        return res

    def next(self, request, params={}):
        InitiativeListCtl.count += 1
        self.form['pageNo'] = InitiativeListCtl.count
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        self.form['lastId'] = Initiative.objects.last().id
        res = render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})
        return res

    def previous(self, request, params={}):
        InitiativeListCtl.count -= 1
        self.form['pageNo'] = InitiativeListCtl.count
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        self.form['lastId'] = Initiative.objects.last().id
        res = render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})
        return res

    def deleteRecord(self, request, params={}):
        if not self.form['ids']:
            self.form['error'] = True
            self.form['message'] = "Please select at least one checkbox"
        else:
            for id in self.form['ids']:
                id = int(id)
                record = self.get_service().get(id)
                if record:
                    self.get_service().delete(id)
                    self.form['message'] = "Data has been deleted successfully"
                else:
                    self.form['error'] = True
                    self.form['message'] = "Data was not deleted"

        self.form['pageNo'] = 1
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        # self.form['lastId'] = Initiative.objects.last().id
        return render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})

    def submit(self, request, params={}):
        InitiativeListCtl.count = 1
        records = self.get_service().search(self.form)
        self.page_list = records['data']
        if self.page_list == []:
            self.form['message'] = "No record found"
        res = render(request, self.get_template(), {'pageList': self.page_list, 'form': self.form})
        return res

    def get_template(self):
        return "InitiativeList.html"

    def get_service(self):
        return InitiativeService()