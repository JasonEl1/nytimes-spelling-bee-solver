print("v.1.0")
print("------")

#maximum word length. Can be modified
maxLength = 7

#read english words list from .txt file
my_file = open("words.txt", "r")
data = my_file.readlines()

#remove newline characters
counter = 0
for i in data:
    data[counter] = i.replace("\n", "")
    counter += 1

#get input letters
letters = []
center = input("Center letter : ")
print("Enter the outer 6 letters : ")
for x in range(6):
    letters.append(input())
    
print("Please wait...")
print("")

result = []

#remove all items that include letters not in the puzzle
counter = 0
good = True
for word in data:
    good = True
    if len(word)<4:
        good = False
    for x in range(len(word)):
        if letters.count(word[x]) == 0 and word[x] is not center:
            good = False
    if good :
        result.append(word)
    counter+=1
    
#remove all items that don't include the center letter
final = []
counter = 0
for index in result:
    if result[counter].count(center) > 0:
        final.append(index)
    counter+=1

print(final)