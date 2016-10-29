import re

import pandas as pd

data_dir = "tweet\ crawler/"

df = pd.read_csv(data_dir+'tweets_crawler_dataset.csv')

s = df['id']

s1 = s.value_counts().index

re.MULTILINE = True
regex = re.compile('[^0-9]')

s11 = []

for x in s1:
	res = regex.search(x)
	if res == None:
		s11.append(x)

s2 = pd.Series(s11)

df.to_csv(data_dir+'filtered_dataset.csv', mode='a', index=False)