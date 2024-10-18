from bs4 import BeautifulSoup as bs
import helper_selenium as hs
import helperfunctions as helper
from constants import lumaEvents
import time
import random
import pandas as pd

def GetEventData(filename):
    links=helper.ReadFile(filename)
    pdDict={"organizer":[],
            "eventName":[],
            "date":[],
            "time":[],
            "address": []
                }
    failed_urls=[]
    for link in links:
        try:
            html = hs.GetHTML(helper.concatURL(lumaEvents.baseURL, link), className=True)
            soup = bs(html, "html.parser")
            organizer=helper.ExtractInfo(soup, lumaEvents.organizerClass) #soup.find("div", class_=lumaEvents.organizerClass).get_text()
            eventName=helper.ExtractInfo(soup, lumaEvents.eventNameClass, extend=True).find("h1").get_text()
            date=helper.ExtractInfo(soup, lumaEvents.dateClass)
            Time=helper.ExtractInfo(soup, lumaEvents.TimeClass)
            address=helper.ExtractInfo(soup, lumaEvents.addressClass)
            pdDict["organizer"].append(organizer)
            pdDict["eventName"].append(eventName)
            pdDict["date"].append(date)
            pdDict["time"].append(Time)
            pdDict["address"].append(address)
            print(f"{link}, {organizer}, {eventName}, {date}, {Time}, {address}")
            t=random.randint(lumaEvents.randomStart,lumaEvents.randomStop)
            print(f"Sleeping for {t} seconds...")
            time.sleep(t)
        except:
            failed_urls.append(link)
            pass
    # helper.UpdateFile(lumaEvents.failedURLsFile, failed_urls)
    helper.UpdateCSV(lumaEvents.csvFile, pdDict)

def ExtractEventList(filename):
    GetEventData(filename)
    

def GetLocationsList(filename):
    links=helper.ReadFile(lumaEvents.eventsFile)
    for link in links:
        html = hs.GetHTML(helper.concatURL(lumaEvents.baseURL, link), className="timeline")
        soup = bs(html, "html.parser")
        event_data=soup.find_all("div", class_="timeline")
        for event in event_data:
            usa_events_link=event.find_all("a")
            links=[]
            for link in usa_events_link:
                links.append(link.get('href'))
                print( link.get('href'))
            helper.UpdateFile("lumaEventsListURL", links)
            t=random.randint(lumaEvents.randomStart,lumaEvents.randomStop)
            print(f"Sleeping for {t} seconds...")
            time.sleep(t)
    pass

def ScrapeLocations():
    links=[]
    html = hs.GetHTML(helper.concatURL(lumaEvents.baseURL, lumaEvents.discoverURL), className=lumaEvents.continentClass)
    soup = bs(html, "html.parser")
    continent_data=soup.find_all("div", class_=lumaEvents.continentClass)
    for continent in continent_data:
        usa_events_link=continent.find_all("a")
        for link in usa_events_link:
            links.append(link.get('href'))
            print( link.get('href'))
        helper.UpdateFile(lumaEvents.eventsFile, links)
        t=random.randint(2,15)
        print(f"Sleeping for {t} seconds...")
        time.sleep(t)
    pass

def LumaMain():
    if helper.IsFilePresent(lumaEvents.csvFile, extension=".csv"):
        print("[INFO LUMA EVENT]: if loop")
        if helper.IsFilePresent(lumaEvents.failedURLsFile):
            print("[INFO LUMA EVENT]: if loop failed URLS")
            GetEventData(lumaEvents.failedURLsFile)
        else:
            print("Scraping completed")
    elif helper.IsFilePresent(lumaEvents.eventListFile):
        print(f"[INFO LUMA EVENT]: elif-1 loop {lumaEvents.eventListFile}")
        ExtractEventList(lumaEvents.eventListFile)
        
    elif helper.IsFilePresent(lumaEvents.eventsFile):
        print(f"[INFO LUMA EVENT]: elif-2 loop {lumaEvents.eventListFile}")
        GetLocationsList(lumaEvents.eventsFile)
    else:
        print("[INFO LUMA EVENT]: else loop")
        ScrapeLocations()
        GetLocationsList(lumaEvents.eventsFile)
        ExtractEventList(lumaEvents.eventListFile)
        GetEventData(lumaEvents.failedURLsFile)

