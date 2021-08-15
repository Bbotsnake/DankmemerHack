import requests
payload = {
    'content': "pls hunt"
}

header = {
    'authorization': 'Authority'
}

r = requests.post("API LINK", 
                    data=payload, headers=header)
