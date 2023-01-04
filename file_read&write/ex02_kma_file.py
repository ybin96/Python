import requests
import re

f = open('./Data/kma.txt', 'w', encoding='utf-8')
url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
text = requests.get(url).text
# print(text)

location_list = re.findall(r'<location wl_ver="3">(.+?)<location>', text, re.DOTALL)
for location in location_list:
    city = re.findall(r'<city>(.+?)</city>', location)
    data_list = re.findall(r'<data>(.+?)</data>', location, re.DOTALL)

    for data in data_list:
        tmEf = re.findall(r'<tmEf>(.+?)</tmEf>', data)
        wf = re.findall(r'<wf>(.+?)</wf>', location)
        tmn = re.findall(r'<tmn>(.+?)</tmn>', location)
        tmx = re.findall(r'<tmx>(.+?)</tmx>', location)
        # print(city[0], tmEf[0], wf[0], tmn[0], tmx[0])
        row = "%s,%s,%s,%s,%s\n" % (city[0], tmEf[0], wf[0], tmn[0], tmx[0])
        f.write(row)
