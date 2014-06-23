from wikitools import wiki, api

usr = 'dcbot'
pwd = 'digicol'

site = wiki.Wiki("http://localhost:8888/w/api.php") 
site.login(usr, password=pwd)

title = 'Test Page'
params = {'action':'query','prop':'info','intoken':'edit','titles':title}
request = api.APIRequest(site, params)
result = request.query()
pages = result['query']['pages']

print result

edittoken = None
for k, p in pages.items():
    print p
    if 'edittoken' in p:
        edittoken = p['edittoken']
        break

print edittoken