import pytz
from datetime import datetime
from pytz import timezone

eastern = timezone('Europe/Amsterdam') #timezone from database
loc_dt = eastern.localize(datetime.now()) #input  datetime


loc_dt.astimezone(pytz.utc) #converting into utc

print(loc_dt.astimezone(pytz.utc))