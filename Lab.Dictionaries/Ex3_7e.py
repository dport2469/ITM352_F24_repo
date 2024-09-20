# Create a list of dictionaries where each dictionary represents a trip
trips = [
    {'duration': 1.1, 'fare': 6.25},
    {'duration': 0.8, 'fare': 5.25},
    {'duration': 2.5, 'fare': 10.50},
    {'duration': 2.6, 'fare': 8.05}
]


# Print out the dictionary
print(trips)
#duration = trip_durations[2]
print(f"The 3'rd trip was {trips[2]['duration']} miles and cost ${trips[2]['fare']:0.2f}")