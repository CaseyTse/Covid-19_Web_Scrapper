import requests
import sys
import datetime
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import string
import datetime
Page = "https://www.saskatchewan.ca/government/news-and-media/2020/november/09/covid19-update-one-additional-death-190-new-cases-37-in-hospital-22-recoveries"
Articles = []

#Still needs to add the deaths for today
#Be able to Text or Email myself/others


if __name__ == "__main__":
    x = datetime.datetime.now()
    year = x.strftime("%Y")
    month = x.strftime("%m")
    day = x.strftime('%d')
    date = (month + "/" + day + "/" + year)
    page = requests.get(Page)
    soup = BeautifulSoup(page.content, 'html.parser')
    Test = soup.find(class_="column c-two-third")
    Map = Test.find('img')
 
 
    for tag in Test.find_all('p'):
        Articles.append(tag.get_text())

    # print(words)
    for Article in Articles:
        words = Article.split() 
        #need to get rid of the word + period somehow
        for index, word in enumerate(words):
            #New Cases for Today
            if word == "new" and words[index + 1] == "cases" and not words[index - 1].isalpha():
                print("New Cases: " + words[index - 1] + " for " + date )
            #Far North West
            elif word == "Far" and words[index + 1] == "North" and words[index + 2] == "West" and not words[index + 3].isalpha():
                print("Far North West Cases:" + words[index + 3])
            #Far North Central
            elif word == "Far" and words[index + 1] == "North" and words[index + 2] == "Central":
                print("Far North Central Cases:" + words[index + 3])
            #Far North East
            elif word == "Far" and words[index + 1] == "North" and words[index + 2] == "East":
                print("Far North East Cases:" + words[index + 3])
            #North West
            elif words[index - 1] != "Far" and word == "North" and words[index + 1] == "West":
                print("North West Cases:" + words[index + 2])
            #North Central
            elif words[index - 1] != "Far" and word == "North" and words[index + 1] == "Central":
                print("North Central Cases:" + words[index + 2])
            #North East
            elif words[index - 1] != "Far" and word == "North" and words[index + 1] == "East":
                print("North East Cases:" + words[index + 2])
            #Saskatoon
            elif word == "Saskatoon" and not words[index + 1].isalpha():
                print("Saskatoon Cases:" + words[index + 1])
            #Central West
            elif word == "Central" and words[index + 1] == "West":
                print("Central West Cases:" + words[index + 2])
            #Central East
            elif word == "Central" and words[index + 1] == "East":
                print("Central East Cases:" + words[index + 2])
            #Regina
            elif word == "Regina" and not words[index + 1].isalpha():
                print("Regina Cases:" + words[index + 1])
            #South West
            elif word == "South" and words[index + 1] == "West":
                print("South West Cases:" + words[index + 2])
            #South Central
            elif word == "South" and words[index + 1] == "Central":
                print("South Central Cases:" + words[index + 2])
            #South East
            elif word == "South" and words[index + 1] == "East":
                print("South East Cases:" + words[index + 2])
    #For Loop Complete
    print(Map['src'])






 
