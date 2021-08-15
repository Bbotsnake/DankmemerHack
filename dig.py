import requests
payload = {
    'content': "pls dig"
}

header = {
    'authorization': 'Authority'
}

r = requests.post("API LINK", 
                    data=payload, headers=header)
