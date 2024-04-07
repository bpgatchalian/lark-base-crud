from lark.base_api import BaseAPI

lark_base_api = BaseAPI()

update_a_record_request = {
        "fields": {                
        "Name": "Bryner",
        "Age": 33,
        "Birthday": "1970/06/01",
        "Address": "Makati, Philippines"}
}

response = lark_base_api.update_a_record(json_data=update_a_record_request, record_id="recu9eqdaKMped") # change record_id

print(response.text)