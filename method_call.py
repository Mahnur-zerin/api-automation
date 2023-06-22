from test_cases.get_api_respone import get_api_response
import json

payment_url="https://rentmyapidevteam1.leaperdev.rocks/api/payments/transafe-iframe-attr?client_host=https://teststore09.rentmydevteam1.admin.leaperdev.rocks"
api_response = get_api_response("GET",payment_url)

