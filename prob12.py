import pandas as pd

def sentiments():
    data=pd.read_excel('user_reviews.xlsx')

    sentiment=data["Sentiment"].tolist()
    Apps=data["App"].tolist()
    apps=set()
    for app in Apps:
        apps.add(app)
    track1={}
    track2={}
    strr=[]
    for i in apps:
        start_index= Apps.index(i)
        length=Apps.count(i)
        track1.update({i:sentiment[start_index:start_index+length].count('Positive')})
        track2.update({i:sentiment[start_index:start_index+length].count('Negative')})
        #print(track1)
        max1=max(track1,key=track1.get)
        max2=max(track2,key=track2.get)
    strr.append("Most Positive sentiment is {} and corresponding App is {}".format(track1[max1],max1))
    strr.append("Most Negative sentiment is {} and corresponding App is {}".format(track2[max2],max2))
    return strr

