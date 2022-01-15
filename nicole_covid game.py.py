count = 0


#for scenarios, it is just one single letter
a = "Due to decline in  coronavirus cases, many shops have reopened and a new title will be launching at your local videogame shop. "
b = "A sale is held for the new game. You can just buy the game or get it in a bundle with a limited edition controller. The queue for just the game is longer since fewer people have money to buy the bundle."
c = "You stay at home and scroll through social media. You come across a post claiming that there will be hbl starting tomorrow."
d = "There are large crowds of customers. When you get home, your throat is dry and you feel feverish. "
e = "You spend the extra money to get the controller. But we're in a pandemic, and money isn't easy to come by. Perhaps you could have spent it on something more essential. "
f = "PM Lee doesn't announce hbl, but he drinks from his cup and says in four languages that bubble tea stores will be closed indefinitely tomorrow onwards."
g = "The post was fake news! oh no your whole class didn't go to school and everyone got a yellow form :( remember to check your sources!"
h = "You have been diagnosed with COVID-19. Maybe if you had been more careful, you could have avoided being infected. Thankfully you sought medical attention immediately and didn't spread it to anyone else. "
i = "You feel better after resting for after a few days. To be safe, you isolate yourself from others for 14 days. Your sense of social responsibility may have just curbed the spread of the virus. "
j = "You stay at home to avoid the crowd. Kudos to you for keeping yourself and others safe! Perhaps you could have stayed healthy without being cut off from the rest of the world?"



#start
currentScenario = a

#### a
while currentScenario == a:
    print(currentScenario)
    choice = "" 
    while choice != "1" or choice != "2":
        if count == 0:
            choice = input(
'''
option 1: Go
option 2: Don't go

select 1 or 2: ''')
            count += 1
            
        else:
            print("\ninvalid input, please enter 1 or 2")
            choice = input(
'''
select 1 or 2: ''')
        if choice == "1":
            currentScenario = b
            count = 0
            break
        elif choice == "2":
            currentScenario = c
            count = 0
            break
        
#### b

while currentScenario == b:
    print("\n \n \n" + currentScenario)
    choice = "" 
    while choice != "1" or choice != "2":
        if count == 0:
            choice = input(
'''
option 1: Get bundle for $100 as there is a long queue
option 2: Wait in line to buy the game at $50 

select 1 or 2: ''')
            count += 1
            
        else:
            print("\ninvalid input, please enter 1 or 2")
            choice = input(
'''
select 1 or 2: ''')
        if choice == "1":
            currentScenario = d
            count = 0
            break
        elif choice == "2":
            currentScenario = e
            count = 0
            break

#### c

while currentScenario == c:
    print("\n \n \n" + currentScenario)
    choice = "" 
    while choice != "1" or choice != "2":
        if count == 0:
            choice = input(
'''
option 1: Wait until 4pm to watch pm lee's address to check if it's true
option 2: Share the post with your classmates

select 1 or 2: ''')
            count += 1
            
        else:
            print("\ninvalid input, please enter 1 or 2")
            choice = input(
'''
select 1 or 2: ''')
        if choice == "1":
            currentScenario = f
            count = 0
            break
        elif choice == "2":
            currentScenario = g
            count = 0
            break

#### d

while currentScenario == d:
    print("\n \n \n" + currentScenario)
    choice = "" 
    while choice != "1" or choice != "2":
        if count == 0:
            choice = input(
'''
option 1: Head to the nearest clinic
option 2: Drink water and hope you get better

select 1 or 2: ''')
            count += 1
            
        else:
            print("\ninvalid input, please enter 1 or 2")
            choice = input(
'''
select 1 or 2: ''')
        if choice == "1":
            currentScenario = h
            count = 0
            break
        elif choice == "2":
            currentScenario = i
            count = 0
            break

#### e

while currentScenario == e:
    print("\n \n \n" + currentScenario)
    break

#### f

while currentScenario == f:
    print("\n \n \n" + currentScenario)
    choice = "" 
    while choice != "1" or choice != "2":
        if count == 0:
            choice = input(
'''
option 1: Rush out to buy bubble tea one last time
option 2: Avoid the crowds of people buying bubble tea

select 1 or 2: ''')
            count += 1
            
        else:
            print("\ninvalid input, please enter 1 or 2")
            choice = input(
'''
select 1 or 2: ''')
        if choice == "1":
            currentScenario = d
            count = 0
            break
        elif choice == "2":
            currentScenario = j
            count = 0
            break

#### g

while currentScenario == g:
    print("\n \n \n" + currentScenario)
    break

###### h
##
##if currentScenario == h:
##    print("\n \n \n" + currentScenario)
##    
##
###### i
##
##if currentScenario == i:
##    print("\n \n \n" + currentScenario)
    

#### j

while currentScenario == j:
    print("\n \n \n" + currentScenario)
    break

#### d repeat

while currentScenario == d:
    print("\n \n \n" + currentScenario)
    choice = "" 
    while choice != "1" or choice != "2":
        if count == 0:
            choice = input(
'''
option 1: Avoid the crowds of people buying bubble tea
option 2: Drink water and hope you get better

select 1 or 2: ''')
            count += 1
            
        else:
            print("\ninvalid input, please enter 1 or 2")
            choice = input(
'''
select 1 or 2: ''')
        if choice == "1":
            currentScenario = h
            count = 0
            break
        elif choice == "2":
            currentScenario = i
            count = 0
            break

#### h

if currentScenario == h:
    print("\n \n \n" + currentScenario)
    

#### i

if currentScenario == i:
    print("\n \n \n" + currentScenario)
   
