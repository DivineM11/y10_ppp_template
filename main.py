from time import sleep
print("Welcome!")
sleep(0.2)

def slowPrint(conditions):
    for letter in conditions:
        pass


conditions = print("Here are the terms and conditions. 1: ")

play = input("Would u like to play rock paper scissors?(yes/no): ")

if play == "yes":
    print("Brillant! Now we can begin!")
    print()
elif play == "no":
    print("Alright then. I'll hope to see you soon...")
else:
    print("I don't understand this gibberish. Type 'yes' or 'no'!")