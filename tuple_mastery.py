input = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

def format(input):
    for item in input:
        print(f'Itinerary {input.index(item) + 1}: {item[0]} - From {item[1]} to {item[2]}')

format(input)