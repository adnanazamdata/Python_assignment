import urllib.request, urllib.error, urllib.parse

url = 'https://www.zoho.com/forms/templates.html'

response = urllib.request.urlopen(url)
webContent = response.read()



from bs4 import BeautifulSoup


soup = BeautifulSoup(webContent)

print(soup.get_text()) 
