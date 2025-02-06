from SOS.ORS.ctl.BaseCtl import BaseCtl


class ClientCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id']=requestForm['id']
        self.form['fullName']=requestForm['fullName']
        self.form['appointmentDate']=requestForm['appointmentDate']
        self.form['contactNumber']=requestForm['contactNumber']
        self.form['illness']=requestForm['illness']

    def form_to_model(self, obj):
        pk=int(self.form['id'])
        if pk >0:
            obj.id=pk
        obj.fullName=self.form['fullName']
        obj.appointmentDate=self.form['appointmentDate']
        obj.contactNumber=self.form['contactNumber']
        obj.illness=self.form['illness']
        return obj

    def model_to_form(self, obj):
        if obj is None:
            return
        self.form['id']=obj.id
        self.form['fullName']=obj.fullName
        self.form['appointmentDate'] = obj.appointmentDate
        self.form['contactNumber'] = obj.contactNumber
        self.form['illness'] = obj.illness
        
