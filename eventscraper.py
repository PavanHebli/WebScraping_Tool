from bs4 import BeautifulSoup as bs
import time
import helper_selenium as hs
import helperfunctions as helper
from constants import lumaEvents
import time
import random
import pandas as pd
from LumaEvents import LumaMain

start_time = time.time()

LumaMain()

print("--- %s seconds ---" % round((time.time() - start_time), 2))

