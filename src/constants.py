# import urllib3
from urllib.parse import urljoin

BaseUrl = "https://api.rechargeapps.com"
headers = {
    "X-Recharge-Access-Token": "abc123",
    "Accept":"application/json",
    "Content-Type":"application/json"
}

# New Customer
NewCustomerUrl = urljoin(BaseUrl, "customers")
CustomerEmail = "dusan2322077712@gmail.com"
NewCustomerBody = {
    "email": CustomerEmail,
    "first_name": "John",
    "last_name": "Jones",
    "billing_first_name": "John",
    "billing_last_name": "Jones",
    "billing_address1": "24 5th Avenue",
    "billing_zip": "10153",
    "billing_city": "New York",
    "billing_province": "NY",
    "billing_country": "United States",
    "billing_phone":"57820586"
}

# New Address
NewAddressUrl = urljoin(BaseUrl, "customers/customerId/addresses")
NewAddressBody = {
    "address1": "24 5th Avenue",
    "address2": "",
    "city": "New York",
    "province": "NY",
    "first_name": "John",
    "last_name": "Jones",
    "zip": "10153",
    "company": "Google",
    "phone": "57820586",
    "country": "United States",
    "original_shipping_lines": [
        {
            "price": "0.00",
            "code": "Standard Shipping",
            "title": "Standard Shipping"
        }
    ],
    "shipping_lines_override": None
}

# New Subscription
NewSubscriptionUrl = urljoin(BaseUrl, "subscriptions")
NewSubscriptionBody = {
    "address_id": 0,
    "next_charge_scheduled_at":"2019-12-12T00:00:00",      
    "product_title":"Vogue",
    "price":10.5,
    "quantity":1,
    "shopify_variant_id":3844924611,
    "sku_override": False,
    "order_interval_unit":"day",
    "order_interval_frequency":"30",
    "number_charges_until_expiration": 2,
    "charge_interval_frequency":"30",
    "properties": [
        {
          "name": "grind",
          "value": "drip"
        },
        {
          "name": "size",
          "value": "medium"
        }
    ]
}