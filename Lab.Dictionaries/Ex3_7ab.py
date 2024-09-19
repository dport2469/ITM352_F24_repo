# Define the list of taxi trip durations in miles
trip_durations = [1.1, 0.8, 2.5, 2.6]

# Define the tuple of fares for the same number of trips
trip_fares = ("$6.25", "$5.25", "$10.50", "$8.05")

# Store both the list and tuple in a dictionary
trips = {
    "miles": trip_durations,
    "fares": trip_fares
}

# Print out the dictionary
print(trips)
print(f"The 3'rd trip was {trips['miles'][2]} miles and cost {trips['fares'][2]}")