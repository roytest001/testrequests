#coding=utf-8

import urllib
import urllib2


URL_IP = 'http://127.0.0.1:8000/ip'
URL_GET = 'http://127.0.0.1:8000/get'

def url_simple_urllib():
    response = urllib2.urlopen(URL_IP)
    print ">>>>>> Response Headers:"
    print response.info()
    print ">>>>>> Response Body:"
    print ''.join([line for line in response.readlines()])

def url_params_urllib2():
    params = urllib.urlencode({'param1': 'hello',   'param2': 'world'})
    print "Request Params:"
    print params
    response = urllib2.urlopen('?'.join([URL_GET,'%s']) % params)
    print ">>>>>> Response Headers:"
    print response.info()
    print ">>>>>> Response Body:"
    print ''.join([line for line in response.readlines()])
    print '>>>>>> Status Code'
    print response.getcode()


if __name__ == '__main__':
    print "Use simple urllib2"
    url_simple_urllib()
    print "Use params urllib2"
    url_params_urllib2()