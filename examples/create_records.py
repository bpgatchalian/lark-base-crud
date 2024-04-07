from lark.base_api import BaseAPI

lark_base_api = BaseAPI()

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