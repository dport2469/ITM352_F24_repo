# Initialize a tuple of strings representing different emotions
emotions = ("happy", "sad", "fear", "surprise")

# Use a conditional expression to print "true" or "false"
print("The last element is")
if( (emotions[-1] == "happy") and (len(emotions) > 3) ):
    print("happy")
else:
    print(" is not happy")