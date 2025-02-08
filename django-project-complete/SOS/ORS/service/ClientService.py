from django.db import connection

from ..models import Client
from ..service.BaseService import BaseService
from ..utility.DataValidator import DataValidator


class ClientService(BaseService):
    def search(self, params):
        pageNo = (params["pageNo"] - 1) * self.pageSize
        sql = "select * from sos_client where 1=1"
        val = params.get("fullName", None)
        if DataValidator.isNotNull(val):
            sql += " and fullName like '" + val + "%%'"
        sql += " limit %s, %s"
        cursor = connection.cursor()
        print("--------", sql, pageNo, self.pageSize)
        cursor.execute(sql, [pageNo, self.pageSize])
        result = cursor.fetchall()
        columnName = ('id', 'fullName', 'appointmentDate', 'contactNumber', 'illness')
        res = {
            "data": [],
        }
        res["index"] = ((params['pageNo'] - 1) * self.pageSize) + 1
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res['data'].append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def get_model(self):
        return Client

