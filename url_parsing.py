try:
    from urllib.parse import urlparse, urlunparse
except:
    from urllib2 import urlparse, urlunparse

# Parse a URL
parsed_url = urlparse(
        "https://www.devdungeon.com/test/node/1?q=5&x=that#test_fragment"
    )
print(parsed_url)
print(parsed_url.scheme)
print(parsed_url.netloc)
print(parsed_url.path)
print(parsed_url.params)
print(parsed_url.query)
print(parsed_url.fragment)

# Create a URL
new_url = urlunparse(
    ("https",                   # scheme
     "www.devdungeon.com",      # Netloc
     "/archive",                # Path
     None,                      # Params
     "q=5&x=that",              # Query
     "test_fragment"))          # Fragmentrint("[*] Processing %s % href")
print(new_url)
