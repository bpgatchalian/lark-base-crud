from lark.base_api import BaseAPI

lark_base_api = BaseAPI()

response = lark_base_api.delete_a_record(record_id="recu9eqdaKMped") # change record_id

print(response.text)