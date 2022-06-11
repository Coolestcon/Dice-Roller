import random, operator, time
import pkg_resources
pkg_resources.require("playsound==1.2.2")
from playsound import playsound


ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

# This Func just gets all the different values from the input, it's a mess, so please don't look at it.
def remove():
    global roll_num, op, sides, op_num
    no_d = dice.split("d", 1)
    roll_num = int(no_d[0])
    
    num_op_num = no_d[1]
    for i in range(0, len(num_op_num)):
        if num_op_num[i] == "+" or num_op_num[i] == "-" or num_op_num[i] == "/" or num_op_num[i] == "*":
            op = num_op_num[i]

    # don't even ask.
    num_0 = num_op_num.replace("+", "!")
    num_1 = num_0.replace("-", "!")
    num_2 = num_1.replace("*", "!")
    num_3 = num_2.replace("/", "!")
    sides_and_op_num = num_3.split("!")
    sides = int(sides_and_op_num[0])
    op_num = sides_and_op_num[1]


# ASCII art from https://onlineasciitools.com
print("-------------------------------------------------------------------------------")
print("DDDDD   IIIII  CCCCC  EEEEEEE  RRRRRR   OOOOO  LL      LL      EEEEEEE RRRRRR")
print("DD  DD   III  CC    C EE       RR   RR OO   OO LL      LL      EE      RR   RR")
print("DD   DD  III  CC      EEEEE    RRRRRR  OO   OO LL      LL      EEEEE   RRRRRR")
print("DD   DD  III  CC    C EE       RR  RR  OO   OO LL      LL      EE      RR  RR")
print("DDDDDD  IIIII  CCCCC  EEEEEEE  RR   RR  OOOO0  LLLLLLL LLLLLLL EEEEEEE RR   RR")
print("-------------------------------------------------------------------------------")
time.sleep(0.3)
print("by Connor Mackay\n\n\n")
time.sleep(0.7)

# Main Loop
while True:
    roll_num = 0
    sides = 0
    op = ""
    op_num = 0
    roll = 0
    total_roll = 0
    
    # Imput
    print("What dice you want to roll? (eg. 2d20+3)")
    dice = str(input(": "))
    print("")
    
    remove()
    
    # This Calculates the dice roll and prints it in the console, if it's a nat 20 or nat 1 then it will be printed.
    for i in range(0,roll_num):
        ran_roll = int(random.randint(1,sides))
        roll = ran_roll + roll
        playsound("sounds/roll.wav")
        if sides == 20 and ran_roll == 20:
            print("Nat 20! :)")
            playsound("sounds/nat20.wav")
        elif sides == 20 and ran_roll == 1:
            print("Nat 1! :(")
            playsound("sounds/nat1.wav")
        else:
            print("Roll %s: %s" %((i + 1), ran_roll))
    op_func = ops[op]
    total_roll = op_func(int(roll), int(op_num))
    print("-------------------------------------------------------------------------------")
    print("You Rolled:")
    print(total_roll)
    print("-------------------------------------------------------------------------------")
