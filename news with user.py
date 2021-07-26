import datetime
import requests
import json
from win32com.client import Dispatch
import time

def speak(str):
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(str)



if __name__ == '__main__':
    hour = int(datetime.datetime.now().hour)
    speak("Whats your good name?")
    name = input("Enter your name: ")
    if hour>=0 and hour<12:
        speak(f"Good morning! {name} Sir")
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon {name} Sir")
    else:
        speak(f"Good Evening {name} Sir")
    speak("Which country's news do you want to hear??")
    con = input("Country's name: ")
    if con== "Australia":
        speak("Australia,s news for today is: ")
        url_aus = "https://newsapi.org/v2/top-headlines?country=au&apiKey=57be975464b343bfbebfc930c904686c"
        news_aus = requests.get(url_aus)
        news_aus = news_aus.text
        news_dict_aus = json.loads(news_aus)
        arts_aus = news_dict_aus["articles"]
        for articles in arts_aus:
            print(f"Title : {articles['title']}")
            speak(articles['title'])     
            print(f"Description : {articles['description']}\n\n")
            speak(articles['description'])
            time.sleep(2)
            speak("Next news is...")   
    if con=="India":     
        speak("News for today")
        url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=57be975464b343bfbebfc930c904686c"
        news = requests.get(url)
        news = news.text
        news_dict = json.loads(news)
        arts = news_dict["articles"]
        for articles in arts:
            print(f"Title : {articles['title']}")
            speak(articles['title'])     
            print(f"Description : {articles['description']}\n\n")
            speak(articles['description'])
            time.sleep(2)
            speak("Next news is...")
    if con=="New Zealand":
        speak(" New Zealand's News for today is")
        url_nez = "https://newsapi.org/v2/top-headlines?country=nz&apiKey=57be975464b343bfbebfc930c904686c"
        news_nez = requests.get(url_nez)
        news_nez = news_nez.text
        news_dict_nez = json.loads(news_nez)
        arts_nez = news_dict_nez["articles"]
        for articles in arts_nez:
            print(f"Title : {articles['title']}")
            speak(articles['title'])     
            print(f"Description : {articles['description']}\n\n")
            speak(articles['description'])
            time.sleep(2)
            speak("Next news is...")
    if con=="America":
        speak(" America's News for today is")
        url_amr = "https://newsapi.org/v2/top-headlines?country=us&apiKey=57be975464b343bfbebfc930c904686c"
        news_amr = requests.get(url_amr)
        news_amr = news_amr.text
        news_dict_amr = json.loads(news_amr)
        arts_amr = news_dict_amr["articles"]
        for articles in arts_amr:
            print(f"Title : {articles['title']}")
            speak(articles['title'])     
            print(f"Description : {articles['description']}\n\n")
            speak(articles['description'])
            time.sleep(2)
            speak("Next news is...")      
    speak("That's all for today's news")


        
        
    

    
   









