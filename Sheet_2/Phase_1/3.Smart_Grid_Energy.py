import json

def main():
    reading = json.loads(input("Enter data: "))

    average_reading = list(
        map(
            lambda day: sum(valid)/len(valid) if (valid := [x for x in day if x is not None]) else 0.0,
            reading
        )
    )
    print(average_reading)
    
    

main()