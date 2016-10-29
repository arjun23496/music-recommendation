import pandas as pd
import sys

df = pd.read_csv("emotion_lexicon.txt",sep="\t")

df_new = pd.DataFrame([],columns=['word', 'anger', 'anticipation', 'disgust', 
								'fear', 'joy', 'negative', 'positive', 'sadness', 'surprise', 'trust'])

emotions = list(['anger', 'anticipation', 'disgust', 
								'fear', 'joy', 'negative', 'positive', 'sadness', 'surprise', 'trust'])

x=0
w=0
while x < df['word'].count():

	sys.stdout.write(" %d/14182 \r" % (w))
	sys.stdout.flush()
	
	temp_df = pd.DataFrame([[df.iloc[x]['word'],0,0,0,0,0,0,0,0,0,0]],columns=['word', 'anger', 'anticipation', 'disgust', 
							'fear', 'joy', 'negative', 'positive', 'sadness', 'surprise', 'trust'])
	temp_df = temp_df.set_value(0,'anger',df.iloc[x]['num'])
	x=x+1
	temp_df = temp_df.set_value(0,'anticipation',df.iloc[x]['num'])
	x=x+1
	temp_df = temp_df.set_value(0,'disgust',df.iloc[x]['num'])
	x=x+1
	temp_df = temp_df.set_value(0,'fear',df.iloc[x]['num'])
	x=x+1
	temp_df = temp_df.set_value(0,'joy',df.iloc[x]['num'])
	x=x+1
	temp_df = temp_df.set_value(0,'negative',df.iloc[x]['num'])
	x=x+1
	temp_df = temp_df.set_value(0,'positive',df.iloc[x]['num'])
	x=x+1
	temp_df = temp_df.set_value(0,'sadness',df.iloc[x]['num'])
	x=x+1
	temp_df = temp_df.set_value(0,'surprise',df.iloc[x]['num'])
	x=x+1
	temp_df = temp_df.set_value(0,'trust',df.iloc[x]['num'])
	x=x+1
	w=w+1
	df_new = df_new.append(temp_df)	

df_new[emotions] = df_new[emotions].astype(int)

df_new.to_csv("emotion_lex.csv")
print "complete"