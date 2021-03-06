import requests
from pprint import pprint

response = requests.post(
    'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
    headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
response.raise_for_status()
payload=response.json()
pprint(payload)

response = requests.get('https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',headers={'X-Auth-Token':payload['Token']})
lista=response.json()['response']
array=[]
for i in range(len(lista)):
    array.append([lista[i]['family'],lista[i]['hostname'],lista[i]['managementIpAddress'],lista[i]['lastUpdated'],lista[i]['reachabilityStatus']])
pprint(array)
