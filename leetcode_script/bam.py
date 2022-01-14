#!/usr/bin/env python3

# hardcoded csv is required as mentioned in main
# requirements : pandas
# question time is hardcoded, can be changed as comfort

from pandas import read_csv
from webbrowser import open as webopen
from time import sleep
from threading import Thread

easy_time   = 600  # 10 mins 
medium_time = 1200 # 20 mins
hard_time   = 2700 # 45 mins

def make_df(file_name):
    df = read_csv(file_name,header = None)
    return df

def select_question(df):
    row = df.sample(n=1)
    return(row.values.tolist())

def open_link(url):
    webopen(url)

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        sleep(1)
        t -= 1
      
    print("Time's up!!")

def main():
    df = make_df("leetcode.csv")
    question = select_question(df)
    name = question[0][0]
    type = question[0][1].lower()
    link = question[0][2]

    print(name)
    t1 = Thread(target=open_link, args=(link,))

    open_link(link)

    if   (type == "easy"):
        #countdown(easy_time)
        t2 = Thread(target=countdown, args=(easy_time,))
        t1.start()
        t2.start()
    elif (type == "medium"):
        #countdown(medium_time)
        t2 = Thread(target=countdown, args=(medium_time,))
        t1.start()
        t2.start()
    elif (type == "hard"):
        #countdown(hard_time)
        t2 = Thread(target=countdown, args=(hard_time,))
        t1.start()
        t2.start()
    
    t1.join()
    t2.join()


main()
