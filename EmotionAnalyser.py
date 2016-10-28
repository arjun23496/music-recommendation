class EmotionAnalyser:
	
	def __init__(self,text):
		self.text = text

	def get_emotion_vector(self):
		import pandas as pd
		import numpy as np
		import regex as re

		dataf = pd.read_csv("req_data/emotion_lex.csv")
		emotions = ['anger', 'anticipation', 'disgust', 'fear', 
					'joy', 'negative', 'positive', 'sadness', 'surprise', 'trust']

		regex = re.compile('[^a-zA-Z ]')		
		self.text = regex.sub('',self.text)		
		bag = self.text.split(" ")
		emotion_vector = [0,0,0,0,0,0,0,0,0,0]

		for x in bag:
			df_temp = pd.DataFrame([],columns = emotions)
			df_temp = df_temp.append(dataf[dataf['word'] == x])
			if df_temp['word'].count() > 0:
				vec = [0,0,0,0,0,0,0,0,0,0]
				ctr = 0 
				for emotion in emotions:
					vec[ctr] = df_temp.iloc[0][emotion]
					ctr = ctr+1
				emotion_vector = np.add(emotion_vector,vec)

		return tuple(emotion_vector.astype(int))