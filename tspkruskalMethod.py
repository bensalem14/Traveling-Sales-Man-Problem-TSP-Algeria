import networkx as nx
from geopy.distance import geodesic
import pandas as pd
import folium

# Read the CSV file
df = pd.read_csv('AlgeriaCities.csv')

print(df.columns)
# Extract city, distance, and road information
cities = list(set([*df['City'],*df['Adjacent province']]))
roads = [(x['City'],x['Adjacent province'],{"weight": x['Distance'],"color":"blue","label":x['Route']}) for _, x in df.iterrows()]




G = nx.Graph()
G.add_nodes_from(cities)
G.add_edges_from(roads)    
#we first extract the mst of the algerian graph then apply a preorder
#traversal or  dfs to make it connected
mst = nx.minimum_spanning_tree(G)


graph = nx.Graph()
graph.add_edges_from([x for x in list(mst.edges)])


# Perform a depth-first search (DFS) traversal to construct the tour
path = list(nx.dfs_preorder_nodes(graph))
print(path)

df1 = pd.read_csv('Cities.csv')
cost=0
#the cost is calculated based on the geometric distance between coordinants
for i in range(len(path) - 1):
    current_city = path[i]
    next_city = path[i + 1]
    print(current_city,i)
    # Find the row in the DataFrame with the current city and the adjacent city
    cord1=(df1[df1['City'] == current_city].Latitude.values[0],df1[df1['City'] == current_city].Longitude.values[0])
    cord2=(df1[df1['City'] == next_city].Latitude.values[0],df1[df1['City'] == next_city].Longitude.values[0])
    cost += geodesic(cord1, cord2).kilometers

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
map.save("kruskal_map.html")
