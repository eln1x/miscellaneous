#!/usr/bin/env python

import requests
# import logging

# try:
#     import http.client as http_client
# except ImportError:
#     # Python 2
#     import httplib as http_client
# http_client.HTTPConnection.debuglevel = 1
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True



url = 'https://www.facebook.com/ajax/login/help/identify.php?ctx=recover&dpr=1'
#ser-Agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04
user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04'}
cookies = {
'fr': '0mhwKXOQQSYLxtBlYtzPlgiMbCPBQ.BYlE_H.Sy.AAA.0.0.BYmG4P.AWVqoyoF',
'datr': 'x0-UWOy6cVTV7f',
'sb': 'R9SVWL1MKn7EsFp',
'lu': 'gAjTKdP3y9fcaeX8EDQ',
'locale': 'en_GB',
'reg_fb_ref': 'https://www.facebook.com/login/identify?ctx=recover&lwv=110',
'av': '1',
'act': '1476030173938/0',
'reg_fb_gate': 'https://www.facebook.com/?stype=lo&jlou=AffNm0SU1Am4f959IMoPaEhN9Cuov2OMfG_-5wqomqaxTZQ_t2oRQmg&smuh=64217&lh=Ac-ZXEBPn4Az8hgD'
}

data = {}
data['lsd']='AVoJ0ffB',
data['email']='V@GMAIL.COM',
data['did_submit']='Search',
data['__user']='0',
data['__a']='1',
data['__dyn']='7xe1xG12wAxu13wm8gxZ3ocWwAyUG4XzEa8uwh9UcU88lwIyo8obo6ucxG48hwv9FovgeFUuzUhzE2HBUfE',
data['__af']='i0',
data['__req']='5',
data['__be']='-1',
data['__pc']='PHASED:DEFAULT',
data['__rev']='2814629',


r = requests.post(url,data=data,headers=user_agent, cookies=dict(cookies))


print r.text

