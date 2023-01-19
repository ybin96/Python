import json
import pandas as pd

geo = json.load(open('../Data/SIG.geojson', encoding="UTF-8"))
df_pop = pd.read_csv("../Data/Population_SIG.csv")
print(df_pop.head())

print(df_pop.info())
#    code region      pop
# 0     11  서울특별시  9509458
# 1  11110    종로구   144683
# 2  11140     중구   122499
# 3  11170    용산구   222953
# 4  11200    성동구   285990

#데이터프레임의 code의 자료형을 str으로 변경합니다.
df_pop['code'] = df_pop['code'].astype(str)
print(df_pop.info())

#배경지도 만들기
import folium

# map = folium.Map(location=[37.5574, 126.9197], zoom_start=21)
# map.show_in_browser()   #지도를 브라우저에 출력합니다.

map_sig = folium.Map(location=[35.95, 127.7],
                     zoom_start=8,
                     tiles='cartodbpositron')

# folium.Choropleth(
#     geo_data=geo,
#     data=df_pop,
#     columns=('code','pop'),
#     key_on='feature.properties.SIG_CD').add_to(map_sig)

bins = list(df_pop['pop'].quantile([0,0.2,0.4,0.6,0.8,1]))

folium.Choropleth(
    geo_data=geo,
    data=df_pop,
    columns=('code','pop'),
    key_on='feature.properties.SIG_CD',
    bins =bins,
    fill_color="Blues",
    fill_opacity=1,
    line_opacity=0.5
).add_to(map_sig)

map_sig.show_in_browser()



