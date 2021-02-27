import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import csv

#got the text file open 
dataset = open('WhatsApp Chat with Bublasaur (1).txt','r',encoding=('utf-8')) 

#put it in the variable as list
chat = dataset.readlines()

'''sample element to break the text in 5 parts:
    1. date
    2. time
    3. am/pm
    4. sender
    5. msg
'''

finalList = list()

for i in range(100):
    sample = chat[i]
    value = re.findall(r'[0-9]+/[0-9]+/[0-9]+|[0-9]+:[0-9]+|AM|PM|- [a-zA-Z]+|: [a-zA-Z0-9 ,.?!#@*]*', sample)
    finalList.append(value)

with open('Chat.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['Date','Time', 'AM/PM', 'Sender', 'Message'])
    writer.writerows(finalList)

 




