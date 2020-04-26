from bs4 import BeautifulSoup
import requests

search = input("Search for: ")
params = {"q": search}
bing = requests.get("http://www.bing.com/search", params=params)

print(bing.url)
print(bing)

soup = BeautifulSoup(bing.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})

links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print()
        print(item_text)
        print(item_href)
        print("Summary:", item.find("p").text)
