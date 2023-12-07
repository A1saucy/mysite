f = open('file.txt', 'w')
f.close()

#with open("file.txt", "w") as file:
	#file.write("Python is awesome!")

# Open and read the file after writing:
with open("file.txt", "r") as file:
    print(file.read())

"""with open("file.txt", "a") as file:
	file.writelines(["Hey there!\n", "Python is awesome!\n"])"""