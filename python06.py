'''
python dictionary = json yang berfungsi utk pembuatan REST API 
referensi data https://jsonplaceholder.typicode.com/users
'''

from xml.dom import UserDataHandler


users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        
            
    }
}
print (users)
print ("\n")
print (users["id"]) #panggil dgn key
print (users["name"])
print (users["username"])
print (users["email"])
print (users["address"])
print (users["address"]["zipcode"])

print("\n dari dict ke json")
print (users)
print (type(users))
import json #panggil package json
result = json.dumps(users) #menjadikan string
print (result)
print (type(result))

with open ("result.json","w") as file : #membuat file
    json.dump (users, file)