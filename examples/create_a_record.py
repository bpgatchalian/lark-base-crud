# examples/create_a_records.py

from base_helper.base_api import BaseAPI

app_token = "YOUR_APP_TOKEN"
table_id = "YOUR_TABLE_ID"

lark_base_api = BaseAPI(app_token, table_id)

create_a_record_request = {
        "fields": {                
        "Name": "John Doe",
        "Age": 21,
        "Birthday": "1996/04/07",
        "Address": "Manila, Philippines"}
}

response = lark_base_api.create_a_record(json_data=create_a_record_request)

print(response.text)