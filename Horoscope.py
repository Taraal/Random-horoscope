from lxml import html
import nltk
import urllib
import random
import re, string
import requests
from datetime import datetime, timezone
from bs4 import BeautifulSoup


class Horoscope:

    @staticmethod
    def getDateDay():
        date = datetime.now().strftime('%A')
        return date

    
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
        
        horoscope = Horoscope.replaceText(horoscope)
        return horoscope


    @staticmethod
    def replaceText(text):

        text = text.replace("\\n", "").replace("  ", "").replace("[", "").replace("]", "").replace("'", "").replace("�", "").replace("\"", "")
        return text
        


    @staticmethod
    def getAstroyogi(signe):
        
        url = "https://www.astroyogi.com/horoscopes/daily/" + signe + "-free-horoscope.aspx"
        response = requests.get(url)
        tree = html.fromstring(response.content)
        horoscope = str(tree.xpath(
            "//*[@id=\"today1\"]/p[1]/span/text()"))
        
        horoscope = Horoscope.replaceText(horoscope)

        return horoscope


    @staticmethod
    def getAstrologyDotCom(signe):
        url = "https://www.astrology.com/horoscope/daily/today/" + signe + ".html"
        response = requests.get(url)
        tree = html.fromstring(response.content)
        horoscope = str(tree.xpath(
            "//section[@class=\"horoscope\"]/div[3]/div[1]/p[1]/text()"
            ))

        horoscope = Horoscope.replaceText(horoscope)

        return horoscope

    @staticmethod
    def tokenizeFullHoroscope(signe):
        fullHoroscope = Horoscope.getGanesha(signe) + Horoscope.getAstrologyDotCom(signe) + Horoscope.getAstroyogi(signe)
        token = nltk.sent_tokenize(fullHoroscope)
        return token


    @staticmethod
    def getRandomHoroscope(signe):
        sentences = Horoscope.tokenizeFullHoroscope(signe)
        intList = list(range(0, len(sentences)-1))
        random.shuffle(intList)
        newHoroscope = ""

        for x in range(4):
            newHoroscope += sentences[intList[x]]
        
        newHoroscope = Horoscope.replaceText(newHoroscope)
        print(newHoroscope)



signs = [
    'aries',
    'pisces',
    'leo',
    'cancer',
    'taurus',
    'gemini',
    'virgo',
    'libra',
    'scorpio',
    'sagittarius',
    'capricorn',
    'aquarius'
]
x = 0

for sign in signs:
    print(str(x) + " - " + sign)
    x += 1

signe = input("What is your star sign ?\n")
type(signe)

Horoscope.getRandomHoroscope(signs[int(signe)])



    