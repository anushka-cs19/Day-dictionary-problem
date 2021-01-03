import datetime

#gives day for given date
def get_day(y,m,d):
    
    date=str()
    date=d+" "+m+" "+y
    day_name= ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']
    #gives value of the day that starts as Mon=0, Tue=1 ...
    day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return(day_name[day])

    
#solution function(main)
def solution(D):

    day_name= ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']
    #declared an answer dictionary that contains values 0 by default
    ans={"Mon":0,"Tue":0,"Wed":0,"Thu":0,"Fri":0,"Sat":0,"Sun":0}
    
    #update the existing values from input dict to output dict
    for i in D:
        list1=list(map(str,i.split("-")))
        y=list1[0]
        m=list1[1]
        d=list1[2]
        a=get_day(y,m,d)
        ans[a]+=D[i]
    
    for i in range(1,6):
        if(ans[day_name[i]]==0):
            ans[day_name[i]]=(2*ans[day_name[i-1]])-ans[day_name[i-2]]
    
    print("{'Mon':"+str(ans["Mon"])+", "+"'Tue':"+str(ans["Tue"])+", "+"'Wed':"+str(ans["Wed"])+", "+"'Thu':"+str(ans["Thu"])+", "+"'Fri':"+str(ans["Fri"])+", "+"'Sat':"+str(ans["Sat"])+", "+"'Sun':"+str(ans["Sun"])+'}')

#D={'2020-01-01':4,'2020-01-02':4,'2020-01-03':6,'2020-01-04':8,'2020-01-05':2,'2020-01-06':-6,'2020-01-07':2,'2020-01-08':-2}
D={'2020-01-01':6,'2020-01-04':12,'2020-01-05':14,'2020-01-06':2,'2020-01-07':4}
solution(D)
