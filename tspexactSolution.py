
import pandas as pd
#this solution is too costly 
#the paths generation is done through backtracking since the graph is incomplete
# but the solution remains infeasable
#might become feasable using parallelization with first city option being devided across threads
def generate_permutations(cities, adjacency_list):
    def backtrack(current_permutation, remaining_cities):
        if not remaining_cities:
            yield current_permutation
            return
        
        last_city = current_permutation[-1] if current_permutation else None
        
        for city in remaining_cities:
            if last_city is None or (last_city, city) in adjacency_list or (city, last_city) in adjacency_list:
                new_permutation = current_permutation + [city]
                new_remaining_cities = remaining_cities.copy()
                new_remaining_cities.remove(city)
                yield from backtrack(new_permutation, new_remaining_cities)
    
    yield from backtrack([], set(cities))
# Read the CSV file
df = pd.read_csv('AlgeriaCities.csv')

# Extract city, distance, and road information
cities = list(set([*df['City'],*df['Adjacent province']]))
roads = [(x['City'],x['Adjacent province'],{"weight": x['Distance'],"color":"blue","label":x['Route']}) for _, x in df.iterrows()]
adjacency_list=[(x['City'],x['Adjacent province']) for _, x in df.iterrows()]
perms=list(generate_permutations(cities, adjacency_list))
print("__________________header")
print(df.head(1))
print("__________________cities")
print(cities,len(cities))
print("__________________roads")
print(roads)
print("__________________paths")
print(perms)

