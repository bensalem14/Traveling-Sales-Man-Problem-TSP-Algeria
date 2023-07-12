import pandas as pd
from geopy.distance import geodesic
import folium

#simple distance calculation based on coordinantes
def distance_between(df,city1, city2):
    """distance between two cities"""
    row1,row2 = df[df.City==city1].iloc[0],df[df.City==city2].iloc[0]
    lat1, lon1 = row1.Latitude, row1.Longitude
    lat2, lon2 = row2.Latitude, row2.Longitude
    distance =  geodesic((lat1,lon1), (lat2,lon2)).kilometers
    return distance


#distance matrix generator based on distances
def get_distance_matrix(df,cities):
    """populate distance matrix"""
    num_cities = len(cities)
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = distance_between(df,cities[i], cities[j])
            distances[i][j] = int(dist)
            distances[j][i] = int(dist)
    return distances

#function to solve the tsp based on the nearest neighbor algorithm
def solve_tsp_nearest(distances):
    num_cities = len(distances)
    visited = [False] * num_cities
    tour = []
    total_distance = 0
    
    # Start at the first city
    current_city = 0
    tour.append(current_city)
    visited[current_city] = True
    
    
    # Repeat until all cities have been visited
    while len(tour) < num_cities:
        nearest_city = None
        nearest_distance = float('inf')

        # Find the nearest unvisited city
        for city in range(num_cities):
            if not visited[city]:
                distance = distances[current_city][city]
                if distance < nearest_distance:
                    nearest_city = city
                    nearest_distance = distance

        # Move to the nearest city
        current_city = nearest_city
        tour.append(current_city)
        visited[current_city] = True
        total_distance += nearest_distance

    # Complete the tour by returning to the starting city
    tour.append(0)
    total_distance += distances[current_city][0]

    return tour, total_distance



# Read the CSV file and load the df into a pandas dfFrame
df = pd.read_csv('Cities.csv')

# Create a list of all cities
cities = list(set(df['City']) )
# Create a distance matrix
distances = get_distance_matrix(df,cities)

# Specify the start city and the number of nearest neighbors to consider

tour, total_distance = solve_tsp_nearest(distances)
path = [cities[i] for i in tour]
print("Tour:", path)
print("Total distance:", total_distance)


#____________________________________________________________________________________________
# Create a Folium map centered around the Algeria
map = folium.Map(location=[28.26369960393583, 2.532736476742567], zoom_start=5)
df1 = df
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
map.save("NN_map.html")
