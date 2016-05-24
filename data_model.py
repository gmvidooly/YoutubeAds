from storage import DataServerSql
import json
from bottle import response


class DataClass(object):

    def __init__(self):
        self.data_sql = DataServerSql()
        self.ver = "v1"

    def get_channels(self):
        channels_list = []
        _sql = "SELECT videoid FROM trending where country='IN' group by videoid order by id desc limit 500 "
        results = self.data_sql.execute_query(_sql, 'select')
        if results is not None:
            for data in results:
                if data is not None:
                    channels_list.append(data)

        response.status = 200
        response_data = {'channels_list': channels_list}
        response_content = json.dumps(response_data)
        response.content_type = "application/json"

        return response_content
