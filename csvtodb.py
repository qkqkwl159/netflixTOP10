import csv
import os.path
import sqlite3
from datetime import *


exec(open("netflixcsv.py",encoding="utf-8").read())

file = 'contents.db'
if os.path.isfile(file):
    os.remove(file)

datalist=list()
temp=''
jan=''
with open('movie.csv','r')as f1:
    all=csv.reader(f1)
    for i in all:
        print(i)
        temp = i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]
        datalist.append(temp)
print(datalist)
try:
    con=sqlite3.connect("contents.db")
    cur=con.cursor()
    cur.execute("create table movie('구분','국가','출시일','장르','KATEGORY','시리즈','제목','오리지널')")
    for t in datalist:
        cur.execute("insert into movie values(?,?,?,?,?,?,?,?)",t)
    cur.execute("select * from movie")
    for row in cur:
        print(row)
finally:
    con.commit()
    con.close()

datalist.clear()
with open('tvshow.csv','r')as f2:
    all=csv.reader(f2)
    for i in all:

        temp = i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]
        datalist.append(temp)


try:
    con=sqlite3.connect("contents.db")
    cur=con.cursor()
    cur.execute("create table tvshow('구분','국가','출시일','장르','KATEGORY','시리즈','제목','오리지널')")
    for t in datalist:
        cur.execute("insert into tvshow values(?,?,?,?,?,?,?,?)",t)
    cur.execute("select * from movie")
    for row in cur:
        print(row)
finally:
    con.commit()
    con.close()


last_update =datetime.now()
last_update = last_update.strftime("%Y-%m-%d %a %H:%M")


print('''          =============================================
         │                                             │
         │                                             │
         │                DB 생성 완료                   │
         │                                             │
         │                                             │
          =============================================''')
