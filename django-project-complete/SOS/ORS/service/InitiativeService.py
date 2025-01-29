from django.db import connection

from ..models import Initiative
from .BaseService import BaseService
from ..utility.DataValidator import DataValidator


class InitiativeService(BaseService):
    def search(self, params):
        pageNo = (params["pageNo"] - 1) * self.pageSize
        sql = "select * from sos_initiative where 1=1"
        val = params.get("display", None)
        if DataValidator.isNotNull(val):
            sql += " and display like '" + val + "%%'"
        sql += " limit %s, %s"
        cursor = connection.cursor()
        result = cursor.fetchall()
        columnName = ('id', 'initiativeName', 'type', 'startDate', 'version')
        res = {
            "data": [],
        }
        res["index"] = ((params['pageNo'] - 1) * self.pageSize) + 1
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res['data'].append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def get_model(self):
        return Initiative
