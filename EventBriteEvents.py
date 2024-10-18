from bs4 import BeautifulSoup as bs
import helper_selenium as hs
import helperfunctions as helper
from constants import EventBrite
import time
import random
import pandas as pd

def ScrapeEvents():
    links=[]
    html = hs.GetHTML(helper.concatURL(EventBrite.baseURL, EventBrite.exploreEventsURL), className=EventBrite.exploreEventClass)
    soup = bs(html, "html.parser")
    exploreEvenets_data=soup.find_all("div", class_=EventBrite.exploreEventClass)
    for eventSection in exploreEvenets_data:
        allEvenetLinks=eventSection.find_all("a")
        for link in allEvenetLinks:
            links.append(link.get('href'))
            print( link.get('href'))
        helper.UpdateFile(EventBrite.exploreAllEventsFile, links)
        t=random.randint(2,15)
        print(f"Sleeping for {t} seconds...")
        time.sleep(t)
    pass

def GetEventsList():
    
    pass

def ExctractEventData():
    pass

def RerunFailedExtraction():
    pass

def EventBriteMain():
    pass