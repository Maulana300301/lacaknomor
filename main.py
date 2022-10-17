import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder

pepnumber phonenumbers.parse(number)
location geocoder.descriptionfor_number(pepnumber, 'en')
print (location)

from phonenumbers import carrier
service pro phonenumbers.parse(number)
print (carrier . name_for_number (service_pro, 'en '))

from opencage.geocoder import OpenCageGeocode

key "a9c5b28b233c43f8bd91a9030e67498d'

geocoder OpenCageGeo code (key)
query str(location)
results geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start= 9)
folium.Marker([lat, lng], popup=location ).add_to(myMap)
myMap.save("mylocation.html")