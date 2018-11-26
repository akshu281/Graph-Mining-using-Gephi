import csv
import pandas as pd
#extracting the route information
with open('Bus_Data.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

route_stops={}
"""creating identifier for route data"""
for inp in data[1:]:
    route=inp[0]+"_"+inp[1]
    try:
        route_stops[route].append(inp[2])
    except KeyError as K:
        route_stops[route]=[inp[2]]
print(route_stops)
"""appending each edge to list along with the weight"""
edges=[]
for key,value in route_stops.items():
    for index in range(0,len(value)-2):
        edges.append(value[index]+"_"+value[index+1])

# print(len(set(edges)))
"""fetching only unique edges"""
edges_set=list(set(edges))
# print(edges[:10])
edges_list=[edge.split("_") for edge in edges]
# print(len(edges_list))
print(edges_list[1])
#storing the csv files"""
pd.DataFrame(edges_list).to_csv("edge_list_individual.csv",index=False,header=False)
# with open('edge_list.csv', 'w', newline='') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerows(edges_list)
