import requests

def query_api_get(url, headers, params, json_payload,number_of_attempts=1):
    attempt = 0
    res = None

    while attempt < int(number_of_attempts):
        attempt = attempt + 1
        res = requests.get(url, params=params, headers=headers, json=json_payload)
        if res.status_code == 200:
            break
    
    try:
        return { 'code': res.status_code, 'json' : res.json() }
    
    except:
        return { 'code': res.status_code, 'json' : None, 'text': res.text }

def query_api_post(url, headers, params, json_payload, number_of_attempts=1):
    attempt = 0
    res = None

    while attempt < int(number_of_attempts):
        attempt = attempt + 1
        res = requests.post(url, params=params, headers=headers, json=json_payload)
        if res.status_code == 200:
            break

    try:
        return { 'code': res.status_code, 'json' : res.json() }
    
    except:
        return { 'code': res.status_code, 'json' : None, 'text': res.text }
