import pandas as pd
def average():
    data=pd.read_excel("App-data.xlsx")
    categories=set()
    for category in data["Category"]:
        categories.add(category)   #CREATINNG A SET OF CATEGORIES
    print("The Categories are as follows", categories)
    print("Number of categories =",len(categories))
    installs = data["Installs"]   #DATAFRAME OF INTALLS
    cat=data["Category"]  #DATAFRAME OF ALL CATEGORY WITH REPITITION AS WELL
    
    pd.options.mode.chained_assignment=None     # TO HANDLE THE EXCEPPTION RAISED IN  PANDAS WHILE USING DATAFRAMES
    for i in range(0,10841):
        if installs[i]=="1,000+":
            installs[i]=0.01
            continue
        if installs[i]=="5,000+":
            installs[i]=0.05
            continue
        if installs[i]=="10,000+":
            installs[i]=0.1
            continue
        if installs[i]=="50,000+":
            installs[i]=0.5
            continue
        if installs[i]=="100,000+":
            installs[i]=1.0
            continue
        if installs[i]=="500,000+":
            installs[i]=5
            continue
        if installs[i]=="1,000,000+":
            installs[i]=10
            continue
        if installs[i]=="5,000,000+":
            installs[i]=50
            continue
        if installs[i]=="50,000,000+":
            installs[i]=500
            continue
        if installs[i]=="10,000,000+":
            installs[i]=100
            continue
        else:
            installs[i]=0.0
    print(installs)
    print(sum(installs))
    gre={}
    avg={}
    c=summ=0
    for i in categories:
        for j in range(len(data["Category"])):
            if i==cat[j]:
                summ+=installs[j]
                c+=1
        #print("Downloads of {} is {}".format(i,summ))
        gre.update({i:summ})   #gre is dictionary key value pair
        avg.update({i:(summ/c)})
        summ=0
        c=0
    #print(gre)
    strr=[]
    maxx=max(gre,key=gre.get)
    minn=min(gre,key=gre.get)
    strr.append("Category with most downloads is {}".format(maxx))
    strr.append("Category with least downloads is {}".format(minn))
    strr.append("Category with average of at least 2,50,000 downloads are: ")
    for j in avg.keys():  
        if (avg[j]*100000)>=250000:  #100000 to get back actual range of no ,avg[j] is actual category no
            strr.append(j)
    return strr

#average()