# examples/delete_records.py

from base_helper.base_api import BaseAPI

app_token = "YOUR_APP_TOKEN"
table_id = "YOUR_TABLE_ID"

lark_base_api = BaseAPI(app_token, table_id)

delete_records_request = {
    "records": [
        "recu9eqThmSTV7",
        "recu9eroqd8AKu"
    ]
}

response = lark_base_api.delete_records(delete_records_request)

print(response.text)