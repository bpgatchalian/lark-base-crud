# examples/get_records.py

from base_helper.base_api import BaseAPI

app_token = "YOUR_APP_TOKEN"
table_id = "YOUR_TABLE_ID"

lark_base_api = BaseAPI(app_token, table_id)

response = lark_base_api.get_records('YOUR_RECORD_ID')

print(response.text)