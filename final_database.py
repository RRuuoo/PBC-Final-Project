# -*- coding: utf-8 -*-
import webbrowser
import requests
import re
import googlemaps 
gmaps = googlemaps.Client(key = '你的金鑰')
geocode_result = gmaps.geocode("臺南市")
city_loc = geocode_result[0]['geometry']['location']


# places_to_go:  先前使用者輸入的所有想去地點
'''version1:  只抓出符合關鍵字的第一筆資料'''
def retrieve_place_ids(places_to_go):
    for i in range(len(places_to_go)):
        geocode_result = gmaps.geocode(places_to_go[i])
        place_id = geocode_result[0]['place_id']
        
        information = []
        detail_results = gmaps.place(place_id, language = "zh-tw")['result']
        name = detail_results['name']
        try:
            address = detail_results['formatted_address']
        except:
            address = 'None'    
        try:
            phone = detail_results['formatted_phone_number']
        except: 
            phone = 'None'
        try:
            opening_hours = detail_results['opening_hours']['weekday_text']
        except:
            opening_hours = 'None'
        information[place_id] = {'name': name, 'address': address, 'phone_number': phone, 'opening':opening}
        
    return information



'''version2:  抓出符合關鍵字的所有資料，再依據使用者輸入的街道名稱，篩選出最終的地名'''
def retrieve_place_ids(places_to_go):
    ids = []
    for i in range(len(places_to_go)):
        search_result = gmaps.places_places(places_to_go[i], session_token = '*', location = city_loc, radius = 30000, strict_bounds = True)
        for i in range(len(search_result)):
            placeName = result[i]['structured_formatting']['main_text']
            placeId = result[i]['place_id']
            ids.append({'place_name': placeName, 'place_id':placeId}
    return ids

def create_all_data(ids):
    information = dict()
    for i in range(len(ids)):
        place_id = ids[i]['id']
        place_detail = gmaps.place(place_id, language = 'zh-tw')['result']
        name = place_detail['name']
        try:
            street_name = place_detail['address_components'][1]['short_name']       
        except:
            street_name = 'None'
        try:
            address = place_detail['formatted_address']
        except:
            address = 'None'
        try:
            phone = place_detail['formatted_phone_number']
        except:
            phone = 'None'
        try:
            opening = shop_detail['opening_hours']['weekday_text']
        except:
            opening = 'None'
    information[place_id] = {'name': name, 'address': address, 'street_name': street_name, 'phone_number': phone, 'opening':opening}
    
    return information                   

    

        
                       
                       
                       
                       
                       
                       
                       
'''從google map爬出地點之間的距離&移動時間'''

address1= target_loc[0]
address2= target_loc[1]

#此行可以另外打開網頁確認google map
webbrowser.open('https://www.google.com.tw/maps/dir/' + address1 + '/' + address2)

#抓取網頁資料
res=requests.get('https://www.google.com.tw/maps/dir/' + address1 + '/' + address2)

print(res.text)

#尋找被\"包起來的字串
m =re.findall('\\\\\"([^"]+)\\\\\"', res.text)

#尋找想要的資訊
for i in range(len(m)):
    if  m[i]==address2 and m[i+3][-1]=='分' :
        print("路徑為: %s, 距離為: %s, 預估所需時間為: %s " %(m[i+1],m[i+2],m[i+3]))
        break
    
    
