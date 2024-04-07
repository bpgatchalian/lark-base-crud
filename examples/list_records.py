from lark.base_api import BaseAPI

lark_base_api = BaseAPI()

response = lark_base_api.list_records()

print(response.text)