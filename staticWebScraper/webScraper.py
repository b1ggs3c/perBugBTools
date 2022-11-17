import requests
from bs4 import BeautifulSoup


#edit    URL = "Enter URL Here"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
#delete     results = soup.find(id="ELEMENT by ID")

print("\n==============================\n")
python_query = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
python_query_elements = [
    h2_element.parent.parent.parent for h2_element in python_query
]

#ex. <h2 class="man name">RANDOM TEXT</h2>
for classname_element in python_query_elements:
    #tag = classname_element variable
    #edit   classname_element = classname_element.find("h2", class_="man name")
    #edit   classname_element = classname_element.find("h3", class_="man name")
    #edit   classname_element = classname_element.find("p", class_="man name")
    print(classname_element.text.strip())
    print(classname_element.text.strip())
    print(classname_element.text.strip())

print("\n==============================\n")
    link_url = classname_element.find_all("a")[1]["href"]
    print(f"ALL LINKS {link_url}\n")
    print()
