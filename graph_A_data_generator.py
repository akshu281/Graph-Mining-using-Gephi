import pandas as pd

# reading the bus volume data set
df=pd.read_csv("origin_destination_bus_201809.csv")
print("Read data")
print(df.shape)
""" converting the data to list of dictionary"""
data=list(df.T.to_dict().values())
print("converted to dict")
edges_data_weekday=[]
edges_data_weekend=[]
def match_src_dst(element,d):
    # print(element)
    # print(d)
    """checking if the data is available already for aggregation"""
    if(element['source'] == d['ORIGIN_PT_CODE'] and element['target'] == d['DESTINATION_PT_CODE']):
        # print("updating")
        return True
    # print("new data")
    return False
count=0
for d in data:
    count+=1
    print(count)
    #aggregating separately for weekday and weekend
    if(d['DAY_TYPE']=='WEEKDAY'):
        elem=None
        try:
            for x in edges_data_weekday:
                if(match_src_dst(x,d)):
                    elem=x
                    break;
        except Exception as e:
            print(e)
            pass
        if(elem==None):
            edges_data_weekday.append({'source':d['ORIGIN_PT_CODE'],'target':d['DESTINATION_PT_CODE'],'weight':d['TOTAL_TRIPS']})
        else:
            elem['weight']=elem['weight']+d['TOTAL_TRIPS']
    if(d['DAY_TYPE']=='WEEKENDS/HOLIDAY'):
        elem=None
        try:
            for y in edges_data_weekend:
                if(match_src_dst(y,d)):
                    elem=x
                    break;
        except:
            pass
        if(elem==None):
            edges_data_weekend.append({'source':d['ORIGIN_PT_CODE'],'target':d['DESTINATION_PT_CODE'],'weight':d['TOTAL_TRIPS']})
        else:
            elem['weight']=elem['weight']+d['TOTAL_TRIPS']

"""storing the extracted data in csv files for futher processing"""
pd.DataFrame(edges_data_weekday).to_csv("stop_volume_weekday.csv",index=False,header=False)
pd.DataFrame(edges_data_weekend).to_csv("stop_volume_weekend.csv",index=False,header=False)
"""
