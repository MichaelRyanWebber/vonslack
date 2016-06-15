import requests
import json

authurl = 'https://my.vonagebusiness.com/appserver/rest/user/null?htmlLogin=bedrockmichael&htmlPassword=!Ft5!Hx9'
requrl = 'https://dashboard.vonagebusiness.com/presence/dashui?filterExtension=702,705,709,715&firstRequest=true'

s = requests.session()
s.get(authurl)
r = s.get(requrl)

slackurl = 'https://hooks.slack.com/services/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'

datastring = json.dumps(r.json(), indent=4)

print datastring

pdata = []

for ext in r.json()['extensions']:
    if ext['duration'] != -1:
        line = ext['name'] + " is on the phone with " + ext['onCallWith'] + '\n'
        pdata.append(line)
    else:
        line = ext['name'] + ' is not on a call currently\n'
        pdata.append(line)

datastring = ' '.join(pdata)
payload = {"text":datastring}
slackresponse = requests.post(slackurl, json=payload)

if slackresponse.status_code != requests.codes.ok :
    print slackresponse.content
