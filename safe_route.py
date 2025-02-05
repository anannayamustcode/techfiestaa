import requests
from model.ml_model import predict_score

#all coords in form of lon,lat

#ml model requires in form lat,lon

start = (-118.2436, 34.0522)
end = (-118.3215, 34.1330)  

def get_routes(start, end):    
    print('\n\n')
    url = f"https://router.project-osrm.org/route/v1/car/{start[0]},{start[1]};{end[0]},{end[1]}?alternatives=true&overview=full&geometries=geojson"
    
    response = requests.get(url)
    data = response.json()

    routes=[]

    if "routes" in data:
        route_data = data["routes"][:3]  # Get up to 3 routes

    # Store each route separately
        for route in route_data:
            route_coords = route["geometry"]["coordinates"]
            routes.append(route_coords)
    
    return routes

def avg_safety_score(route):

    score = 0

    for lon, lat in route:
        score = score+predict_score(lat, lon)
    
    return score

def safest_route(routes):
    
    safety_scores=[avg_safety_score(route) for route in routes]

    safest_index = safety_scores.index(min(safety_scores))

    alternative_routes = routes[:safest_index] + routes[safest_index+1:]

    return routes[safest_index], alternative_routes

def get_safest_route(start, end):

    try:    
        routes = get_routes(start, end)

        safe_route, alt_routes =safest_route(routes)

        l=[] #Extract coordinates
        for lon, lat in safe_route:
            l.append([lat,lon])
    
        return l
    except:
        return 0

def get_alt_routes(start, end):

    try:    
        routes=get_routes(start, end)

        safe_route, alt_routes = safest_route(routes)

        new_routes=[]
        for route in alt_routes:
            l=[]
            for lon, lat in route:
                l.append([lat,lon])
            new_routes.append(l)
        print(new_routes)
        return new_routes
    
    except:
        return 0




