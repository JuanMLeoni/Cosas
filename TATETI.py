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

b = {1:uno,2:dos,3:tres,4:cuatro,5:cinco,6:seis,7:siete,8:ocho,9:nueve}


print("***** ***** *****\n"
      f"* {b[7]} * * {b[8]} * * {b[9]} *\n"
      "***** ***** *****\n"
      "***** ***** *****\n"
      f"* {b[4]} * * {b[5]} * * {b[6]} *\n"
      "***** ***** *****\n"
      "***** ***** *****\n"
      f"* {b[1]} * * {b[2]} * * {b[3]} *\n"
      "***** ***** *****\n")


for k in range(1,5):
        X = int(input("Equipo X: "))
        for i in b:
             if X == b[i]:
                  b[i] = "X"
                  print("***** ***** *****\n"
                    f"* {b[7]} * * {b[8]} * * {b[9]} *\n"
                    "***** ***** *****\n"
                    "***** ***** *****\n"
                    f"* {b[4]} * * {b[5]} * * {b[6]} *\n"
                    "***** ***** *****\n"
                    "***** ***** *****\n"
                    f"* {b[1]} * * {b[2]} * * {b[3]} *\n"
                    "***** ***** *****\n")

        if( b[1] == "X" and b[2] == "X" and b[3] == "X" or
            b[4] == "X" and b[5] == "X" and b[6] == "X" or
            b[7] == "X" and b[8] == "X" and b[9] == "X" or
            b[1] == "X" and b[4] == "X" and b[7] == "X" or
            b[2] == "X" and b[5] == "X" and b[8] == "X" or
            b[3] == "X" and b[6] == "X" and b[9] == "X" or
            b[1] == "X" and b[5] == "X" and b[9] == "X" or
            b[3] == "X" and b[5] == "X" and b[7] == "X"):
            print("Equipo X ganó")
            break

        O = int(input("Equipo O: "))
        for i in b:
             if O == b[i]:
                  b[i] = "O"
                  print("***** ***** *****\n"
                    f"* {b[7]} * * {b[8]} * * {b[9]} *\n"
                    "***** ***** *****\n"
                    "***** ***** *****\n"
                    f"* {b[4]} * * {b[5]} * * {b[6]} *\n"
                    "***** ***** *****\n"
                    "***** ***** *****\n"
                    f"* {b[1]} * * {b[2]} * * {b[3]} *\n"
                    "***** ***** *****\n")
        
        if( b[1] == "O" and b[2] == "O" and b[3] == "O" or
            b[4] == "O" and b[5] == "O" and b[6] == "O" or
            b[7] == "O" and b[8] == "O" and b[9] == "O" or
            b[1] == "O" and b[4] == "O" and b[7] == "O" or
            b[2] == "O" and b[5] == "O" and b[8] == "O" or
            b[3] == "O" and b[6] == "O" and b[9] == "O" or
            b[1] == "O" and b[5] == "O" and b[9] == "O" or
            b[3] == "O" and b[5] == "O" and b[7] == "O"):
            print("Equipo O ganó")
            break
    