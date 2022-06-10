import random, operator, time
from playsound import playsound

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

roll = 0


def remove():
    global roll_num, op, sides, op_num
    no_d = dice.split("d", 1)
    roll_num = int(no_d[0])
    
    num_op_num = no_d[1]
    for i in range(0, len(num_op_num)):
        if num_op_num[i] == "+" or num_op_num[i] == "-" or num_op_num[i] == "/" or num_op_num[i] == "*":
            op = num_op_num[i]

    # Why is splitting strings so annoying, I am so bad at programming
    num_0 = num_op_num.replace("+", "!")
    num_1 = num_0.replace("-", "!")
    num_2 = num_1.replace("*", "!")
    num_3 = num_2.replace("/", "!")
    sides_and_op_num = num_3.split("!")
    sides = int(sides_and_op_num[0])
    op_num = sides_and_op_num[1]


#ASCII art from https://onlineasciitools.com
print("--------------------------------------------------------------")
print("DDDDD   IIIII  CCCCC  EEEEEEE  RRRRRR   OOOOO  LL      LL      EEEEEEE RRRRRR")
print("DD  DD   III  CC    C EE       RR   RR OO   OO LL      LL      EE      RR   RR")
print("DD   DD  III  CC      EEEEE    RRRRRR  OO   OO LL      LL      EEEEE   RRRRRR")
print("DD   DD  III  CC    C EE       RR  RR  OO   OO LL      LL      EE      RR  RR")
print("DDDDDD  IIIII  CCCCC  EEEEEEE  RR   RR  OOOO0  LLLLLLL LLLLLLL EEEEEEE RR   RR")
print("--------------------------------------------------------------")
print("by Connor Mackay\n\n\n")
time.sleep(1)

while True:
    roll_num = 0
    sides = 0
    op = ""
    op_num = 0
    roll = 0
    
    print("What dice you want to roll? (eg. 2d20+3)")
    dice = str(input(": "))
    print("")
    remove()

    total_roll = 0
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

    print("\n--------------------------------------------------------------")
    print("You Rolled:")
    print(total_roll)
    print("--------------------------------------------------------------\n")
