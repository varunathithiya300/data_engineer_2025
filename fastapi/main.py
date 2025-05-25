import requests

agro_api_key = "636c64bb621a56fad79e4da90f8ebd29"
polygon_id = "5dd8a9d57f1a850b2070af5d30d00c0d"
url = f'https://api.agromonitoring.com/agro/1.0/weather?polyid={polygon_id}&appid={agro_api_key}'

response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code, response.text)
    print(response.reason)