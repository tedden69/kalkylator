
def readIntFromUser(text):
    while True:
        try:
            x = input(text)
            print(x)
            return int(x)
        except:
            print ("bad input")


def GetOperatorFromUser(text2):
   while True:
        y = input(text2)
        if y == "+":
            return "+"

        if y == "-":
            return "-"

        if y == "*":
            return "*"

        print ("bad input")

def calculateSum(tal1,tal2,operator):
    if operator == "-":
        sum = tal1 - tal2
        return sum
    if operator == "+":
        sum = tal1 + tal2
        return sum
    if operator == "*":
        sum = tal1 * tal2
        return sum