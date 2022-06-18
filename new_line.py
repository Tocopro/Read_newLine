
sonnets = open("C:\\Users\\NEAK\\Documents\\Sonnets\\reprints.txt")
user = int(input("Enter a Line NUmber: "))
user = user - 1
lines_read = sonnets.readlines()

print("Line requested is " + str(user + 1))
print(lines_read[user])
