#Goal: Create a program that will grab the IP address of the
#device in question, determine a longitude and latitude and
#then determine the weather for that area.
import config, urllib2, sys, socket, json, darksky
from urllib2 import urlopen
from datetime import date, timedelta
from darksky import forecast
dkey = config.darkSK


def main():
    #Test Internet connection
    connect = connection_valid()
    if connect == False:
        print "Program cannot determine weather with no connection..."
        print "Exiting..."
        sys.exit()

    print "Connection Successful!"
    print "Determining IP Address..."
    ipAddr = str(urlopen('http://ip.42.pl/raw').read())
    print "IP Address found: "+str(ipAddr)
    print "JSON dump of location based on IP:"
    jsonDump = urllib2.urlopen("https://freegeoip.net/json/"+ipAddr).read()
    jsonOrganized = json.loads(jsonDump)
    region = jsonOrganized['region_name']
    zipC = jsonOrganized['zip_code']
    city = jsonOrganized['city']
    lg = jsonOrganized['longitude']
    la = jsonOrganized['latitude']
    print "Longitude found: "+str(lg)
    print "Latitude found: "+str(la)
    print "Using data to find local weather..."
    jsonDarkSky = urllib2.urlopen("https://api.darksky.net/forecast/"+str(dkey)+"/"+str(la)+","+str(lg)).read()
    darkOrganized = json.loads(jsonDarkSky)
    currentTemp = darkOrganized['currently']['temperature']
    precipProb = darkOrganized['currently']['precipProbability']
    humidity = darkOrganized['currently']['humidity']
    ws = darkOrganized['currently']['windSpeed']
    summary = darkOrganized['currently']['summary']
    print "_______________________________________________________\n\n"
    print "The Current Temperature Near the Following Parameters:\n"
    print "Region: "+str(region)+"    |        Zipcode: "+str(zipC)
    print "City ------------------------------ "+str(city)
    print "Summary --------------------------- "+str(summary)
    print "Current Temperatre ---------------- "+str(currentTemp)+" F"
    print "Humidity -------------------------- "+str(humidity)
    print "Precipitation Probability --------- "+str(precipProb)+"%"
    print "Wind Speed ------------------------ "+str(ws)
    print "\n\n___________________________________________________"


def connection_valid():
    try:
        urllib2.urlopen('http://github.com',timeout=2)
        return True
    except urllib2.URLError as err:
        return False




if __name__ == "__main__": main()
