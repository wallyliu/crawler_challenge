import pandas as pd

# fetch raw data from bank of taiwan
raw_data = pd.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')
data = raw_data[0]

# extract useful first five column and do data preprocessing
currency = currency.ix[:,0:5]
currency.columns  = [u'幣別',u'現金匯率 本行買入',u'現金匯率 本行賣出',u'即期匯率 本行買入', u'即期匯率 本行賣出']
currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)', expand=True)

# save as a EXCEL file
currency.to_excel('currency.xlsx')
