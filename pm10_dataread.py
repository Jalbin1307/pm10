# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:12:05 2020

@author: USER
"""


from ast import literal_eval


f = open("test.txt",'r')
for i in range(1, 2):
    line = f.readline()
    print(line[-49:-30])
    a = literal_eval(line[13:-55])
   # print(a['raw'][0]['data']['PM2.5'])
  #  print(a['raw'][0]['data']['PM10'])
    #print(a['raw'][0]['data']['PM1.0'])
    
f.close()

"""






a = {"raw":[{"data":{"PM2.5":"4","PM10":"9","PM1.0":"3"},"id":"NIDS_DUST1"},{"data":{"TEMP":"29.62","CO2":"637.82","GAS":"877364.96","IAQ":"92.44","HUMI":"32.19","VOC":"0.84","PRESS":"1024.49"},"id":"G414_TVOC"}]}
print(a['raw'][0]['data']['PM2.5'])
print(a['raw'][0]['data']['PM10'])
print(a['raw'][0]['data']['PM1.0'])


"""