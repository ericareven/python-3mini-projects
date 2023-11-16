with open("story.txt", "r") as f: # open allows you to open a file, and "r" is read mode, "w" is write mode (to over-write or create a file) and with as f provides context for the file so that you can do any operations on the file and then python will close the file
    story = f.read()

# create a set instead of a list, bc a set will only include unique elementsw, while a list will include all elements, even if there are repeats
# words = [] list
words = set()

start_of_word = -1 # we found the beginning of the word
target_start = "<"
target_end = ">"

# find <word> in the story. We are looping through the story one character at a time
for i, char in enumerate(story): # enumerate gives you access to an element and its position. 
    if char == target_start:
        start_of_word = i
    
    if char == target_end and start_of_word != -1: # if we found the > AND we had the <
        word = story[start_of_word: i + 1] # gives us access to a slice (subsection) of the string. Go up to AND include the ending index
        # words.append(word) add word to words list
        words.add(word)
        start_of_word = -1 # reset start_of_word so the function can look for the next word

answers = {} # empty dictionary

for word in words: # iterate through set
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer # creates a dictionary with all the words associated with all the values

for word in words:
    story = story.replace(word, answers[word])

print(story)