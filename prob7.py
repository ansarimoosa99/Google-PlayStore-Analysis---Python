import pandas as pd
import numpy as np

def prob7():
     string=[]
     data=pd.read_excel('App-data.xlsx')
     installs = data["Installs"].tolist() 
     #pd.options.mode.chained_assignment=None
     for i in range(len(installs)):
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
            installs[i]=5.0
            continue
        if installs[i]=="1,000,000+":
            installs[i]=10.0
            continue
        if installs[i]=="5,000,000+":
            installs[i]=50.0
            continue
        if installs[i]=="50,000,000+":
            installs[i]=500.0
            continue
        if installs[i]=="10,000,000+":
            installs[i]=100.0
            continue
        else:
            installs[i]=0.0
            
     ser1=pd.Series(installs)
     data["installs"]=ser1   
     del data["Installs"]  
            
     av=data.groupby("Android Ver")
     varyd=av.get_group("Varies with device")
     a=varyd["installs"].agg(np.sum)
     
     all_sum=av["installs"].agg(np.sum).to_dict()
     b=sum(all_sum.values())-a
     sol=(a-b)*100/a
     if sol<0:
         string.append("There is a percentage decrease of {}".format(abs(sol)))
     else:
         string.append("There is a percentage increase of {}".format(abs(sol)))
     return string
     #print(av.groups)
#prob7()

