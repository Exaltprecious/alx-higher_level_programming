#!/usr/bin/python3
'''Script that fetches my https://alx-intranet.htbn.io/status'''

import urllib.request

if __name__ == '__main__':
    text = '''Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'''
    url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()

    print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body.decode('utf-8'))
