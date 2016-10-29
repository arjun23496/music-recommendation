import pandas as pd
import numpy as np
import math

from ast import literal_eval
from UserSimilarity import UserSimilarity
from EmotionAnalyser import EmotionAnalyser

def cosine_similarity(vec1,vec2):
	numerator = np.sum(np.multiply(vec1,vec2))
	denominator = math.sqrt(np.sum(np.multiply(vec1,vec1))) * math.sqrt(np.sum(np.multiply(vec2,vec2)))
	return numerator/denominator

user = "Sebastian"
emotion_analyser = EmotionAnalyser("I should be sleep, but im not! thinking about an old friend who I want. but he's married now. damn, &amp; he wants me 2! scandalous!")
emotion = emotion_analyser.get_emotion_vector()
number_top_user = 10

# user_similarity = UserSimilarity(user)
# df = user_similarity.get_similarity()

df = pd.read_csv("computed_data.csv")
df_user_emotion = pd.read_csv('req_data/user_emotion_music.csv')

df = df.sort_values("similarity", ascending=False)
df = df.iloc[0:number_top_user]

df_user_emotion = df_user_emotion[df_user_emotion['user'].isin(df['user'])]

music_list = pd.unique(df_user_emotion['music'])

#probability of music listening

df_recommendations = pd.DataFrame([], columns=['music','interest'])

for x in music_list:
	df_temp = df_user_emotion[df_user_emotion['music'] == x]
	res_prob = 0
	for index,y in df_temp.iterrows():
		user_sim = df[df['user'] == y['user']].iloc[0]['similarity']
		emotional_cosine_sim = cosine_similarity(literal_eval(y['emotion']), emotion)
		res_prob =res_prob + ( user_sim * emotional_cosine_sim )
	df_recommendations = df_recommendations.append(pd.DataFrame([[x, res_prob]], columns=['music','interest']))

df_recommendations = df_recommendations.sort_values('interest', ascending=False)

print df_recommendations
# df_recommendations.to_csv('user_music_interest.csv')