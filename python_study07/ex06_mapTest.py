import json
geo = json.load(open("../Data/SIG.geojson", encoding="UTF-8"))
# keyList = geo.keys()
# print(keyList)
# print(geo)
# print(type(geo))
# print(len(geo))
# print(geo)

# dict_keys(['type', 'name', 'crs', 'features'])
# t = geo['type']
# print(t)
# print(type(t))
# name = geo['name']
# print(name)
# print(type(name))
# crs = geo['crs']
# print(crs)
# print(type(crs))
features = geo['features']
# print(features)
# print(type(features))
# print(len(features))
# print("-"*50)
# print(features[0])
# print(type(features[0]))

keylist = features[0].keys()
print(keylist)
# dict_keys(['type', 'properties', 'geometry'])
print(features[0]["type"])

print(features[0]["properties"])
#{'SIG_CD': '42110', 'SIG_ENG_NM': 'Chuncheon-si', 'SIG_KOR_NM': '춘천시'}

print(features[0]["geometry"].keys())   #dict_keys(['type', 'coordinates'])
print(features[0]["geometry"]["coordinates"])       #4차원배열의 위도,경도 정보











