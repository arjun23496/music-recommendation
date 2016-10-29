import random
import pandas as pd

database_length = 5000
song_list = []
name_list = []
emotion_list = ['anger', 'anticipation', 'disgust', 
				'fear', 'joy', 'sadness', 'surprise', 'trust']
f = open("music_list")
song_list = f.readlines()
f.close()

f = open("name_list")
name_list = f.readlines()

ctr = 0
for x in song_list:
	x = x.replace("\xe2\x80\x93",":")
	x = x.replace("\xe2\x80\x9c","")
	x = x.replace("\xe2\x80\x9d\n","")
	if ctr <= 100:
		song_list[ctr] = x[5:] 
	else:
		song_list[ctr] = x[4:]
	ctr = ctr+1

ctr = 0
for x in name_list:
	name_list[ctr] = x.replace("\t\n","")
	ctr = ctr+1

print random.choice(name_list)

user = []
emotion = []
music = []

for x in range(0,database_length):
	user.append(random.choice(name_list))
	emotion.append(tuple( [random.randint(0,5), random.randint(0,5), random.randint(0,5),
							random.randint(0,5), random.randint(0,5), random.randint(0,5),
							random.randint(0,5), random.randint(0,5), random.randint(0,5), random.randint(0,5)] ))
	music.append(random.choice(song_list))

df = pd.DataFrame.from_items([("user",user),("emotion",emotion),("music",music)])

df.to_csv("user_emotion_music.csv")

print df.describe()
print df.head()