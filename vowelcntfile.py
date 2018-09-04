fileName = input("Enter the file to check: ").strip()

infile = open(fileName, "r")

vowels = set("AEIOUaeiou")
#cons = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

countV = 0
#countC = 0
for c in infile.read():
    if c in vowels:
        countV += 1
    #elif c in cons:
        #countC += 1
print("The number of Vowels is: ",countV)
#print("\nThe number of consonants is: ",countC)