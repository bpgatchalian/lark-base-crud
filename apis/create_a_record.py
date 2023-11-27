from lark.base_table import BitableAPI
from lark.lark_auth import Authenticator

def main():
    bitable_api = BitableAPI()
    new_refresh_token = Authenticator()
    refresh_token = new_refresh_token.get_refresh_token()  # generate new refresh token

    # Input
    order_no = "666"
    product_name = "Gloves (Style A)"
    order_status = "Reviewing"
    customer_name = "Mr. Han"
    purchase_qty = 7
    order_amount = 1500
    order_date = "2022/10/26"
    est_delivery_date = "2022/10/31"

    # Call the API
    response = bitable_api.create_a_record(
        order_no, product_name, order_status, customer_name, purchase_qty, order_amount, order_date, est_delivery_date
    )

    print(response.text)

if __name__ == "__main__":
    main()
