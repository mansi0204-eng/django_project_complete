from ..service.BaseService import BaseService
from ..models import User
from ..utility.DataValidator import DataValidator


class ForgetPasswordService(BaseService):

    def search(self,params):
        val=params.get('loginId',None)
        q= self.get_model().ojects.filter()
        if DataValidator.isNull(val):
            q=q.filter(lognId=val)
        return q

    def get_model(self):
        return User