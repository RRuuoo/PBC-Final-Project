# -*- coding: utf-8 -*-
import webbrowser
import requests
import re
import googlemaps 
gmaps = googlemaps.Client(key = '你的金鑰')
geocode_result = gmaps.geocode("臺南市")
city_loc = geocode_result[0]['geometry']['location']


'''使用者輸入資料'''
numbers = int(input())   # 輸入要去幾個地方
target_loc = []
for i in range(numbers):
    tmp = input()
    target_loc. append(tmp)  #輸入要去的地點的名稱


        
'''取得台南市半徑30公里內，關鍵字包含之所有地點的「店名」&「id」 (台南市寬度約77.6公里)'''
search_place = input()
result = gmaps.places_autocomplete(search_place, session_token = '*', location = city_loc, radius = 30000, strict_bounds = True)
candidate_ids = []
for i in range(len(result)):
    name = result[i]['structured_formatting']['main_text']
    shopId = result[i]['place_id']
    candidate_ids.append({'name': name, 'id':shopId})
#print(candidate_ids)




'''利用id取得目標地點資料: 店id、店名、完整地址、街名、電話、開放時間'''

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
    
#for i in information.keys():
#    print(i)
#    for j in information[i].keys():
#        print(j, ':', information[i][j])
#    print()

    

        
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
    
    
