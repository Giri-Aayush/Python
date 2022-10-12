#create a dictionary, take input from the user for a word a return its meaning
def checkkey(dic, pin):
    if pin in dic.keys():
        return True
    else:
        return False


Dictionary = {
    "abamp": "Electricity",
    "mezzaluna": "a crescent-shaped,with a handle on each end or a connecting handle.",
    "abator": "law a person who effects an abatement",
    "Abboud": "Sudanese army general and statesman: prime minister 1958–64.",
    "labarum": "an ecclesiastical standard or banner, as for carrying in procession",
    "Lachish": "a Canaanite city captured by Joshua: now an archaeological site in Israel.",
    "kabaka": "the traditional king of Buganda, a region and former kingdom of southern Uganda",
    "kalendar": "a calendar, especially of a church"
}

#Driver Code
print("Enter the word, you want the meaning for : ")
key = input()

if checkkey(Dictionary, key):
    print(Dictionary[key])
else:
    print("The word does not exists in Dictionary")