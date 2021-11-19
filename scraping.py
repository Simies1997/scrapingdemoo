import requests
from bs4 import BeautifulSoup
import pprint
def get_repositories():
    url_to_call = "https://www.bayut.com/to-rent/property/dubai/"
    response=requests.get(url_to_call,headers={'user-Agent':"Mozilla/5.0"})
    response_code=response.status_code
    if response_code != 200:
        print("error occured")
        return
    html_content = response.content
    dom = BeautifulSoup(html_content,'html.parser')
    all_scrapingg_repos = dom.select("div._1e33cd36 ")
    repositories = []
    for each_scrapingg_repo in all_scrapingg_repos:
        href_link = each_scrapingg_repo.a.attrs["href"]
        name = href_link[1:]
        repo = {"label":name,
               "link":"https://github.com{}".format(href_link)}
        repositories.append(repo)
        return repositories
    
if __name__== "__main__":
    print("Started scraping")
    scrapingg_repos = get_repositories()
    pprint.pprint(scrapingg_repos)
