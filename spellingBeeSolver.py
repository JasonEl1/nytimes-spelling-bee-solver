print("------")
print("v.1.1")
print("------")

#maximum word length. Can be modified
maxLength = 7

#read english words list from .txt file
data = []
file = open("words.txt", "r")
for line in file:
    data.append(line.strip("\n"))

#get input letters
center = input("Center letter : ")
print("Enter the outer 6 letters separated by 'enter': ")
letters = []
for _ in range(6):
    letters.append(input())

print("Please wait...\n")

result = []

#remove all items that include letters not in the puzzle
for word in data:
    if len(word)>3:
        good = True
        for char in word:
            if letters.count(char) == 0 and char is not center:
                good = False
        if(good):
            result.append(word)

#remove all items that don't include the center letter
for index in result:
    if index.count(center) == 0:
        result.remove(index)

print("Possible words:")
print(*result, sep=", ")
