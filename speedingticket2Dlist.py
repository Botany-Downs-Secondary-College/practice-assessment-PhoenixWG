speedingTickets = []
totalTickets = 2
name = ""


def printSummary():
    
    print("""
    
    """)
    
    for number in range(0, len(speedingTickets)):
        print("Driver Name: ", speedingTickets[number][0], " Fine amount :$", speedingTickets[number][1])
    print("Total amount of speedingTickets: ", totalTickets)
    
for i in range(totalTickets):
    
    name = raw_input("Enter name: ")
    speedlimit = int(input("Enter speedlimt :"))
    speed = int(input("Enter speed :"))
    fine = speed - speedlimit
    speedingTickets.append([name, fine])
    
print("""
------------------------------------------------
Displaying indexed stored (appended to) list
------------------------------------------------
""")
print(speedingTickets)
printSummary()