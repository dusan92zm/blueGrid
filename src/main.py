#!/bin/python3
import json
import requests
import constants

def createCustomer():
    response = requests.post(constants.NewCustomerUrl,
                json.dumps(constants.NewCustomerBody),
                headers=constants.headers)
    if(response.status_code != 200):
        print("Failed to create customer.")
        return 1

    responseObject = json.loads(response.text)
    customerId = responseObject["customer"]["id"];

    newAddressUrl = constants.NewAddressUrl.replace("customerId", str(customerId));
    response = requests.post(newAddressUrl,
                json.dumps(constants.NewAddressBody),
                headers=constants.headers)
    if(response.status_code != 200):
        print("Failed to create address.")
        return 1

    responseObject = json.loads(response.text)
    addressId = responseObject["address"]["id"];

    constants.NewSubscriptionBody["address_id"] = addressId;
    response = requests.post(constants.NewSubscriptionUrl,
                json.dumps(constants.NewSubscriptionBody),
                headers=constants.headers)
    if(response.status_code != 200):
        print("Failed to create subscriptions.")
        return 1

    responseObject = json.loads(response.text)
    subscriptionId = responseObject["subscription"]["id"];

    print("Created Customer Id: {0}, Address Id: {1}, Subscription Id: {2}"
        .format(customerId, addressId, subscriptionId))
    print("Done.")

def main():
    createCustomer()

main()