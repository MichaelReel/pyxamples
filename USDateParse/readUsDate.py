from datetime import datetime

outputFormat = "%Y-%m-%d"

acceptedUSDateFormats = [
        "%Y-%m-%d", 
		"%Y %m %d", 
		"%Y/%m/%d", 
		"%m-%d-%Y", 
		"%m %d %Y", 
		"%m/%d/%Y",
		"%m-%d-%y", 
		"%m %d %y", 
		"%m/%d/%y", 
	]

def getISODate(usDate):
    """Return a date in the format y-m-d when given in a random US style date format"""
    d = None
    for format in acceptedUSDateFormats:
        try:
            d = datetime.strptime(usDate, format)
        except ValueError:
            d = None
        if d != None:
            return d.strftime(outputFormat)
    return None

print getISODate("2/13/15")
print getISODate("1-31-10")
print getISODate("5 10 2015")
print getISODate("2012 3 17")
print getISODate("2001-01-01")
print getISODate("2008/01/07")