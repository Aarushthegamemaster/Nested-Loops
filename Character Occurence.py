string = str(input("Please enter a word here:"))
char = str(input("Please enter a character that's in the word:"))
i = 0
count = 0

while(i<len(string)):
    if(string[i] == char):
        count = count + 1
    i = i+1
        

print("The number of times", char,"occured is",count)