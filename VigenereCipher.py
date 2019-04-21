#this is dodgy
def stringelements(str, length):
    for i in range(length):
        print("%s[%i] = %s" % (str, i, str[i]))
    return


dim=255 #having dim and offset as global variables allows easy changes to the tabula recta
offset=0

count=0

#create tabula recta
tabula=[[0] * dim for j in range(dim)]

for i in range(dim):
    for j in range(dim):
        tabula[i][j]=chr(((j + count) % dim) + offset)
    count+=1



#checker
for row in tabula:
   print(' '.join([str(elem) for elem in row]))

#input stage
plainstr = input("Please enter your arbitrary string:")
keyword = input("Please enter your keyword:")
print("Your plaintext string is: " + plainstr)
print("Your keyword is: " + keyword)

length = len(plainstr)
print("Length of input string: %i" %length)
#stringelements(plainstr, length)

#remove whitespaces from input
plainstr = plainstr.replace(' ', '')
print("spaces removed: %s" % plainstr)
print("Length of nospace input string: %i" %len(plainstr))
#stringelements(plainstr, length)

#create array to perform cipher with
cipharray=[[0] * len(plainstr) for i in range(3)]
for j in range(len(plainstr)):
    cipharray[1][j] = plainstr[j]

for j in range(len(plainstr)):
    cipharray[0][j] = keyword[j % len(keyword)]

#encode
for j in range(len(plainstr)):
    refa=ord(cipharray[1][j])-offset
    refb=ord(cipharray[0][j])-offset
    cipharray[2][j] = tabula[refa][refb]

#checker
for row in cipharray:
   print(' '.join([str(elem) for elem in row]))

cipherstr="".join(cipharray[2])

#show encrypted message
print("\nYour encrypted message is: %s\n" % cipherstr)

#decode
decodearray=[[0] * len(cipherstr) for i in range(3)]
for j in range(len(plainstr)):
    decodearray[1][j] = cipherstr[j]

for j in range(len(cipherstr)):
    decodearray[0][j] = keyword[j % len(keyword)]

for j in range(len(cipherstr)):
    refa2=ord(decodearray[0][j])-offset
    refb2=ord(decodearray[1][j])-ord(decodearray[0][j])
    decodearray[2][j] = tabula[0][refb2]

#checker
for row in decodearray:
   print(' '.join([str(elem) for elem in row]))

decodestr="".join(decodearray[2])

#show encrypted message
print("\nYour decrypted message is: %s\n" % decodestr)