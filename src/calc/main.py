
import functions as func

number = func.readIntFromUser("skriv in ett tal")
ettill = func.readIntFromUser("skriv in ett till tal")
abba = func.GetOperatorFromUser("* , + eller -")
sum = func.calculateSum(number,ettill,abba)

print (sum)
