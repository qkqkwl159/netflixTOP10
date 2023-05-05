from tkinter import *
from PIL import ImageTk
import tkinter as tk
import tkinter.ttk
import sqlite3
from csvtodb import last_update
import webbrowser
import os
import threading
from netflixcsv import trailler_urllist

exec(open("netfliximg.py",encoding="utf-8").read())

conn=sqlite3.connect('contents.db')
cur=conn.cursor()


trailler = trailler_urllist
date = last_update
print(date)

win = Tk()
win.minsize(width=700, height=388)
win.maxsize(width=700, height=388)
win.title("NETFLIX TOP 10")


# 포스터 Photoimage 값 리스트
movie_poster = list()
for pti in range(10):
    movie_poster.append(PhotoImage(file='poster\\movie_top'+str(pti+1)+'.png'))

tvshow_poster = list()
for pti in range(10):
    tvshow_poster.append(PhotoImage(file='poster\\tvshow_top'+str(pti+1)+'.png'))


#국가 리스트
    #영화
movie_contry = list()
cur.execute("select 국가 from movie")
x = cur.fetchall()
for i in x:
    if(i[0] not in movie_contry and i[0] != ''):
        movie_contry.append(i[0])


    #드라마
tvshow_contry = list()
cur.execute("select 국가 from tvshow")
x =cur.fetchall()
for i in x:
    if (i[0] not in tvshow_contry and i[0] != ''):
        tvshow_contry.append(i[0])



#장르 리스트
    #영화
movie_janre = list()
cur.execute("select 장르 from movie")
x = cur.fetchall()
for i in x:
    if(i[0] not in movie_janre and i[0] != ''):
        movie_janre.append(i[0])


    #드라마
tvshow_janre = list()
cur.execute("select 장르 from tvshow")
x = cur.fetchall()
for i in x:
    if(i[0] not in tvshow_janre and i[0] != ''):
        tvshow_janre.append(i[0])




# 탭
notebook = tk.ttk.Notebook(win)
notebook.pack()



# 표 data 삽입 버튼 기능
def treesel():
    try:
        treeview.delete(1)
        data = ''
        cur.execute(f"select 국가,출시일,장르,KATEGORY,시리즈,제목,오리지널 from movie where 제목 = '{movie_title[listbox1.curselection()[0]]}'")
        movie_info = cur.fetchall()
        print(movie_info[0])
        treeview.insert("","end",values=movie_info[0],iid=1)
        # poster label에 이미지 띄우기
        index = listbox1.index(listbox1.curselection()[0])
        image_path = movie_poster[index]
        poster_label.config(image=image_path)
    except IndexError:
        treeview.insert("","end",values=('','','','','','',''),iid=1)


def treesel2():
    try:
        treeview2.delete(1)
        data = ''
        title = tvshow_title[listbox2.curselection()[0]]
        if '\'' in title and title.count('\'') ==1:

            title = title.replace('\'','\'\'')
            print(title)
        cur.execute(f"select 국가,출시일,장르,KATEGORY,시리즈,제목,오리지널 from tvshow where 제목 = '{title}'")
        tvshow_info = cur.fetchall()
        print(tvshow_info[0])
        treeview2.insert("","end",values=tvshow_info[0],iid=1)
        # poster label에 이미지 띄우기
        index = listbox2.index(listbox2.curselection()[0])
        image_path = tvshow_poster[index]
        poster_label2.config(image=image_path)
    except IndexError:
        treeview2.insert("","end",values=('','','','','','',''),iid=1)






# 콤보박스 국가 선택목록 함수
def contry_sorting():
    rank_listbox.delete(0,9)
    index=0
    text = contry_combo.get()
    cur.execute(f"select 제목 from movie where 국가 = '{text}'")

    for data in cur:
        rank_listbox.insert(index,str(data[0]))
        index=index+1

def contry_sorting2():
    rank_listbox2.delete(0,9)
    index=0
    text = contry_combo2.get()
    cur.execute(f"select 제목 from tvshow where 국가 = '{text}'")

    for data in cur:
        rank_listbox2.insert(index,str(data[0]))
        index=index+1


# 콤보박스 장르 선택목록 함수
def janre_sorting():
    rank_listbox.delete(0,9)
    index=0
    text = janre_combo.get()
    cur.execute(f"select 제목 from movie where 장르 = '{text}'")

    for data in cur:
        rank_listbox.insert(index,str(data[0]))
        index = index + 1


def janre_sorting2():
    rank_listbox2.delete(0,9)
    index=0
    text = janre_combo2.get()
    cur.execute(f"select 제목 from tvshow where 장르 = '{text}'")

    for data in cur:
        rank_listbox2.insert(index,str(data[0]))
        index = index + 1
# 예고편 버튼 함수
def movie_trailler():
    try:
        title = trailler_urllist[listbox1.curselection()[0]]
        #title = title.replace(' ','-')

        print(title)
        url = title#'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    except IndexError:
        print('Error!!')

