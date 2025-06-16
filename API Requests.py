import requests
import json


# 1. Get Request
url = "https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)

if response.status_code == 200:
    API_Data = response.json()
    for key in API_Data:{
        print(key,":", API_Data[key])
}

else:
    print(f"Failed Status Code with: {response.status_code}")


# 2. POST Request
url2 = "https://reqres.in/api/users"
headers = {"x-api-key": "reqres-free-v1"}
data = {"name": "Saumit", "job":"Dev"}

response2 = requests.post(url2, headers = headers, data = json.dumps(data))

if response2.status_code == 201:
    print("Item created successfully")
    data = response2.json()
    for key in data:
        print(key, ":", data[key])
    
else:
    print(f"Error: {response.status_code}")



# 3. Bearer Token Implementation
#Creating User
user_url = "https://bookstore.demoqa.com/Account/v1/User"
credentials = {
    "userName": "saumit18",
    "password": "Ssc@1997"
}
headers = {
    "Content-Type": "application/json"
}

user_response = requests.post(user_url, data=json.dumps(credentials), headers=headers)

if user_response.status_code == 201:
    print("User created successfully.")
    print("Response:", user_response.json())
    user_id = user_response.json().get("userID")
elif user_response.status_code == 406:
    print("User already exists. Attempting to fetch token...")
    user_id = None
else:
    print("Error creating user:", user_response.status_code)
    print(user_response.text)
    exit()

#Generate token
token_url = "https://bookstore.demoqa.com/Account/v1/GenerateToken"
token_response = requests.post(token_url, data=json.dumps(credentials), headers=headers)

if token_response.status_code == 200:
    token_data = token_response.json()
    token = token_data.get("token")
    print("Token generated.")
    print("Response:", token_data)
else:
    print("Failed to generate token.")
    print(token_response.text)
    exit()

#Proceed only if we have both token and userId
if not user_id:
    print("UserID not available. You need to fetch it manually or from another endpoint.")
    exit()

#Add book to user account
books_url = "https://bookstore.demoqa.com/BookStore/v1/Books"
book_data = {
    "userId": user_id,
    "collectionOfIsbns": [
        {"isbn": "9781449331818"}
    ]
}

auth_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}

book_response = requests.post(books_url, data=json.dumps(book_data), headers=auth_headers)

if book_response.status_code == 201:
    print("Book added to user account.")
    print("Response:", book_response.json())
else:
    print("Error:", book_response.status_code)
    print(book_response.text)