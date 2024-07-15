import urllib.request, urllib.parse, urllib.error
import json, ssl

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    address = address.strip()
    url = serviceurl + urllib.parse.urlencode({'q': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('--- failed to retrieve ---')
        print(data)
        break

    if len(js['features']) == 0:
        print('--- object not found ---')
        print(data)
        break

    # print(json.dumps(js, indent=4))

    print('Plus code', js['features'][0]['properties']['plus_code'])