import pytz
from datetime import datetime
from pytz import timezone

eastern = timezone('Europe/Amsterdam') #database time
loc_dt = eastern.localize(datetime.now()) #input date time


loc_dt.astimezone(pytz.utc) #converting into utc

print(loc_dt.astimezone(pytz.utc))