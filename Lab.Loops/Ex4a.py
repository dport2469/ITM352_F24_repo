sample_fares = [8.60, 5.75, 13.25, 21.21]

for fare in sample_fares:
    if fare > 12:
        print(f"${fare} is too high!")
    else:
        print(f"${fare} is low.")