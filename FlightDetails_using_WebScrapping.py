fno=input("Enter the flight no. in the format (Code/Number/): ")
print("Enter the Date in the format (year/month/day/)")
dat=input("Also note that the input date can be only 2 days behind or ahead the present date): ")
import requests
from bs4 import BeautifulSoup

url="https://www.flightstats.com/v2/flight-tracker/"+fno+dat
r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
d=soup.find("div",{"class":"sc-TFwJa jJAJYo"})
fno=d.text

d=soup.find("div",{"class":"sc-TFwJa SUctH"})
fnam=d.text

d=soup.find("div",{"class":"sc-TFwJa hxcixc"})
DepPlace=d.text
d=soup.find("div",{"class":"sc-TFwJa jqWxQP"})
DepCode=d.text
d=soup.find("div",{"class":"sc-TFwJa icbxbp"})
DepDate=d.text
d=soup.find("div",{"class":"sc-TFwJa dKHRdN"})
DepTime=d.text

d=soup.find("div",{"class":"sc-bHwgHz kiZeQS"})
ArrPlace=d.contents[2].contents[0].contents[1].text
ArrCode=d.contents[2].contents[0].contents[0].text
ArrDate=d.contents[1].contents[1].contents[1].text
ArrTime=d.contents[1].contents[2].contents[0].contents[1].text


d=soup.find("div",{"class":"sc-ipZHIp bveXXR"})
stat=d.contents[0].text+". "+d.contents[1].text
d=soup.find("div",{"class":"sc-jKVCRD gNXHaj"})
Altitude=d.contents[1].text
d=soup.find("div",{"class":"sc-iSDuPN fmwYhF"})
tymrem=d.contents[1].contents[2].contents[1].text
d=soup.find("div",{"class":"sc-iSDuPN fqLCFv"})
equip=d.contents[1].contents[1].contents[1].text

print("Flight Details........................................")
print("Flight Number: ",fno)
print("Carrier Name: ",fnam)
print("Aircraft Type:",equip)
print("Departure Details.....................................")
print("Place: ",DepPlace)
print("Airport Code: ",DepCode)
print("Departure Date: ",DepDate)
print("Scheduled Departure Time: ",DepTime)
print("Arrival Details.....................................")
print("Place: ",ArrPlace)
print("Airport Code: ",ArrCode)
print("Arrival Date: ",ArrDate)
print("Scheduled Arrival Time: ",ArrTime)
print("Current Details.....................................")
print("Status: ",stat)
print("Altitude: ",Altitude)
print("Time remaining to reach the destination: ",tymrem)
