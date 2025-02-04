import requests
from model.ml_model import predict_score


def get_routes(start, end):    
    print('\n\n')
    url = f"https://router.project-osrm.org/route/v1/car/{start[0]},{start[1]};{end[0]},{end[1]}?alternatives=true&overview=full&geometries=geojson"
    
    response = requests.get(url)
    data = response.json()

    if "routes" in data:
        routes = data["routes"][:3]  # Get up to 3 routes

    # Store each route separately
        route_1 = routes[0]["geometry"]["coordinates"] if len(routes) > 0 else None
        route_2 = routes[1]["geometry"]["coordinates"] if len(routes) > 1 else None
        route_3 = routes[2]["geometry"]["coordinates"] if len(routes) > 2 else None
    
    return route_1, route_2, route_3

def avg_safety_score(route):

    score = 0

    for lon, lat in route:
        score = score+predict_score(lon, lat)
    
    return score

def safest_route(r1, r2, r3):
    
    r1s= avg_safety_score(r1)
    r2s= avg_safety_score(r2)
    r3s= avg_safety_score(r3)

    safest = min(r1s, r2s, r3s)

    if safest==r1s:
        return r1
    
    elif safest==r2s:
        return r2
    
    else:
        return r3




