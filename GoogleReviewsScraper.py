import requests
from bs4 import BeautifulSoup
import urllib.parse


#Input Name of Establishment and City
#Outputs PlaceId
def get_placeid(Name, City):
    api = 'https://maps.googleapis.com/maps/api/geocode/json?'
    url = api + urllib.parse.urlencode({'address': Name}) + City + '&key=[GOOGLE_API_KEY]'
    jsondata1 = requests.get(url).json()
    placeid = jsondata1['results'][0]['place_id']
    return placeid
#Input PlaceId
#Outputs the 5 Most Recent Reviews
def get_reviews(place_id):
    Main_Api = 'https://maps.googleapis.com/maps/api/place/details/json?placeid={}&key=[GOOGLE_API_KEY]'.format(place_id)
    jsondata = requests.get(Main_Api).json()
    return jsondata

if __name__ == "__main__":
    
    #PlaceHolder for any Business Name and City
    Name = 'Baja Fish Tacos'
    City = 'Laguna Niguel'
   
    placeid = get_placeid(Name, City)
    
    print(placeid)
    print()
    print()

    #placeid is used to get json from that exact business
    jsondata = get_reviews(placeid)
    
   
   
    #Outputs Operational Hours
    Hours =jsondata['result']['opening_hours']['weekday_text']
    print(Hours)
    print()

    #Outputs Reviews and Rating
    for i in range(5):
        Reviews = jsondata['result']['reviews'][i]['text']
        Rating = jsondata['result']['reviews'][i]['rating']
        print(Reviews)
        print('Rating: '+ str(Rating))
        print()

