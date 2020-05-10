from urllib.request import urlopen
api_url = 'https://pixabay.com/images/search/nature/'
url_result = urlopen(api_url)

data = url_result.read()
print(data)
