
# request module

# Installing module
# pip install requests

# Import requests module
import requests
response = requests.get("https://my-json-server.typicode.com/typicode/demo/posts")
print(response.json())