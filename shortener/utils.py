import random
import string
from django.conf import settings
import requests
import json
SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)
def code_generator(size = 6, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size = 6):
    URLClass = instance.__class__
    new_code = None
    for i in range(100): #try 100 times, if not succeed, then reuse an old code
        new_code = code_generator(size = size)
        #check if new code already existed in database
        qs_exists = URLClass.objects.filter(shortcode = new_code).exists()
        #if not, return right away
        if not qs_exists:
            print("OK, this code has not existed!")
            return new_code
    return new_code

    qs_exists = URLClass.objects.filter(shortcode='abc123').exists()
    print("qs_exists = ", qs_exists)
    if qs_exists:
        return code_generator(size = size)
    return new_code
def addHttpIfNecessary(code):
    if code[:7] != "http://" and code[:8] != "https://":
        print("this does not have http at beginning!")
        code = "http://" + code
    return code
def checkForMalware(link):
    print("link = ", link)
    api_key='AIzaSyAsgJYrNU_OIAx2i1Rp28drZHykuuvzDx4'
    url = "https://safebrowsing.googleapis.com/v4/threatMatches:find"
    payload = {'client': {'clientId': "mycompany", 'clientVersion': "0.1"},
            'threatInfo': {'threatTypes': ["SOCIAL_ENGINEERING", "MALWARE"],
                        'platformTypes': ["ANY_PLATFORM"],
                        'threatEntryTypes': ["URL"],
                        'threatEntries': [{'url': link}]}}
    params = {'key': api_key}
    r = requests.post(url, params=params, json=payload)
    # Print response
    print("===============Response from Google:======================")
    print(r.content) 
    print(r.json())
    if "matches" in r.json():
        return True
    return False
