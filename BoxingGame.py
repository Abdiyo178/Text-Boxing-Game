import random
health = 100


Abdiyo = ""
combos = ["jab", "block", "duck", "weave", "righthook", "lefthook", "uppercut"]
computer = (random.choice(combos))
yes_varianti = ["yes", "ye", "y", "yez", "yess"]
play = input("Do you want to play? Yes/No: ").lower()
if play not in yes_varianti:
    print("Bye!")
    quit()
while Abdiyo not in combos:
    Abdiyo = input("What do you choose? Jab/Block/Duck/Weave/RightHook/LeftHook/UpperCut").lower()
    if Abdiyo not in combos:
        print("Please enter a valid choice!")

print(f"You choose: {Abdiyo}. \nhealth : {health}.")
print("Computer: " + computer)

def subtract(health, jab):
    return(health - jab)
    jab = 25
    health = 100
print (eval('subtract(health, jab)'))
def subtract(health, block):
    return(health - block)
    block = -3
    health = 100
print (eval('subtract(health, block)'))
def subtract(health, weave):
    return(health - weave)
    weave = -1
    health = 100
print (eval('subtract(health, weave)'))
def subtract(health, righthook):
    return(health - righthook)
    block = 45
    health = 100
print (eval('subtract(health, righthook)'))
def subtract(health, lefthook):
    return(health - lefthook)
    block = 55
    health = 100
print (eval('subtract(health, lefthook)'))
def subtract(health, uppercut):
    return(health - uppercut)
    block = 50
    health = 100
print (eval('subtract(health, uppercut)'))


























    