# examples/create_records.py

from base_helper.base_api import BaseAPI

app_token = "YOUR_APP_TOKEN"
table_id = "YOUR_TABLE_ID"

lark_base_api = BaseAPI(app_token, table_id)

create_records_request = {
    "records": [
        {
            "fields": {
                "Name": "Lisa Davis",
                "Age": 41,
                "Birthday": "1970/07/22",
                "Address": "No.50, XX Road, Seattle, US"
            }
        },
        {
            "fields": {
                "Name": "Amit Kohli",
                "Age": 28,
                "Birthday": "1995/04/01",
                "Address": "No.10, xx Road, Los Angeles, US"
            }
        }        
    ]
}

response = lark_base_api.create_records(create_records_request)

print(response.text)