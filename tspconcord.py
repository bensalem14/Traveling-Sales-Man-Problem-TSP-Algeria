from __future__ import division, print_function


import pandas as pd
import folium
from concorde.tsp import TSPSolver

#get cities coordinantes
cities = pd.read_csv(
    "Cities.csv"
)


# Instantiate solver who uses the concorde algorithm
solver = TSPSolver.from_data(cities.Latitude, cities.Longitude, norm="GEO")

# Find tour
tour_data = solver.solve()
assert tour_data.success

solution = cities.iloc[tour_data.tour]
print("Optimal tour:")

print(
    " -> ".join("{r.City}".format(r=row) for _, row in solution.iterrows())
)
path=["{r.City}".format(r=row) for _, row in solution.iterrows()]


# Create a Folium map centered around the Algeria
map = folium.Map(location=[28.26369960393583, 2.532736476742567], zoom_start=5)

# Create a dictionary for coordinates
coordinates = {}
for _, row in cities.iterrows():
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
map.save("concorde_map.html")