import pandas as pd
import numpy as np
import math
from ast import literal_eval

class UserSimilarity:

	def __init__(self,user):
		self.user = user

	def cosine_similarity(self,vec1,vec2):
		numerator = np.sum(np.multiply(vec1,vec2))
		denominator = math.sqrt(np.sum(np.multiply(vec1,vec1))) * math.sqrt(np.sum(np.multiply(vec2,vec2)))
		return numerator/denominator

	def get_similarity(self):
		df = pd.read_csv('req_data/user_emotion_music.csv')

		user = self.user
		temp_users = pd.unique(df['user'])
		users = []

		for x in temp_users:
			# if x != user:
			users.append(x)

		df_user = df[df['user'] == user]
		unique_music = len(pd.unique(df_user['music']))

		df_res = pd.DataFrame([],columns=['user','similarity'])

		for x in users:
			df_comp = df[df['user'] == x]
			df_comp = df_comp[df_comp['music'].isin(df_user['music'])]
			# print df_comp.head()
			# df_comp = df[]
			unique_music_comp = len(pd.unique(df_comp['music']))
			cos_sim = 0
			# print df_comp
			for index,y in df_comp.iterrows():
				music_piece = y['music']
				df_temp = df_user[df_user['music'] == music_piece]
				
				user_tuple = literal_eval(df_temp.iloc[0]['emotion'])
				opp_tuple = literal_eval(y['emotion'])

				cos_sim = cos_sim + self.cosine_similarity(user_tuple,opp_tuple)
			cos_sim = cos_sim / (math.sqrt(unique_music*unique_music_comp))

			df_res=df_res.append(pd.DataFrame([[x, cos_sim]], columns=['user','similarity']))

		return df_res