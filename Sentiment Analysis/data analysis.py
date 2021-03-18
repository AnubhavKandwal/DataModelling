#PHASE 2: Data cleaning phase - clean the known issues with the csv created
'''
The known issue with the csv are:
    1. '- ' symbol in the Sender column
    2. ': ' symbol in the message column
    3. Blank spaces in between each data entry - is it because of the \n ?? [Need investigation]
    4. Emoji usage is now blank text - ignore or add value?
    5. '<Media omitted>' messages to be handled properly - to be removed as data point ? [Reduces time series setup - replace as 'MediaSent'?]
'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Chat.csv', encoding=('utf-16'))
data.drop('Time', axis = 1, inplace = True)
data['Sender'] = data['Sender'].str.lstrip('- ')
data['Message'] = data['Message'].str.lstrip(': ')

consolidated_sender1 = data[data['Sender'] == '<s1>'].groupby('Date').count()
consolidated_sender2 = data[data['Sender'] == '<s2>'].groupby('Date').count()

plt.plot(consolidated_kakarot.index, consolidated_kakarot['Message'], color = '<c1>', label = '<l1>')
plt.plot(consolidated_bublasaur.index, consolidated_bublasaur['Message'], color = '<c2>', label = '<l2>')
plt.legend()