# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 07:18:30 2019

@author: Elaine
"""

import googlemaps 
gmaps = googlemaps.Client(key = '金鑰')
geocode_result = gmaps.geocode("臺南市")
city_loc = geocode_result[0]['geometry']['location']

        
'''取得台南市半徑30公里內，關鍵字包含之所有地點的「店名」&「id」 (台南市寬度約77.6公里)'''
search_place = input()
result = gmaps.places_autocomplete(search_place, session_token = '*', location = city_loc, radius = 30000, strict_bounds = True)
candidate_ids = []
for i in range(len(result)):
    name = result[i]['structured_formatting']['main_text']
    shopId = result[i]['place_id']
    candidate_ids.append({'name': name, 'id':shopId})
#print(candidate_ids)



'''利用id取得目標地點資料: 
   一、地址(formatted address)                二、 店家的經緯度(geometry location)
   三、周一~周日開放時間(opening hours)        四、電話(formatted phone number)
'''

information = dict()
for i in range(len(candidate_ids)):
    shopId = candidate_ids[i]['id']
    shop_detail = gmaps.place(shopId, language = 'zh-tw')['result']
    
    name = shop_detail['name']
    street_name = shop_detail['address_components'][1]['short_name']
    formal_address = shop_detail['formatted_address']
    phone = shop_detail['formatted_phone_number']
    location = shop_detail['geometry']['location']
    try:
        opening = shop_detail['opening_hours']
    except:
        opening = 'None'
    information[shopId] = {'name': name, 'address': formal_address, 'street_name': street_name, 'location': location,  'opening':opening, 'phone_number': phone}
    
    
for i in information.keys():
    print(i)
    for j in information[i].keys():
        print(j, ':', information[i][j])
    print()

    
    
    
    
    
    
    
    
