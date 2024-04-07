from lark.base_api import BaseAPI

lark_base_api = BaseAPI()

create_a_record_request = {
        "fields": {                
        "Name": "John Doe",
        "Age": 21,
        "Birthday": "1996/04/07",
        "Address": "Manila, Philippines"}
}

response = lark_base_api.create_a_record(json_data=create_a_record_request)

print(response.text)