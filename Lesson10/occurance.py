string=input("Enter the word")
character=input("Enter the character you want to check")
i=0
counter=0
while i<len(string):
    if string[i]==character:
        counter=counter+1
    i=i+1
print(counter)