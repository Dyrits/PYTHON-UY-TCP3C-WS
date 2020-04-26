from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

# search = input("Search for: ")
# params = {"q": search}
href = input("Enter an URL: ")
link = requests.get(href)
print(link.url)
print(link)

soup = BeautifulSoup(link.text, "html.parser")
links = soup.findAll("img")

for item in links:
    try:
        img_url = requests.get(item.attrs["src"])
        print("Getting", img_url)
        img = Image.open(BytesIO(img_url.content))
        img.save("./ScrappedIMGS/ScrappedIMG-" +
                 item.attrs["alt"])
    except:
        continue
