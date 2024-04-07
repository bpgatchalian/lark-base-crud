from lark.base_api import BaseAPI

lark_base_api = BaseAPI()

delete_records_request = {
    "records": [
        "recu9eqThmSTV7",
        "recu9eroqd8AKu"
    ]
}

response = lark_base_api.delete_records(delete_records_request)

print(response.text)