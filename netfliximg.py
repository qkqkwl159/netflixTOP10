import requests
from bs4 import BeautifulSoup
import urllib
from PIL import Image
from PIL import ImageTk
import os
import shutil


file = 'poster'
if os.path.isdir(file):
    shutil.rmtree(file)



def changeurl(rank,index):
    suburl = url + rank[index].a["href"]
    subres = requests.get(suburl, headers=headers)
    subres.raise_for_status()
    subsoup = BeautifulSoup(subres.text, "lxml")
    return subsoup

#test_img = Image.open('movie_top1.jpg')
# im = test_img.convert('RGB')
# im.save('test_movie.png', 'png')


# resize_img = test_img.resize((175,260))
# resize_img.save('resize_img.png','png')

# jpg를 png로 변경하는 함수
def jtop(filename,outfilename):
    img_open=Image.open(r'poster\\'+filename+'.jpg')
    img_open.convert('RGB').save(r'poster\\'+outfilename+'.png','png')

# png파일 사이즈 재정의 함수
def resize_img(filename,outfilename):
    img_open = Image.open(r'poster\\' + filename + '.png')
    resize = img_open.resize((175,260))
    resize.save(r'poster\\' + outfilename + '.png','png')


# 새폴더 poster를 만듬
os.mkdir("poster")


url="https://flixpatrol.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
contents = soup.find_all("li", attrs={"class":"hover:text-gray-400"})
t1 = soup.find_all("li", attrs={"class":"group-hover:text-gray-400"})

movie_file = 'movie_top'
tvshow_file = 'tvshow_top'

# 탑 1 포스터.jpg 받기

img = changeurl(t1,0).find("img").get("src")
imgurl = "http://flixpatrol.com" + img
urllib.request.urlretrieve(imgurl,"poster\movie_top1.jpg")
print(' ==================== movie_top1 다운 완료 ==========================')

img = changeurl(t1,1).find("img").get("src")
imgurl = "http://flixpatrol.com" + img
urllib.request.urlretrieve(imgurl,"poster\\tvshow_top1.jpg")
print(' ==================== tvshow_top1 다운 완료 ==========================')

# 2 - 9위 포스터.jpg 받기
for num in range(9):
    img = changeurl(contents,num).find("img").get("src")
    imgurl = "http://flixpatrol.com" + img
    urllib.request.urlretrieve(imgurl, 'poster\\movie_top'+str(num+2)+'.jpg')
    print(f' ==================== movie_top{num+2} 다운 완료 ==========================')
    img = changeurl(contents, num+9).find("img").get("src")
    imgurl = "http://flixpatrol.com" + img
    urllib.request.urlretrieve(imgurl, 'poster\\tvshow_top' + str(num + 2) + '.jpg')
    print(f' ========================== tvshow_top{num + 2} 다운 완료 ==========================')
# 포스터 jpg -> png 로변경
for i in range(1, 11):
    jtop(movie_file + str(i), movie_file + str(i))
    jtop(tvshow_file + str(i), tvshow_file + str(i))


# png 포스터 크기 변경
for i in range(1,11):
    resize_img(movie_file + str(i),movie_file + str(i))
    resize_img(tvshow_file + str(i), tvshow_file + str(i))

print('''          =============================================
         │                                             │
         │                                             │
         │            이미지 다운 및 변경완료              │
         │                                             │
         │                                             │
          =============================================''')
