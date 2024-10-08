with  open('./names.txt','r') as names_file:
    name = names_file.readline()
    num_names = 0
    while (name != ''):
        print(name)
        num_names += 1
        name = names_file.readline()

print(f"There are {num_names} names")