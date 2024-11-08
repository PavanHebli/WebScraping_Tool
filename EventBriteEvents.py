from bs4 import BeautifulSoup as bs
import helper_selenium as hs
import helperfunctions as helper
from constants import EventBrite
import time
import random
import pandas as pd

def GetEventsList():
    links=[]
    for page in range(432, EventBrite.pages+1):
        print(f"[INFO] Fetching data from page: {page}")
        html = hs.GetHTML(helper.concatURL(EventBrite.baseURL, EventBrite.exploreEventsURL, f"{EventBrite.paginationURL}{page}"), className=EventBrite.exploreEventClass)
        soup = bs(html, "html.parser")
        exploreEvenets_data=soup.find_all("section", class_=EventBrite.exploreEventClass)
        # allEvenetLinks=exploreEvenets_data.find_all("a")
        for link in exploreEvenets_data:
            url=link.find("a").get('href')
            links.append(url)
        helper.UpdateFile(EventBrite.allEventsListFile, links)
        t=random.randint(2,15)
        print(f"[INFO] Sleeping for {t} seconds...")
        time.sleep(t)
    pass

# def GetEventsList():
    
#     pass

def ExctractEventData(filename, failedURL=False):
    links=helper.ReadFile(filename)
    failed_urls=[]
    csvHeader=True
    for link in reversed(links):
        pdDict={"eventName":[],
            "organizer":[],
            "date":[],
            "time":[],
            "address": [],
            "cost":[],
            "tags":[],
            "url":[]
                }
        try: 
            print(f"[INFO] fetching: {link}")
            html = hs.GetHTML(helper.concatURL(link), className=EventBrite.eventDetailesTitle)
            soup = bs(html, "html.parser")
            pdDict["url"].append(link)
            eventName=helper.ExtractInfo(soup, EventBrite.eventDetailesTitle, tag="h1")
            pdDict["eventName"].append(eventName)
            eventOrganizer=helper.ExtractInfo(soup, EventBrite.eventDetailsOrganizer, tag="strong")
            pdDict["organizer"].append(eventOrganizer)
            eventDateTime=helper.ExtractInfo(soup, EventBrite.eventDetailsDateTime, tag="span")
            eventDate=""
            eventTime=""
            if eventDateTime:
                eventDate=eventDateTime[0:3]
                eventTime=eventDateTime[4:]
            pdDict["date"].append(eventDate)
            pdDict["time"].append(eventTime)

            eventAdressTag=helper.ExtractInfo(soup, EventBrite.eventDetailsAddress, extend=True)
            eventAdress=""
            addressPTag=""
            if eventAdressTag:
                eventAdress=eventAdressTag.get_text()
                if eventAdressTag.find("p"):
                    addressPTag=eventAdressTag.find("p").get_text()
                eventAdress=f'{addressPTag} {eventAdress}'
            pdDict["address"].append(eventAdress)
            
            eventCost1=helper.ExtractInfo(soup, EventBrite.eventCost1)
            eventCost2=helper.ExtractInfo(soup, EventBrite.eventCost2)
            pdDict["cost"].append(f"{eventCost1} {eventCost2}")
            
            eventUrgencyTag1=helper.ExtractInfo(soup, EventBrite.eventUrgency)
            eventUrgencyTag2=helper.ExtractInfo(soup, EventBrite.eventUrgency2, tag="span")
            pdDict["tags"].append(f"{eventUrgencyTag1} {eventUrgencyTag2}")

            helper.UpdateOnFlyCSV(EventBrite.csvFile, pdDict, csvHeader)
            pdDict.clear()
            csvHeader=False
            t=random.randint(5, 20)
            print(f"[INFO] Sleeping for {t} seconds...")
            time.sleep(t)
        except Exception as e:
            print(f"[ERROR] Problem with the URL, Saving for reference.")
            helper.UpdateOnFlyFile(EventBrite.failedURLsFile, link)
            # failed_urls.append(link)
    
    # helper.UpdateFile(EventBrite.failedURLsFile, failed_urls, failedURLs=failedURL)
    # helper.UpdateCSV(EventBrite.csvFile, pdDict)
    pass

def RerunFailedExtraction():

    pass

def EventBriteMain():
    ExctractEventData(EventBrite.allEventsListFile)
    # if helper.IsFilePresent(EventBrite.csvFile, extension=".csv"):
    #     print("[INFO EVENT_BRITE EVENT]: if loop")
    #     if helper.IsFilePresent(EventBrite.failedURLsFile):
    #         print("[INFO EVENT_BRITE EVENT]: if loop failed URLS")
    #         ExctractEventData(EventBrite.failedURLsFile, failedURL=True)
    #     else:
    #         print("Scraping completed")
    # elif helper.IsFilePresent(EventBrite.allEventsListFile):
    #     print(f"[INFO EVENT_BRITE EVENT]: elif-1 loop {EventBrite.allEventsListFile}")
    #     ExctractEventData(EventBrite.allEventsListFile)
    # else:
    #     print("[INFO EVENT_BRITE EVENT]: else loop")
    #     GetEventsList()
    #     ExctractEventData(EventBrite.allEventsListFile)
    #     ExctractEventData(EventBrite.failedURLsFile, failedURL=True)
    pass