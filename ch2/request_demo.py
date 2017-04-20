# coding=utf-8

import requests

URL_IP = 'http://127.0.0.1:8000/ip'
URL_GET = 'http://127.0.0.1:8000/get'


def url_simple_requests():
    response = requests.get(URL_IP)
    print ">>>>>> Response Headers:"
    print response.headers
    print ">>>>>> Response Body:"
    print response.text


def url_params_requests():
    params = {'param1': 'hello', 'param2': 'world'}
    print "Request Params:"
    print params
    response = requests.get(URL_IP, params=params)
    print ">>>>>> Response Headers:"
    print response.headers
    print ">>>>>> Response Body:"
    print response.json
    print '>>>>>> Status Code'
    print response.status_code
    print response.reason


if __name__ == '__main__':
    print "Use simple requests:"
    url_simple_requests()
    print "Use params requests:"
    url_params_requests()
