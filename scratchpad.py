# if helper.IsFilePresent(lumaEvents.filename):
#     links=helper.ReadFile(lumaEvents.filename)
# else:
#     html = hs.GetHTML(helper.concatURL(lumaEvents.baseURL, lumaEvents.discoverURL), className="jsx-1536647430 continent-section")
#     soup = bs(html, "html.parser")
#     continent_data=soup.find_all("div", class_=lumaEvents.continentClass)
#     for continent in continent_data:
#         # print(f"Working on #{continent[0].text}")
#         # helper.AppendFile(lumaEvents.filename, continent)
#         usa_events_link=continent.find_all("a")
#         for link in usa_events_link:
#             links.append(link.get('href'))
#             print( link.get('href'))
#         helper.AppendFile(lumaEvents.filename, links)
#         t=random.randint(2,15)
#         print(f"Sleeping for {t} seconds...")
#         time.sleep(t)

# print(links)
# for link in links:
#     print(link)
#     html = hs.GetHTML(helper.concatURL(lumaEvents.baseURL, link), className="timeline")
#     soup = bs(html, "html.parser")
#     event_data=soup.find_all("div", class_="timeline")
#     for event in event_data:
#         usa_events_link=event.find_all("a")
#         links=[]
#         for link in usa_events_link:
#             links.append(link.get('href'))
#             print( link.get('href'))
#         helper.AppendFile("lumaEventsListURL", links)
#         t=random.randint(2,15)
#         print(f"Sleeping for {t} seconds...")
#         time.sleep(t)
# if helper.IsFilePresent("lumaEventsListURL"):
#     links=helper.ReadFile("lumaEventsListURL")
#     pdDict={"organizer":[],
#            "eventName":[],
#            "date":[],
#            "time":[],
#            "address": []
#              }
#     failed_urls=[]
#     for link in links:
#         try:
#             html = hs.GetHTML(helper.concatURL(lumaEvents.baseURL, link), className=True)
#             soup = bs(html, "html.parser")
#             organizer=helper.ExtractInfo(soup, lumaEvents.organizerClass) #soup.find("div", class_=lumaEvents.organizerClass).get_text()
#             eventName=helper.ExtractInfo(soup, lumaEvents.eventNameClass, extend=True).find("h1").get_text()
#             date=helper.ExtractInfo(soup, lumaEvents.dateClass)
#             Time=helper.ExtractInfo(soup, lumaEvents.TimeClass)
#             address=helper.ExtractInfo(soup, lumaEvents.addressClass)

#             pdDict["organizer"].append(organizer)
#             pdDict["eventName"].append(eventName)
#             pdDict["date"].append(date)
#             pdDict["time"].append(Time)
#             pdDict["address"].append(address)
#             print(f"{link}, {organizer}, {eventName}, {date}, {Time}, {address}")
#             t=random.randint(2,30)
#             print(f"Sleeping for {t} seconds...")
#             time.sleep(t)
#         except:
#             failed_urls.append(link)
#     helper.AppendFile("failed_urls", failed_urls)
#     helper.UpdateCSV(lumaEvents.csvFile, pdDict)