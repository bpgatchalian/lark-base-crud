from lark.base_api import BaseAPI

lark_base_api = BaseAPI()

response = lark_base_api.get_records('YOUR_RECORD_ID')

print(response.text)