def tvshow_trailler():
    try:
        title = trailler_urllist[listbox2.curselection()[0]+9]

        print(title)
        def open():
            url = title
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
        th = threading.Thread(target=open)
        th.start()
    except IndexError:
        print('Error!!')
# for x in cur:
#     listbox1.insert(i,str(i+1) + '. '+ str(x[0]))
#     movie_title.append(x[0])
#     i=i+1



# 프레임 관리
frame_1=tk.Frame(win,bg="black",pady=5,height=200)     #영화탭 프레임
notebook.add(frame_1,text='영화')
#frame_1.pack(side=TOP)

frame_2=tk.Frame(win,bg="black",pady=5)     #드라마탭 프레임
#frame_2.pack(side=TOP,fill=BOTH)

notebook.add(frame_2,text='드라마')





# 프로그램 이름
image = tk.PhotoImage(file=r"Logonet.png")

title = tk.Label(frame_1,image=image,bg="black")
title.pack(side=TOP,pady=10)


update_time = tk.Label(frame_1,text=f"LAST UPDATE\n{date}",fg="white",bg='black')
update_time.place(x=520,y=10)


tv_title = tk.Label(frame_2,image=image,bg="black")
tv_title.pack(side=TOP,pady=10)

update_time2 = tk.Label(frame_2,text=f"LAST UPDATE\n{date}",fg="white",bg='black')
update_time2.place(x=520,y=10)

# 나라 정렬 콤보박스,버튼,라벨

movie_frame1 = tk.Frame(frame_1,bg='black')
movie_frame1.place(x=520,y=80)

movie_frame2 = tk.Frame(frame_1,bg='black')
movie_frame2.place(x=520,y=180)

tv_frame1 = tk.Frame(frame_2,bg='black')
tv_frame1.place(x=520,y=80)

tv_frame2 = tk.Frame(frame_2,bg='black')
tv_frame2.place(x=520,y=180)

# 영화탭
# 나라 정렬 콤보박스,버튼,라벨
contry_label = tk.Label(movie_frame1,width=8)
contry_label.config(text = '국가별 정렬',bg='black',fg='white')
contry_label.pack(side=TOP)

contry_combo = tk.ttk.Combobox(movie_frame1,height=3,width=10,values = movie_contry)
contry_combo.config(state="readonly")
contry_combo.pack(side=LEFT)


contry_sort = tk.Button(movie_frame1)
contry_sort.config(text="정렬",command=contry_sorting)
contry_sort.pack(side=RIGHT,padx=5)


# 드라마탭
contry_label2 = tk.Label(tv_frame1,width=8)
contry_label2.config(text = '국가별 정렬',bg='black',fg='white')
contry_label2.pack(side=TOP)

contry_combo2 = tk.ttk.Combobox(tv_frame1,height=3,width=10,values = tvshow_contry)
contry_combo2.config(state="readonly")
contry_combo2.pack(side=LEFT)


contry_sort2 = tk.Button(tv_frame1)
contry_sort2.config(text="정렬",command=contry_sorting2)
contry_sort2.pack(side=RIGHT,padx=5)

# 영화 탭
# 장르 정렬 콤보박스,버튼,라벨
janre_label = tk.Label(movie_frame2,width=8)
janre_label.config(text = '장르별 정렬',bg='black',fg='white')
janre_label.pack(side=TOP)

janre_combo = tk.ttk.Combobox(movie_frame2,height=3,width=10,values = movie_janre)
janre_combo.config(state="readonly")
janre_combo.pack(side=LEFT)

janre_sort = tk.Button(movie_frame2)
janre_sort.config(text="정렬",command=janre_sorting)
janre_sort.pack(side=RIGHT,padx=5)

# 드라마 탭
janre_label2 = tk.Label(tv_frame2,width=8)
janre_label2.config(text = '장르별 정렬',bg='black',fg='white')
janre_label2.pack(side=TOP)

janre_combo2 = tk.ttk.Combobox(tv_frame2,height=3,width=10,values = tvshow_janre)
janre_combo2.config(state="readonly")
janre_combo2.pack(side=LEFT)

janre_sort2 = tk.Button(tv_frame2)
janre_sort2.config(text="정렬",command=janre_sorting2)
janre_sort2.pack(side=RIGHT,padx=5)


# 리스트박스,레이블
movie_frame2 = tk.Frame(frame_1,bg='black')
movie_frame2.pack(side = TOP)

tv_frame2 = tk.Frame(frame_2,bg='black')
tv_frame2.pack(side = TOP)


# 영화 리스트 박스
movie_title = list()

image_path = tk.PhotoImage(file=r'poster\\movie_top1.png')
poster_label = tk.Label(frame_1,bg='black',text="hello",fg='white')
poster_label.config(image=image_path)
poster_label.place(x=10,y=10)

