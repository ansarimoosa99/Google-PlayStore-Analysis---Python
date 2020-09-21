import pandas as pd
import math

def max_avgrating():
    data=pd.read_excel("App-data.xlsx")
    categories=set()
    for category in data["Category"]:
        categories.add(category)
    #print(categories)
    ratings=data["Rating"]
    cat=data["Category"]
    pd.options.mode.chained_assignment=None
    for i in range(len(ratings)):
        if math.isnan(ratings[i]):
            ratings[i]=0.0
    #print(ratings)
    summ=c=0
    avg={}
    for i in categories:
        for j in range(len(data["Category"])):
            if i== cat[j]:
                summ+=ratings[j]
                c+=1
        #print(summ,c)
        avg.update({i:(summ/c)})
        c=0
        summ=0
    print(avg)
    maximum=max(avg,key=avg.get)
    strr=[]
    strr.append("Highest maximum average ratings is {} and corresponding category is {}".format(avg[maximum],maximum))
    return strr
#max_avgrating()