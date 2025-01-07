file = open("info.txt", "a")
file.write("This is a new line of text\n")
file.close()

file = open("info.txt", "a")
file.write("Second line of code\nThird line")
file.close()

file = open("info.txt", "r")
content = file.read
print(file)
