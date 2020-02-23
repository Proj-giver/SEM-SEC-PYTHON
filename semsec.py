import random
import string

def xor(X, Y): return "".join([chr(ord(a) ^ ord(b)) for (a, b) in zip(X, Y)])

def SemEnc(Key, Plaintxt):

    random.seed(a=None, version=2)
    noise = string.printable
    RandomBits = ''
    for i in range(20):
        RandomBits += RandomBits.join(random.choice(noise))

    # print("Random Bits: ", RandomBits, ", len: ", len(RandomBits))

    KeyPluse = Key + RandomBits

    # print("Key Plus:", KeyPluse)
    random.seed(a=KeyPluse, version=2)
    noise2 = string.printable
    randomData = ""
    for i in range(len(Plaintxt)):
        randomData += randomData.join(random.choice(noise2))

    # print("random data: ", randomData)
    #
    # if len(Plaintxt) != len(randomData):
    #     print("Plain text length: ", len(Plaintxt), ", Random Data Length: ", len(randomData))

    cyphertxt = xor(randomData, Plaintxt)
    return RandomBits + cyphertxt

def SemDeCription(cyphertxt, key):
    randomBits = cyphertxt[0:20]
    KeyPluse = key + randomBits

    random.seed(a=KeyPluse, version=2)
    noise2 = string.printable
    randomData = ""
    for i in range(len(cyphertxt)):
        randomData += randomData.join(random.choice(noise2))
    cleartxt = xor(cyphertxt[20:], randomData)
    return(cleartxt)

print("Case 1--------------------------------------------")
plaintxt1 = "Hello World!"
key1 = "sec1"
print("Plain Text: ", plaintxt1)
print("Key: ", key1)
cyphertxt = SemEnc(key1, plaintxt1)
print("Cypher Text: ", cyphertxt)
print("This is the clear text: ", SemDeCription(cyphertxt, key1))
print("Case 2--------------------------------------------")
plaintxt1 = "The password is two!!!"
key1 = "2!!!"
print("Plain Text: ", plaintxt1)
print("Key: ", key1)
cyphertxt = SemEnc(key1, plaintxt1)
print("Cypher Text: ", cyphertxt)
print("This is the clear text: ", SemDeCription(cyphertxt, key1))
print("Case 3--------------------------------------------")
plaintxt1 = "Attack by sea at dawn!"
key1 = "element of suprise"
print("Plain Text: ", plaintxt1)
print("Key: ", key1)
cyphertxt = SemEnc(key1, plaintxt1)
print("Cypher Text: ", cyphertxt)
print("This is the clear text: ", SemDeCription(cyphertxt, key1))
print("Case 4--------------------------------------------")
plaintxt1 = "The tresure is below the 4th panel"
key1 = "they will never get our precous!!"
print("Plain Text: ", plaintxt1)
print("Key: ", key1)
cyphertxt = SemEnc(key1, plaintxt1)
print("Cypher Text: ", cyphertxt)
print("This is the clear text: ", SemDeCription(cyphertxt, key1))
print("Case 5--------------------------------------------")
plaintxt1 = "Phiscaly destroy SSD # 0XC3, immediatly!!!"
key1 = "YcVpquctsgg^)@]s7f5$'s{"
print("Plain Text: ", plaintxt1)
print("Key: ", key1)
cyphertxt = SemEnc(key1, plaintxt1)
print("Cypher Text: ", cyphertxt)
print("This is the clear text: ", SemDeCription(cyphertxt, key1))
