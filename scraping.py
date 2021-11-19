import requests
from bs4 import BeautifulSoup
def get_repositories():
    url_to_call = "https://www.bayut.com/to-rent/property/dubai/"
    response=requests.get(url_to_call,headers={'user-Agent':"Mozilla/5.0"})
    response_code=response.status_code
    if response_code != 200:
        print("error occured")
        return
    html_content = response.content
    dom = BeautifulSoup(html_content,'html.parser')
    dom.select()
if __name__== "__main__":
    print("Started scraping")
    get_repositories()
