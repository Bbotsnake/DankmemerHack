import requests
payload = {
    'content': "pls fish"
}

header = {
    'authorization': 'Authority'
}

r = requests.post("API LINK", 
                    data=payload, headers=header)
