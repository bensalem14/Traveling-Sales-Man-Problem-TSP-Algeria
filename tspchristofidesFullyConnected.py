import networkx as nx
import pandas as pd
import folium
from geopy.distance import geodesic
def distance_between(df,city1, city2):
    """distance between two cities"""
    row1,row2 = df[df.City==city1].iloc[0],df[df.City==city2].iloc[0]
    lat1, lon1 = row1.Latitude, row1.Longitude
    lat2, lon2 = row2.Latitude, row2.Longitude
    distance =  geodesic((lat1,lon1), (lat2,lon2)).kilometers
    return distance
# Read the CSV file
df = pd.read_csv('AlgeriaCities.csv')
df1 = pd.read_csv('Cities.csv')
print(df.columns)

# Extract city, distance, and road information
cities = list(set([*df['City'],*df['Adjacent province']]))
roads = [(i,j,{"weight": distance_between(df1,i,j),"color":"blue"}) for i in cities for j in cities if i!=j]




G = nx.Graph()
G.add_nodes_from(cities)
G.add_edges_from(roads)  
  
#uses the christofides algorithm
tsp = nx.approximation.traveling_salesman_problem

path = tsp(G, cycle=False)
cost=0
#the cost is calculated based on the road distances provided in the AlgeriaCities.csv
for i in range(len(path) - 1):
    current_city = path[i]
    next_city = path[i + 1]

    # Find the row in the DataFrame with the current city and the adjacent city
    cost += distance_between(df1,current_city,next_city)

print(path)
print("length of path")
print(len(path))
print("_____________Cost ")
print(str(cost)+"km")
#____________________________________________________________________________________________
# Create a Folium map centered around the Algeria
map = folium.Map(location=[28.26369960393583, 2.532736476742567], zoom_start=5)

# Create a dictionary for coordinates
coordinates = {}
for _, row in df1.iterrows():
    city = row['City']
    latitude = row['Latitude']
    longitude = row['Longitude']
    coordinates[city] = (latitude, longitude)
# Draw nodes and edges
for i in range(len(path) - 1):
    node1= path[i]
    node2= path[i+1]
    coord1 = coordinates[node1]
    coord2 = coordinates[node2]
 # Create a Folium PolyLine to represent the edge
    line = folium.PolyLine([coord1, coord2], color='blue', weight=1, opacity=0.7)
    map.add_child(line)

# Draw markers for nodes
for node, coord in coordinates.items():
    marker = folium.CircleMarker(coord, radius=5, color='red', fill=True, fill_color='red', fill_opacity=1)
    map.add_child(marker)

# Save the map as an HTML file
map.save("christofidesFullyConnected_map.html")

