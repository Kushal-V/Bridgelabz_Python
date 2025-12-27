import json

def main():
    
    itinerary = json.loads(input("Enter the itinerary: "))

    arrival_time = [
        leg["segments"][-1]["arrival_time"]
        for leg in itinerary["legs"]
    ]
    print(arrival_time)

main()