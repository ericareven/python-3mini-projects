with open("story.txt", "r") as f: # open allows you to open a file, and "r" is read mode, "w" is write mode (to over-write or create a file) and with as f provides context for the file so that you can do any operations on the file and then python will close the file
    story = f.read()

words = []
# find <word> in the story. We are looping through the story one character at a time
for i, char in enumerate(story): # enumerate gives you access to an element and its position. 
