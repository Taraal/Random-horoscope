from lxml import html
import nltk
import urllib
import random
import requests
from datetime import datetime, timezone
from bs4 import BeautifulSoup


class Horoscope:

    @staticmethod
    def getDate():
        date = datetime.now().strftime('%A-%d-%B')
        return date

    @staticmethod
    def getGanesha(signe):
        url = "http://www.ganeshaspeaks.com/horoscopes/daily-horoscope/" + signe
        response = requests.get(url)
        tree = html.fromstring(response.content)
        horoscope = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "").replace("[\'", "").replace("\']", "") 
        return horoscope


    @staticmethod
    def getAstrologyDotCom(signe):
        url = "https://www.astrology.com/horoscope/daily/today/" + signe + ".html"
        response = requests.get(url)
        tree = html.fromstring(response.content)
        horoscope = str(tree.xpath(
            "//section[@class='horoscope']/div[3]/div[1]/p[1]/text()"
            ))

        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "").replace("[\'","").replace("\']","")
        
        return horoscope

    @staticmethod
    def tokenizeFullHoroscope(signe):
        fullHoroscope = Horoscope.getGanesha(signe) + Horoscope.getAstrologyDotCom(signe)
        token = nltk.sent_tokenize(fullHoroscope)
        return token


    @staticmethod
    def getRandomHoroscope(signe):
        sentences = Horoscope.tokenizeFullHoroscope(signe)
        intList = list(range(0, len(sentences)-1))
        random.shuffle(intList)
        newHoroscope = ""

        for x in range(int(len(sentences)/2)):
            newHoroscope += sentences[intList[x]]
        print(newHoroscope)

Horoscope.getRandomHoroscope("virgo")

    