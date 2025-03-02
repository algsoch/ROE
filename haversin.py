import math
import heapq

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of Earth in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# List of city connections
connections = [
    ("New York", "London"), ("Tokyo", "Sydney"), ("Paris", "Berlin"), ("Dubai", "Mumbai"),
    ("San Francisco", "Tokyo"), ("Toronto", "New York"), ("Shanghai", "Singapore"), ("Los Angeles", "Mexico City"),
    ("Istanbul", "Athens"), ("Madrid", "Rome"), ("Bangkok", "Hong Kong"), ("Seoul", "Shanghai"),
    ("Chicago", "Toronto"), ("Cape Town", "Nairobi"), ("Melbourne", "Auckland"), ("Kuala Lumpur", "Jakarta"),
    ("Rio de Janeiro", "Buenos Aires"), ("Berlin", "Prague"), ("Lima", "Bogota"), ("Montreal", "Miami"),
    ("Santiago", "Lima"), ("Vancouver", "San Francisco"), ("Boston", "Dublin"), ("Oslo", "Helsinki"),
    ("Sydney", "Brisbane"), ("Singapore", "Bangkok"), ("Zurich", "Vienna"), ("Tokyo", "Seoul"),
    ("Dubai", "Tel Aviv"), ("Doha", "Istanbul"), ("Athens", "Cairo"), ("Lisbon", "Madrid"),
    ("Warsaw", "Budapest"), ("Houston", "Phoenix"), ("Dallas", "Atlanta"), ("Stockholm", "Copenhagen"),
    ("Hanoi", "Ho Chi Minh City"), ("Casablanca", "Algiers"), ("Abu Dhabi", "Riyadh"), ("Nairobi", "Accra"),
    ("Moscow", "Tbilisi"), ("Addis Ababa", "Lagos"), ("Tehran", "Karachi"), ("Lahore", "Islamabad"),
    ("Dhaka", "Colombo"), ("Kathmandu", "Delhi"), ("Ulaanbaatar", "Nur-Sultan"), ("Brussels", "Amsterdam"),
    ("Perth", "Jakarta"), ("Tashkent", "Bishkek"), ("London", "Paris"), ("Los Angeles", "San Francisco"),
    ("Hong Kong", "Seoul"), ("Chicago", "Boston"), ("Rome", "Vienna"), ("Miami", "Atlanta"),
    ("Cape Town", "Addis Ababa"), ("Jakarta", "Singapore"), ("Mexico City", "Bogota"), ("Montreal", "Toronto"),
    ("Dubai", "Doha"), ("New York", "Miami"), ("Tokyo", "Osaka"), ("Cairo", "Istanbul"), ("Berlin", "Warsaw"),
    ("Rio de Janeiro", "Lima"), ("Buenos Aires", "Santiago"), ("Melbourne", "Sydney"), ("Lisbon", "Dublin"),
    ("Helsinki", "Stockholm"), ("Ho Chi Minh City", "Bangkok"), ("Casablanca", "Nairobi"), ("Vienna", "Prague"),
    ("Dallas", "Houston"), ("Phoenix", "San Diego"), ("Vancouver", "Seattle"), ("Kuala Lumpur", "Manila"),
    ("Manila", "Taipei"), ("Taipei", "Hong Kong"), ("Nairobi", "Accra"), ("Accra", "Lagos"), ("Addis Ababa", "Luanda"),
    ("Luanda", "Cape Town"), ("Athens", "Rome"), ("Oslo", "Brussels"), ("Stockholm", "Helsinki"), ("Zurich", "Amsterdam"),
    ("Tel Aviv", "Istanbul"), ("Tehran", "Dubai"), ("Moscow", "Helsinki"), ("Doha", "Abu Dhabi"),
    ("Kuwait City", "Dubai"), ("Islamabad", "Delhi"), ("Colombo", "Mumbai"), ("Karachi", "Tehran"),
    ("Yerevan", "Tbilisi"), ("Tbilisi", "Baku"), ("Kigali", "Nairobi"), ("Muscat", "Dubai"),
    ("Jeddah", "Riyadh"), ("Brisbane", "Perth"), ("Barcelona", "Paris"), ("Caracas", "Bogota"),
    ("Sao Paulo", "Buenos Aires"), ("Nairobi", "Addis Ababa"), ("Accra", "Lagos"), ("Luanda", "Kinshasa"),
    ("Wellington", "Auckland"), ("Perth", "Wellington"), ("Kigali", "Nairobi"), ("Mumbai", "Delhi"),
    ("Lahore", "Karachi"), ("Nur-Sultan", "Almaty"), ("Tashkent", "Almaty"), ("Ulaanbaatar", "Beijing"),
    ("Beijing", "Shanghai"), ("Shanghai", "Hong Kong"), ("Hong Kong", "Tokyo"), ("Tokyo", "Seoul"),
    ("Seoul", "Beijing"), ("Dubai", "Singapore"), ("Istanbul", "Bangkok"), ("Cairo", "Dubai"),
    ("Istanbul", "Casablanca"), ("Mumbai", "Singapore"), ("Dubai", "Bangkok")
]

city_coords = {
    "Accra": (5.603716, -0.187), "Nairobi": (-1.286389, 36.817223), "Addis Ababa": (9.005401, 38.763611),
    "Zurich": (47.3769, 8.5417), "Vienna": (48.2082, 16.3738)
}

def dijkstra(start, end):
    graph = {city: [] for city in city_coords}
    for city1, city2 in connections:
        if city1 in city_coords and city2 in city_coords:
            distance = haversine(*city_coords[city1], *city_coords[city2])
            graph[city1].append((distance, city2))
            graph[city2].append((distance, city1))
    
    queue = [(0, start, [])]
    seen = set()
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in seen:
            continue
        path = path + [node]
        if node == end:
            return path
        seen.add(node)
        for distance, neighbor in graph[node]:
            heapq.heappush(queue, (cost + distance, neighbor, path))
    return []
print('vickyp.py')
print(','.join(dijkstra("Accra", "Vienna")))
