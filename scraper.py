from bs4 import BeautifulSoup
import html5lib
import requests
import math
import time 


def scraper():
    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0"}
    requests.packages.urllib3.disable_warnings()
    base_url='http://www.monsterindia.com/it-jobs'
    source = requests.get(base_url+'.html',headers=HEADERS,verify=False)
    soup = BeautifulSoup(source.text, "lxml")
    num_jobs = int(soup.find("div", {"class": "count pull-left"}).getText().split(' ')[-2])
    print(num_jobs)
    num_pages = int(math.ceil(num_jobs/40.0))
    print(num_pages)
    # import ipdb; ipdb.set_trace()
    for page in range(1,num_pages+1):
        page_url = base_url+'-'+str(page)+".html"
        print(page_url)
        res = requests.get(page_url,headers=HEADERS,verify=False)
        soupobj = BeautifulSoup(res.text)
        links = soupobj.find("div", class_="tab-content")
        links = links.find("ul", class_="ullilist")
        for i in links:
            jtitle=i.find("div",class_="joblnk serachjoblnk").find("div",class_="jtitle").getText().strip()
            link=i.find("div",class_="joblnk serachjoblnk").find("div",class_="jtitle").find("a",class_="title_in")['href']
            companyname=i.find("div",class_="joblnk serachjoblnk").find("div",class_="jtxt orange").getText().strip()
            location=i.find("div",class_="joblnk serachjoblnk").find("div",class_="jtxt jico ico1").getText().strip()
            exp=i.find("div",class_="joblnk serachjoblnk").find("div",class_="jtxt jico ico2").getText().strip()
            skills=i.find("div",class_="joblnk serachjoblnk").find_all("span",class_="black")[0].previous_element.getText().strip()
            summary=i.find("div",class_="joblnk serachjoblnk").find_all("span",class_="black")[1].previous_element.getText().strip()
            df_dict = {'Location':location, 'Link':link, 'Experience':exp,'Skills':skills,'Company Name':companyname,"summary":summary,"job_title":jtitle,"page_url":page_url}
            print(df_dict)
            exit()
        
if __name__ == '__main__':
    scraper()
















