travel_logs = {
    "france" : ["paris","lille","dijon"],
    "germany" : ["stuttgart","berlin"]
}

print(travel_logs)
for key in travel_logs:
    print(travel_logs[key][1])


nested_list = ['a','b',['c','d']]
print(nested_list[2][1])

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])