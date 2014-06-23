from wikitools import wiki
from wikitools import api
# create a Wiki object
site = wiki.Wiki("http://localhost:8888/mediawiki-1.17.0/api.php") 
# define the params for the query
params = {'action':'query', 'titles':'Main Page'}
# create the request object
request = api.APIRequest(site, params)
# query the API
result = request.query()

print result

params = {'action':'query','prop':'info','intoken':'edit','titles':'Main_Page'}
request = api.APIRequest(site, params)
result = request.query()
token = result['query']['pages']['1']['edittoken']

text="""
{{Descriptive_Summary
|Title=Test Collection

}}
[[Category:Collections]]
[[Category:University Archives collections]]
[[Category:English-language collections]]
"""

params = {'action':'edit', 'title':'Test Collection','token':token,'text':text}
request = api.APIRequest(site, params)
result = request.query()