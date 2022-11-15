import requests
from bs4 import BeautifulSoup
url = "https://webifyhub.web.app"

content = requests.get(url)
htmlContent = content.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)


