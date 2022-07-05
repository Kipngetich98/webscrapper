from turtle import title
import requests
from bs4 import BeautifulSoup


url = "" #Input your ur here

def get_webscrapped():
    """
    Get the content from the front page of the blog
    """

    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    pages = soup.findAll("h3")

    scrapped = {i.a["href"]: i.text.strip()
                for i in pages if i.a}
    for scrap in scrapped:
        s = "{title}:  {url}".format(title=scrapped[scrap], url=scrap)
        print(s)


    return scrapped

if __name__ == "__main__":
    scrapped = get_webscrapped