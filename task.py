def find_lowest_cost_path(airports, start, end):
    lowest_cost = float("inf")
    lowest_cost_path = []

    def find_path(current_path, current_cost, lowest_cost, lowest_cost_path):
        # Get the last airport visited in the current path
        current_airport = current_path[-1]

        # If the current airport is the destination, update lowest_cost and lowest_cost_path if applicable
        if current_airport == end:
            if current_cost < lowest_cost:
                lowest_cost = current_cost
                lowest_cost_path = current_path.append(current_airport)
            return lowest_cost_path, lowest_cost

        # Check all possible connections from the current airport
        for connection in airports:
            if connection["start"] == current_airport:
                if connection["end"] not in current_path:
                    lowest_cost_path, lowest_cost = find_path(
                        current_path + [connection["end"]],
                        current_cost + connection["cost"],
                        lowest_cost,
                        lowest_cost_path,
                    )

        return lowest_cost_path, lowest_cost
    
    lowest_cost_path, lowest_cost = find_path([start], 0, lowest_cost, lowest_cost_path)
    return lowest_cost_path, lowest_cost


def check_direct_route(airports, start, end):
    for connection in airports:
        if connection["start"] == start and connection["end"] == end:
            return True, connection["cost"]
    return False, None


airports = [
    {"start": "ISB", "end": "LHR", "cost": 1000},
    {"start": "LHR", "end": "NYC", "cost": 750},
    {"start": "CBS", "end": "NYC", "cost": 775},
    {"start": "ISB", "end": "CBS", "cost": 575},
    {"start": "CBS", "end": "GRC", "cost": 731},
    {"start": "NYC", "end": "KHR", "cost": 350},
    {"start": "NYC", "end": "GRC", "cost": 459},
]

start_point = input("Enter the Start point: ").upper()
end_point = input("Enter the destination point: ").upper()

check_direct_route_result, cost = check_direct_route(airports, start_point, end_point)

if check_direct_route_result:
    print(f"There is a direct route available from {start_point} to {end_point} with a cost of {cost}.")
else:
    path, cost = find_lowest_cost_path(airports, start_point, end_point)
    if not path:
        print(f"The path from {start_point} to {end_point} is not found.")
    else:
        print("Lowest Cost Path:", path)
        print("Cost of Path:", cost)