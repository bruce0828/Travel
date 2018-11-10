import glob
import time
import os

from math import radians, cos, sin, asin, sqrt
from operator import itemgetter

#�����뷨�ǣ�dataframe��list��������dict������
#��bus��gps�ֱ𹹽�dictionary,plate��lineΪkeys������Ϊvalue����ʵֻ��plate�����ˣ�

bus_data_dict=dict()
with open("20151101bus.txt", 'r') as f:
    for lines in f:
        [card_id, time, line_no, plate_no] = lines.strip().split(',')    
        [H,M,S]=time.split(':')
        time_numeric=int(H)*3600+int(M)*60+int(S)#ʱ�䴦����룬�������Ƚ�
        if bus_data_dict.has_key((line_no,plate_no)):  
            bus_data_dict[line_no,plate_no].append([card_id, time, time_numeric])
        else:
            bus_data_dict[line_no,plate_no] = [[card_id, time, time_numeric]]

print len(bus_data_dict)


for key in bus_data_dict.keys():
    this_bus_line_no=key[0]
    this_bus_plate_no=key[1]            
    
    with open("bus_data\\"+this_bus_line_no+"_"+this_bus_plate_no, 'w') as wf:#������·�ͳ��Ʒֱ�д���ļ�����ʵû��Ҫ��ֱ��ѭ��dict�ͺ���
        for entry_no in range(0,len(bus_data_dict[key])):
             wf.write(str(bus_data_dict[key][entry_no][0]) + "," + str(bus_data_dict[key][entry_no][1]) + "," + str(bus_data_dict[key][entry_no][2])+ "\n")
                                


gps_data_dict=dict()
with open("20151101gps.txt", 'r') as f:
    for lines in f:
        [plate_no, line_no, lon, lat, time] = lines.strip().split(',')    
        [H,M,S]=time.split(':')
        time_numeric=int(H)*3600+int(M)*60+int(S)
        if gps_data_dict.has_key((line_no,plate_no)):  # not the first record
            gps_data_dict[line_no,plate_no].append([lon, lat, time, time_numeric])
        else:
            gps_data_dict[line_no,plate_no] = [[lon, lat, time, time_numeric]]
print len(gps_data_dict)    

for key in gps_data_dict.keys():
    this_gps_line_no=key[0]
    this_gps_plate_no=key[1]            
    
    with open("gps_data\\"+this_gps_line_no+"_"+this_gps_plate_no, 'w') as wf:
        for entry_no in range(0,len(gps_data_dict[key])):
             wf.write(str(gps_data_dict[key][entry_no][0]) + "," + str(gps_data_dict[key][entry_no][1]) + "," + str(gps_data_dict[key][entry_no][2])+ "," + str(gps_data_dict[key][entry_no][3]) + "\n")


#�����˼·Ӧ���ǣ������ֵ�ÿ������ѭ����Ȼ��ÿ��������ͬ��bus��gps��¼��ƥ��
#bus��gps��ʱ������bus�ĵ�һ���ҵ�ʱ�����ӽ���gps�󷵻��кţ�Ȼ��bus�ڶ��������к�������

#����˵�����ֵ���������ͬid��bus����gps��¼��������  bus�����ǡ�ʱ�䣬0,0��gps�ǡ�ʱ�䣬���ȣ�γ�ȡ� ����ܿ�
#numpy������where ֻҪ�ҳ��ڶ�����0��bus��¼���Ƚ�����������һ��ʱ����ӽ����Ѿ�γ�ȸ���busд��������
#ʱ��ת��Ϊ�����ȽϿ��ܸ���
