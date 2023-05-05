import requests
from bs4 import BeautifulSoup
import urllib
import csv

url="https://flixpatrol.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
contents = soup.find_all("li", attrs={"class":"hover:text-gray-400"})
t1 = soup.find_all("li", attrs={"class":"group-hover:text-gray-400"})

infolst=list() #영화 정보 담는 리스트
trailler_urllist = list() #예고편 URL 리스트
with open('movie.csv','w',encoding='utf-8',newline='')as f1:
    row = csv.writer(f1)
    lnk = url + t1[0].a["href"]  # 1위 링크
    print(lnk)
    trailler_urllist.append(lnk+'trailers/')
    suburl = lnk
    subres = requests.get(suburl, headers=headers)
    subres.raise_for_status()
    subsoup = BeautifulSoup(subres.text, "lxml")
    info = subsoup.find_all("div", attrs={"class": "flex flex-wrap text-sm leading-6 text-gray-500"})
    info_text = info[0].get_text().split('|')
    for data in info_text:
        data = data.strip()
        if (data != "Netflix"):
            infolst.append(data)
        else:
            Norig=1
    if (len(info_text) <= 6):
        for i in range(6 - len(infolst)):
            infolst.append('')
    infolst.append(t1[0].a.get_text())
    if (Norig == 1):
        infolst.append("NETFLIX ORIGINAL")
    else:
        infolst.append('')
    print(infolst)
    row.writerow(infolst)
    for num in range(9):
        infolst.clear()
        Norig=0
        lnk = url+contents[num].a["href"] # 2 - 10위 링크
        print(lnk)
        trailler_urllist.append(lnk + 'trailers/')
        suburl = lnk
        subres = requests.get(suburl, headers=headers)
        subres.raise_for_status()
        subsoup = BeautifulSoup(subres.text, "lxml")
        info = subsoup.find_all("div",attrs={"class":"flex flex-wrap text-sm leading-6 text-gray-500"})
        info_text=info[0].get_text().split('|')
        for data in info_text:
            data = data.strip()
            if(data!="Netflix"):
                infolst.append(data)
            else:
                Norig = 1
        if(len(info_text)<=6):
            for i in range(6-len(infolst)):
                infolst.append('')
        infolst.append(contents[num].a.get_text())
        if (Norig == 1):
            infolst.append("NETFLIX ORIGINAL")
        else:
            infolst.append('')
        print(infolst)
        row.writerow(infolst)

infolst.clear()
with open('tvshow.csv','w',encoding='utf-8',newline='')as f2:
    row = csv.writer(f2)
    lnk = url + t1[1].a["href"]
    Norig=0
    print(lnk)
    trailler_urllist.append(lnk + 'trailers/')
    suburl = lnk
    subres = requests.get(suburl, headers=headers)
    subres.raise_for_status()
    subsoup = BeautifulSoup(subres.text, "lxml")
    info = subsoup.find_all("div", attrs={"class": "flex flex-wrap text-sm leading-6 text-gray-500"})
    info_text = info[0].get_text().split('|')
    for data in info_text:
        data = data.strip()
        if (data != "Netflix"):
            infolst.append(data)
        else:
            Norig = 1
    if (len(info_text) <= 6):
        for i in range(6 - len(infolst)):
            infolst.append('')
    infolst.append(t1[1].a.get_text())
    if (Norig == 1):
        infolst.append("NETFLIX ORIGINAL")
    else:
        infolst.append('')
    print(infolst)
    row.writerow(infolst)
    for num in range(9):
        infolst.clear()
        Norig=0
        lnk = url+contents[num+9].a["href"]
        print(lnk)
        trailler_urllist.append(lnk + 'trailers/')
        suburl = lnk
        subres = requests.get(suburl, headers=headers)
        subres.raise_for_status()
        subsoup = BeautifulSoup(subres.text, "lxml")
        info = subsoup.find_all("div",attrs={"class":"flex flex-wrap text-sm leading-6 text-gray-500"})
        info_text=info[0].get_text().split('|')
        for data in info_text:
            data = data.strip()
            if(data!="Netflix"):
                infolst.append(data)
            else:
                Norig=1
        if(len(info_text)<=6):
            for i in range(6-len(infolst)):
                infolst.append('')
        infolst.append(contents[num+9].a.get_text())
        if(Norig==1):
            infolst.append("NETFLIX ORIGINAL")
        else:
            infolst.append('')
        print(infolst)
        row.writerow(infolst)

print('''          =============================================
         │                                             │
         │                                             │
         │             데이터 크롤링 완료                 │
         │                                             │
         │                                             │
          =============================================''')

# with open('top10.csv','w',newline='')as fp:
#     row = csv.writer(fp);
#     row.writerow(["순위","영화","TV SHOW"])
#     for num in range(9):
#         if num == 0:
#             t1m = t1[num].a.get_text()
#             t1tv= t1[num+1].a.get_text()
#             row.writerow([str(num+1)+"위",t1m,t1tv])
#         movies = contents[num].a.get_text()
#         tvshow = contents[num + 9].a.get_text()
#         row.writerow([str(num+2)+"위",movies,tvshow])
# #link = t1[0].a["href"]
# #print("https://flixpatrol.com/"+link)
# ln="https://flixpatrol.com/"
#
# with open('movieinfo.csv','w',newline='')as f2:
#     row =csv.writer(f2)
#     row.writerow(["영화명" ,"링크","국가","장르"])
#     for num in range(9):
#         moviesln = contents[num].a["href"]
#         movies = contents[num].a.get_text()
#
#
#         if num == 0:
#             t1mln = t1[num].a["href"]
#             t1m = t1[num].a.get_text()
#             row.writerow([t1m,ln+t1m,])
#         row.writerow([movies,ln+moviesln])
#         url =ln+moviesln
#         res1 = requests.get(url, headers=headers)
#         res1.raise_for_status()
#         soup1 = BeautifulSoup(res1.text, "lxml")
#         info = soup1.find_all("div",attrs={"class":"flex flex-wrap text-sm leading-6 text-gray-500"})
#         info_text=info[0].get_text().split('|')
#         for i in info_text:
#             minfo = []
#             i = i.strip()
#             row.writerow([i])





