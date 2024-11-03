# examples/delete_a_record.py

from base_helper.base_api import BaseAPI

app_token = "YOUR_APP_TOKEN"
table_id = "YOUR_TABLE_ID"

lark_base_api = BaseAPI(app_token, table_id)

response = lark_base_api.delete_a_record(record_id="recu9eqdaKMped") # change record_id

print(response.text)