# coding=utf-8
import csv
import json
from urllib import parse,request
import re

filename_read = './2017.csv'
filename_write = './results3.txt'
with open(filename_read) as f:
    reader = csv.reader(f)
    x = 0
    write_da = []
    for row in reader:
        url_value = {'keyword':row[0]}
        row_city = re.findall(r'[（](.*?)[）]', row[3])
	#a = ['（',row_city[0],'）']
        #row_city = ''.join(a)
        #print(row_city)
        city = row[3].replace('（' + row_city[0] + '）','')
        url_value1 = {'city': city}
        url_value = parse.urlencode(url_value)
        url_value1 = parse.urlencode(url_value1)
        url='https://restapi.amap.com/v3/place/text?key=9f9586f7ece479799be36af4f2aa733c&%s&types=&%s&children=1&offset=1&page=1&extensions=all' % (url_value,url_value1)
        #print(url)
        data = request.urlopen(url).read()
        data_a = data.decode('UTF-8')
        address = re.findall(r'"address"\:"(.*?)"',data_a)
        pname = re.findall(r'"pname"\:"(.*?)"',data_a)
        cityname = re.findall(r'"cityname"\:"(.*?)"',data_a)
        adname = re.findall(r'"adname"\:"(.*?)"',data_a)
        location = re.findall(r'"location"\:"(.*?)"',data_a)
        tel = re.findall(r'"tel"\:"(.*?)"',data_a)
        #data_a = json.loads(data)
        print(pname[0])
        print(cityname[0])
        print(adname[0])
        print(address[0])
        print(location[0])
        
        #data_a = data_a['pois']
        write_da.append(data_a)
        with open(filename_write,'a') as fw:
            try:
                wr = [row[0],',',row[1],',',row[2],',',row[3],',',pname[0],',',pname[0]+cityname[0]+adname[0]+address[0],',',tel[0],',',row[7],',',location[0],'\n']
                wr1 = ''.join(wr)
                print(wr1)
            except:
                wr = [row[0],',',row[1],',',row[2],',',row[3],',',pname,',',pname+cityname+adname+address,',',tel,',',row,',',location,'\n']
                print("Error:该医院信息未搜索到")
                continue
            else:
                fw.write(wr1)