listbox1 = tk.Listbox(movie_frame2,selectmode='extend',height=10,width=23,bg='black',fg='white',highlightcolor='white')
listbox1.pack(side=LEFT,padx=10)

sql='select 제목 from movie'
cur.execute(sql)

i=0

for x in cur:
    listbox1.insert(i,str(i+1) + '. '+ str(x[0]))
    movie_title.append(x[0])
    i=i+1

print(movie_title)
# TV SHOW 리스트 박스
tvshow_title = list()

image_path2 = tk.PhotoImage(file=r'poster\\tvshow_top1.png')
poster_label2 = tk.Label(frame_2,bg='black',text="hello",fg='white')
poster_label2.config(image=image_path2)
poster_label2.place(x=10,y=10)


listbox2 = tk.Listbox(tv_frame2,selectmode='extend',height=10,width=23,bg='black',fg='white',highlightcolor='white')
listbox2.pack(side=LEFT,padx=10)

sql='select 제목 from tvshow'
cur.execute(sql)

i=0

for x in cur:
    listbox2.insert(i,str(i+1) + '. '+ str(x[0]))
    tvshow_title.append(x[0])
    i=i+1

print(tvshow_title)


# 순위 리스트 박스

# 영화 탭
index=0
rank_listbox = tk.Listbox(movie_frame2,width=20,height=10,bg='black',fg='white')
rank_listbox.pack(side=RIGHT)

for x in range(10):
    rank_listbox.insert(index,'')
    index=index+1

# 드라마 탭
index=0
rank_listbox2 = tk.Listbox(tv_frame2,width=20,height=10,bg='black',fg='white')
rank_listbox2.pack(side=RIGHT)

for x in range(10):
    rank_listbox2.insert(index,'')
    index=index+1






# 디자인
    # 영화
movie_frame3= tk.Frame(frame_1,bg='black')
movie_frame3.pack(side = TOP,pady=10)
    # 드라마
tv_frame3= tk.Frame(frame_2,bg='black')
tv_frame3.pack(side = TOP,pady=10)


# 표 버튼

    #영화
tree_btn = tk.Button(movie_frame3)
tree_btn.config(text="선택",command=treesel)
tree_btn.pack(side=LEFT,padx=20)


trailer_btn = tk.Button(movie_frame3)
trailer_btn.config(text="예고편", command = movie_trailler)
trailer_btn.pack(side=RIGHT,padx=20)

# th1 = threading.Thread(target=makeurl)
# th1.start()
    # 드라마
tree_btn2 = tk.Button(tv_frame3)
tree_btn2.config(text="선택",command=treesel2)
tree_btn2.pack(side=LEFT,padx=20)

trailer_btn2 = tk.Button(tv_frame3)
trailer_btn2.config(text="예고편", command = tvshow_trailler)
trailer_btn2.pack(side=RIGHT,padx=20)


# 표 정보



treeview = tk.ttk.Treeview(frame_1,columns = ('1','2','3','4','5','6','7'),height=1,show='headings')
treeview.pack()

treeview.column("1",width = 90)
treeview.heading("1",text="국가")

treeview.column("2",width = 80)
treeview.heading("2",text="출시일")

treeview.column("3",width = 80)
treeview.heading("3",text="장르")

treeview.column("4",width = 80)
treeview.heading("4",text="카테고리")

treeview.column("5",width = 80)
treeview.heading("5",text="시리즈")

treeview.column("6",width = 100)
treeview.heading("6",text="제목")

treeview.column("7",width = 110)
treeview.heading("7",text="오리지널")

treeview.insert("","end",values=('','','','','','',''),iid=1)

# 드라마 표

treeview2 = tk.ttk.Treeview(frame_2,columns = ('1','2','3','4','5','6','7'),height=1,show='headings')
treeview2.pack()

treeview2.column("1",width = 90)
treeview2.heading("1",text="국가")

treeview2.column("2",width = 80)
treeview2.heading("2",text="출시일")

treeview2.column("3",width = 80)
treeview2.heading("3",text="장르")

treeview2.column("4",width = 80)
treeview2.heading("4",text="카테고리")

treeview2.column("5",width = 80)
treeview2.heading("5",text="시리즈")

treeview2.column("6",width = 100)
treeview2.heading("6",text="제목")

treeview2.column("7",width = 110)
treeview2.heading("7",text="오리지널")

treeview2.insert("","end",values=('','','','','','',''),iid=1)


# 표 밑에 넓이채워주는 레이블
root_label = tk.Label(frame_1)
root_label.config(fg="white",bg="black",width=100,height=0,text='1652028 :)')
root_label.pack(side=TOP)

root_label2 = tk.Label(frame_2)
root_label2.config(fg="white",bg="black",width=100,height=0,text='1652028 :)')
root_label2.pack(side=TOP)


win.mainloop()