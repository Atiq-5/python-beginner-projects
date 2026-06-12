import random
dice_faces = {
    1: """
┌─────┐
│     │
│  ●  │
│     │
└─────┘
""",
    2: """
┌─────┐
│ ●   │
│     │
│   ● │
└─────┘
""",
    3: """
┌─────┐
│ ●   │
│  ●  │
│   ● │
└─────┘
""",
    4: """
┌─────┐
│ ● ● │
│     │
│ ● ● │
└─────┘
""",
    5: """
┌─────┐
│ ● ● │
│  ●  │
│ ● ● │
└─────┘
""",
    6: """
┌─────┐
│ ● ● │
│ ● ● │
│ ● ● │
└─────┘
"""
}


s = str(input("Roll Dice?(y/n): "))
s = s.lower()
print(s)
if s == 'y' :
    cont = True
elif s == 'n':
    cont = False
else :
    cont = False
    print("Invalid comand")

while(cont):
    num = random.randint(1,6) 
    print(dice_faces[num])
    s = str(input("Roll Dice?(y/n): "))

    if s == 'y' :
        cont = True
    elif s == 'n':
        cont = False
    else :
        cont = False
        print("Invalid comand")

print("Thanks for rolling dice<3")