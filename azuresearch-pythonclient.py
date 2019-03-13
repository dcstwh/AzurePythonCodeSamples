# @author Wee Hyong Tok
# @description Sample Python code to access Azure Search
# @date_created  03-13-2019

import http.client, urllib.parse, json

# Define subscription key, AzureSearch URLs, and API-version
subscriptionKey = '<subscription key>'
host = '<azure search name>.search.windows.net'
path = '/indexes/<name of index>/docs'
apiversion = '2017-11-11'

def azure_search (query):
    headers = {'api-key': subscriptionKey}
    conn = http.client.HTTPSConnection(host)
    
    params = '?search=' + query + '&api-version=' + apiversion
    
    conn.request ("GET", path + params, None, headers)
    response = conn.getresponse ()
    return response.read ()


# get the result
result = azure_search ('pizza')
print (json.dumps(json.loads(result), indent=4))