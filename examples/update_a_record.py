# examples/update_a_record.py

from base_helper.base_api import BaseAPI

app_token = "YOUR_APP_TOKEN"
table_id = "YOUR_TABLE_ID"

lark_base_api = BaseAPI(app_token, table_id)

update_a_record_request = {
        "fields": {                
        "Name": "Michael Gatchitor",
        "Age": 33,
        "Birthday": "1970/06/01",
        "Address": "Makati, Philippines"}
}

response = lark_base_api.update_a_record(json_data=update_a_record_request, record_id="recu9eqdaKMped") # change record_id

print(response.text)