# Functions 
#  2 types of function 


# 1 NOn input function 

# for eg Time ,Data ,Upload speed ,speedtest

import datetime
import email
import imaplib

from wikipedia import wikipedia

from Speak import Say


def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)


def Date():
    date = datetime.date.today()
    Say(date)


def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)


def NonInputExecution(query):
    qry = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()
    elif "day" in query:
        Day()


# 2 Input function

# google search 
# wikepedia 
# youtube

import pywhatkit


def InputExecution(tag, query):
    if "wikipedia" in tag:
        name = str(query).replace("who is", "").replace("about", "").replace("wikipedia", "")
        result = wikipedia.summary(name)
        Say(result)

    elif "google" in tag:
        query = str(query).replace("google", "")
        query = query.replace("search", "")

        pywhatkit.search(query)

