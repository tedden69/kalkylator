# Kalkylator

Uppgift 1.
- ) Skapa en pythonfil
- ) printa "hej" till användaren
- ) kör filen och se att det skrivs ut "hej"

Uppgift 2.   
(3 delar. Lös en del i taget)

- ) program skriver ut texten: "skriv in ett tal"
- ) användaren skriver in ett tal på skärmen och trycker enter och programmet läser in talet (*)
- ) programmet skriver ut talet

(*) googla "input()"

Uppgift 3

- ) programmet ber att få ytterligare ett tal från användaren, och läser in det talet i en ny variabel
- ) programmet gör om båda talen till Integer (***)
- ) programmet adderat (plus) talen  och printar resultatet

googla "python cast string to integer"  och läs på vad en string och integer är.

Uppgift 4

Nu ska man kunna välja plus eller minus. Läs först in båda talen som i uppgift 3 ovan..

- ) läs sedan in antingen tecknet + eller - från användaren
- ) om +, addera talen och skriv ut. Om -, subtrahera talen och skrib ut (***)

googla "python if statement"
googla "python howto compare if strings are equal"

Uppgift 5

- ) Define a funktion called "getIntegerFromUser()" that reads an integer using input() and returns the integer. 
- ) use the new function twice instead of calling input() directly

Google "python howto define function with rerurn value"

Uppgift 6

Googla kolla try/catch. Python exceptionhantering. 

- ) Lägg ett exceptionblock runt din input() funktion. Och runt din funktion som castar till int. Så det skrivs ut ett fint felmeddelande om man inte skriver in ett tal. 
 
Kolla youtube, googla: "python exception handling"

Uppgift 7

Nu ska ditt program försöka läsa in integers från användaren i en while loop tills dom är godkända, och sen räkna ut svaret:

- ) ifall det blir exception i readIntegerFromUser ska dubreturnera  None istället för 0
- ) lägg varje anrop till readInputFromUser() i varsin while loop som kör tills returvärdet från readIntegerFromUser är skiljt ffån None

Googla while loopar

While variable == None:
    variable = .....


Uppgift 8

- ) skapa funktionen getOperatorFromUser() som ska göra exakt samma sak som getIntegerFromUser() fast med skillnaden att den returnerar antingen + eller -

Den nya funktionennska alltså också loopa över input tills den fått antingen ett + eller ett - från användaren

Uppgift 9)

- ) skapa en funktion calculateSum() som tar 3 argument: tal1, tal2 och operator. Funktionen räknar ut och returnerar summan
- ) Ropa på funktionen och printa summan

Uppgift 10)

- ) skapa en ny fil bredvid nuvarande .py fil, kalla den "functions.py"
- ) flytta dina 3 funktioner till den nya filen.
- ) gör "import functions" från din nuvarande fil så att du kan ropa på funktionerna.


# Worms

Uppgift 1)

- ) Skapa en pythonfil som heter worms.py
- ) Skapa en lista med längd 3
- ) fyll listan på position 0 med texten 'h', på position 1 med texten 'e' och på position '2' med texten 'j'
- ) Printa listan

tips: Googla "python lists", "python init list with fixed length", "python update list in position"

Uppgift 2)

- ) loopa över listan och plocka ut varje element för sig (for loop som först läser position 0, sedan position 1, osv...)
- ) printa varje position

Uppgift 3)
- ) Istället för att lägga in en bokstav på varje element i listan, lägg istället in en list (lista i lista!). Nya listorna ska vara 2 långa
- ) Printa sedan ut listan på samma sätt som tidigare

tips: Google "python list of tuples", "python list of list"
tips: istället för lista kan du använda "tuples".

tips: Googla "python for loop", "python loop over list", "python loop print each element"

Uppgift 4)

- ) Importera nya filen display.py
- ) ropa på funktionen "printWorm()" som ligger i display filen, och skicka med din lista med en mask (list1) som ett argument, så den ritas på skärmen. 
    
    Exempel på import: import display
    Exempel på hur man ropar på funktionen: display.printWorm(worm)
    
Uppgift 5)

- ) Skapa en funktion moveWorm(worm, direction), som alltså tar en variabel som är masklistan och direction, som är direction, och uppdaterar masken
- ) Funktionen skall returner den uppdaterade masken

OBS: Funktionen kan lämnas tom utan logik, dvs returnera nu enbart "worm" variabeln som du tog in som argument

Uppgift 6)

- ) I din nya funktion moveWork, implementera if-statement som tittar på "direction" variabeln, och beroende på om direction är satt till 'w', 'a', 's' eller 'd' ska den köra en print för varje bokats, t.ex om man skickar in 'w' printar den: "changing direction up"



