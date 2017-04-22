# music-recommendation

Collabarative Filtering Approach to music recommendations system 
based on Shuiguang Deng,Dongjing Wang,Xitong Li ,Guandong Xu, [Exploring user emotion in microblogs for music recommendation](http://www.sciencedirect.com/science/article/pii/S0957417415005746)

# Steps to create a working model

- Go to `data retrieval and preprocessing directory`
- Create credentials for twitter api online and save the credentials in `credentials/twitter.json`
- Create folder named `tweet crawler`
- Run `tweets_crawler.py` : output will be `tweet crawler\tweets_crawler_dataset.csv`
- Copy the emotional lexicon dataset downloaded to current folder. Rename file as `emotion_lexicon.txt`
- Run `emlexcreator.py`
- Output will be `emotion_lex.csv`
- create `name_list` which is list of user names.
- create `music_list` which is list of music names
- run `dataset_creator.py` : output `user_emotion_music.csv`
- go back to main directory
- copy `emotion_lex.csv` and `user_emotion_music.csv` to this directory
- run main.py : output `user_music_interest.csv`