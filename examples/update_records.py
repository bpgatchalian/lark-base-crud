# examples/update_records.py

from base_helper.base_api import BaseAPI

app_token = "YOUR_APP_TOKEN"
table_id = "YOUR_TABLE_ID"

lark_base_api = BaseAPI(app_token, table_id)

update_records_request = {
    "records": [
        {
            "record_id": "recu9eqThmSTV7", # change record_id
            "fields": {
                "Name": "Lisa Davis",
                "Age": 41,
                "Birthday": "1970/07/22",
                "Address": "No.50, XX Road, Seattle, US"
            }
        },
        {
            "record_id": "recu9eroqd8AKu", # change record_id
            "fields": {
                "Name": "Amit Kohli",
                "Age": 28,
                "Birthday": "1995/04/01",
                "Address": "No.10, xx Road, Los Angeles, US"
            }
        }        
    ]
}

response = lark_base_api.update_records(update_records_request)

print(response.text)