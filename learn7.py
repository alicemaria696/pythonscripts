import requests
import pandas as pd
import jwt

url_api = "https://jsonplaceholder.typicode.com/users"
rows = []
response = requests.get(url_api)
"""if response.status_code == 200:
    #print(response.json())
    data = response.json()
    for i in data:
       #print(f"Username : {i['name']} and Email : {i['email']}")
       rows.append({'index':[i['id']],'Username':[i['name']],'Email':[i['email']]})
       df = pd.DataFrame(rows)
       #print(df)
       df.to_csv("user_details.csv", index=False)
        
elif response.status_code == 400:
    print("bad request")
else:
    print("url not found")"""
    
    
payload = {
    "id": 12,
    "name": "Alice Kanchan",
    "username": "Alice",
    "email": "alice@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92118-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
    "phone": "1-770-136-8131 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server AWS",
      "bs": "harness real-time cloud products"
}
}

    
response = requests.post(url_api, json = payload)
if response.status_code == 200:
    print("Connection established")
elif response.status_code == 201:
    print("new record is added")
    print(response.json())
elif response.status_code == 401:
    print("authorization failure")
else:
    print("url not found")
    
    


        
