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
        print(row_city[0])
        print(row[3])
	#a = ['（',row_city[0],'）']
        #row_city = ''.join(a)
        #print(row_city)
        city = row[3].replace('（' + row_city[0] + '）','')
	
	
        url_value1 = {'city': city}
        url_value = parse.urlencode(url_value)
        url_value1 = parse.urlencode(url_value1)
        url='https://restapi.amap.com/v3/place/text?key=9f9586f7ece479799be36af4f2aa733c&%s&types=&%s&children=1&offset=1&page=1&extensions=all' % (url_value,url_value1)
        print(url)
        data = request.urlopen(url).read()
        data_a = data.decode('UTF-8')
        print(data_a)
        address = re.findall(r'"address"\:"(.*?)"',data_a)
        print(address[0])
        #data_a = json.loads(data)
        
        #data_a = data_a['pois']
        write_da.append(data_a)
        if x%100==0:
            with open(filename_write,'a') as fw:
                json.dump(data_a, fw)
                print("写入json文件，第%s 条" %(x) )
        x +=1
        if x < 0:
            print("此次更新 %s 条" %(x))
            break

