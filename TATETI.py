# alt = 3
# anc = 5
# a = []

# for i in range(1, alt + 1):
#     if (i == 1 or i == alt):
#         a.append("*"*anc)
#     else:
#         a.append("*   *") 

# a = a*3

# for j in a:
#     print(j*3)
uno = 1
dos = 2
tres = 3
cuatro = 4
cinco = 5
seis = 6
siete = 7
ocho = 8
nueve = 9


print("***** ***** *****\n"
      f"* {siete} * * {ocho} * * {nueve} *\n"
      "***** ***** *****\n"
      "***** ***** *****\n"
      f"* {cuatro} * * {cinco} * * {seis} *\n"
      "***** ***** *****\n"
      "***** ***** *****\n"
      f"* {uno} * * {dos} * * {tres} *\n"
      "***** ***** *****\n")


for k in range(1,5):
        X = int(input("Equipo X: "))

        if X == 1:
                uno = "X"
        if X == 2:
                dos = "X"
        if X == 3:
                tres = "X"
        if X == 4:
                cuatro = "X"
        if X == 5:
                cinco = "X"
        if X == 6:
                seis = "X"
        if X == 7:
                siete = "X"
        if X == 8:
                ocho = "X"
        if X == 9:
                nueve = "X"


        print("***** ***** *****\n"
        f"* {siete} * * {ocho} * * {nueve} *\n"
        "***** ***** *****\n"
        "***** ***** *****\n"
        f"* {cuatro} * * {cinco} * * {seis} *\n"
        "***** ***** *****\n"
        "***** ***** *****\n"
        f"* {uno} * * {dos} * * {tres} *\n"
        "***** ***** *****\n")

        if( uno == "X" and dos == "X" and tres == "X" or
            cuatro == "X" and cinco == "X" and seis == "X" or
            siete == "X" and ocho == "X" and nueve == "X" or
            uno == "X" and cinco == "X" and nueve =="X" or
            tres == "X" and cinco == "X" and siete =="X"):
            print("Equipo X ganó")
            break

        O = int(input("Equipo O: "))
        
        if O == 1:
            uno = "O"
        if O == 2:
            dos = "O"
        if O == 3:
            tres = "O"
        if O == 4:
            cuatro = "O"
        if O == 5:
            cinco = "O"
        if O == 6:
            seis = "O"
        if O == 7:
            siete = "O"
        if O == 8:
            ocho = "O"
        if O == 9:
            nueve = "O"

        print("***** ***** *****\n"
        f"* {siete} * * {ocho} * * {nueve} *\n"
        "***** ***** *****\n"
        "***** ***** *****\n"
        f"* {cuatro} * * {cinco} * * {seis} *\n"
        "***** ***** *****\n"
        "***** ***** *****\n"
        f"* {uno} * * {dos} * * {tres} *\n"
        "***** ***** *****\n")
        
        if( uno == "O" and dos == "O" and tres == "O" or
            cuatro == "O" and cinco == "O" and seis == "O" or
            siete == "O" and ocho == "O" and nueve == "O" or 
            uno == "O" and cinco == "O" and nueve =="O" or 
            tres == "O" and cinco == "O" and siete =="O"):
            print("Equipo O ganó")
            break
    