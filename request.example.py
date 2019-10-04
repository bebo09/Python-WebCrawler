import requests

#GET
response = requests.get("https://www.devdungeon.com/archive") # , stream=True
print(response.text)
print(response.status_code)
print(response.headers)


# POST
response = requests.post("https://httpbin.org/anything",
                          files={"file": "The File contents"}, # can pass a list of files
                          data={"form_field_name": "form_value"},
                          params={"q": 5, "action": "delete"})

print(response.text)

# OR stream data in upload
with open('large-file.txt', 'rb') as file_contents:
    response = requests.post('https://httpbin.org/anything', data=file_contents)
    print(response.text)