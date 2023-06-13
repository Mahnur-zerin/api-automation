import json

import requests

auth_url = "https://rentmyapidevteam1.leaperdev.rocks/api/su-admin/users/login"
headers = {
    "Accept": "*/*",
    "Content-Type": "application/json"

}
auth_payload = json.dumps({
    "email": "mleaping@leapinglogic.com",
    "password": "siterocks"
})

auth_response = requests.post(auth_url, headers=headers, data=auth_payload)
token = json.loads(auth_response.text)['result']['token']
print(token)

payment_url = "https://rentmyapidevteam1.leaperdev.rocks/api/payments/transafe-iframe-attr?client_host=https://teststore09.rentmydevteam1.admin.leaperdev.rocks"
payment_headers = {
    "Accept": "*/*",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwidXNlcl90eXBlX2lkIjoxLCJuYW1lIjoiTW9oc2luIEthYmlyIiwiZW1haWwiOiJtbGVhcGluZ0BsZWFwaW5nbG9naWMuY29tIiwiZGF0ZSI6IjIwMjMtMDYtMTIgMTI6NDk6MzkiLCJjb21wYW55X2lkIjozLCJzdG9yZV9pZCI6NTkwLCJzdWJzY3JpcHRpb24iOnsiYWNjb3VudF90eXBlIjoiRVNUQUJMSVNIRUQiLCJpc01vbnRobHkiOnRydWUsImlzQWN0aXZlIjp0cnVlLCJjYXJkIjpmYWxzZSwibmV3SW52ZW50b3J5Ijp0cnVlfSwic291cmNlIjoiYWRtaW4iLCJsb2NhdGlvbiI6NjQ3fQ.EqFAYvpwf0r9BlH3r_V_tMxKSqkxFoejPhGc0DbGMUk"
}

payment_response = requests.get(payment_url, headers=payment_headers)
payment_response = json.loads(payment_response.text)
print(json.dumps(payment_response, indent=4))

order_url = "https://rentmyapidevteam1.leaperdev.rocks/api/orders"
order_headers = {
    "Accept": "*/*",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwidXNlcl90eXBlX2lkIjoxLCJuYW1lIjoiTW9oc2luIEthYmlyIiwiZW1haWwiOiJtbGVhcGluZ0BsZWFwaW5nbG9naWMuY29tIiwiZGF0ZSI6IjIwMjMtMDYtMTIgMTI6NDk6MzkiLCJjb21wYW55X2lkIjozLCJzdG9yZV9pZCI6NTkwLCJzdWJzY3JpcHRpb24iOnsiYWNjb3VudF90eXBlIjoiRVNUQUJMSVNIRUQiLCJpc01vbnRobHkiOnRydWUsImlzQWN0aXZlIjp0cnVlLCJjYXJkIjpmYWxzZSwibmV3SW52ZW50b3J5Ijp0cnVlfSwic291cmNlIjoiYWRtaW4iLCJsb2NhdGlvbiI6NjQ3fQ.EqFAYvpwf0r9BlH3r_V_tMxKSqkxFoejPhGc0DbGMUk"
}
order_payload = json.dumps({
    "id": 202234, "first_name": "mahnur", "last_name": "zerin", "email": "mahnur+18@gmail.com", "mobile": "",
     "address_line1": "88 Park Ave", "address_line2": "", "city": "Nutley", "state": "NJ", "zipcode": "07110",
     "country": "US", "salesman": 2, "type": 1, "terminal_id": 72, "amount_tendered": "null", "custom_values": [],
     "gateway_id": 11282, "payment_gateway_name": "Transafe", "currency": "USD", "is_admin": True, "location": 647,
     "token": "1686627300040", "pickup": "null", "return_to": "null", "item_log": [], "order_source": "Admin",
     "shipping_method": "", "account": "2673460630", "capture": False, "source": "admin_cart_checkout"
})
order_request= requests.post(order_url,headers=order_headers,data=order_payload)
order_request = json.loads(order_request.text) #the response data should be loaded first before dump
print(json.dumps(order_request, indent=4))

