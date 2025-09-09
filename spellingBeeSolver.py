print("------")
print("v.1.2")
print("------")

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

# add words to result list if contain necessary letters and center letter
result = []
for word in data:
    if len(word)>3:
        good = True
        for char in word:
            if letters.count(char) == 0 and char is not center:
                good = False
        if(good and word.count(center)>0):
            result.append(word)

print("Possible words:")
print(*result, sep=", ")
