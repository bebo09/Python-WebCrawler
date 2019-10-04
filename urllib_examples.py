# HTTP GET nad POST request with standard library
try:
    from urllib.request import urlopen, Request
except:
    from urllib2 import urlopen, Request
# Open URL wth String

response = urlopen("https://www.cnbc.com")
print(response.read())

print("- - - - - - - - - - - - -")

# Or prebuild the request

request = Request("https://www.cnbc.com")
request.add_header("User-agent", "Not Firefox")
response = urlopen(request)
print(response.read())


