#THIS PROGRAM CONVERTS NUMBERS TO ITS WORDS EQUIVALENT
def onesplace(n):
    convert1 = {
        1 : "isa",
        2 : "dalawa",
        3 : "tatlo",
        4 : "apat",
        5 : "lima",
        6 : "anim",
        7 : "pito",
        8 : "walo",
        9 : "siyam"
    } 
    return convert1.get(n, "")

def tensplace(n):
    convert2 = {
        2 : "dalawampu",
        3 : "tatlumpu",
        4 : "apat na pu",
        5 : "limampu",
        6 : "anim na pu",
        7 : "pitumpu",
        8 : "walumpu",
        9 : "siyam na pu"
    } 
    return convert2.get(n, "")

def hundsplace(n):
    if int (n) == 0:
        return ""
    elif (n == 4) or (n == 6) or (n == 9):
        return str(onesplace(n)) + " na raan "  
    elif (n == 1) or (n == 2) or (n == 3) or (n == 5) or (n == 7) or (n == 8):
        return str(onesplace(n)) + "ng daan "


#FOR ADDING LIBO AT THE END
def thouplace(n):
    num_ones = int(n)%10
    num_ten = int((int(n)/10)%10)   
    num_hun = int((int(n)/100)%10)
    
    if n == 0:
        return ""
    elif num_ones == 1 or num_ones == 2 or num_ones == 3 or num_ones == 5 or num_ones == 7 or num_ones == 8:
        return str(take3places(n)) + "ng libo "
    elif num_ones == 4 or 6 or 9:
        return str(str(take3places(n))) + " na libo "

#FOR ADDING MILYON AT THE END
def milyonplace(n):
    num_ones = int(n)%10
    num_ten = int((int(n)/10)%10)   
    num_hun = int((int(n)/100)%10)
    
    if n == 0:
        return ""
    elif num_ones == 1 or num_ones == 2 or num_ones == 3 or num_ones == 5 or num_ones == 7 or num_ones == 8:
        return str(take3places(n)) + "ng milyon "
    elif num_ones == 4 or 6 or 9:
        return str(str(take3places(n))) + " na milyon "

#FOR ADDING BILYON AT THE END
def bilyonplace(n):
    num_ones = int(n)%10
    num_ten = int((int(n)/10)%10)   
    num_hun = int((int(n)/100)%10)
    
    if n == 0:
        return ""
    elif num_ones == 1 or num_ones == 2 or num_ones == 3 or num_ones == 5 or num_ones == 7 or num_ones == 8:
        return str(take3places(n)) + "ng bilyon "
    elif num_ones == 4 or 6 or 9:
        return str(str(take3places(n))) + " na bilyon "

#THIS TAKES NUMBERS PER 3 DIGITS AND CONVERTS IT TO WORDS
def take3places(n):
    N_ones = int(n)%10
    N_tens = int((int(n)/10)%10)
    N_hund = int((int(n)/100)%10)
    if N_tens == 0:
        if n == 0:
            return ""
        else:
            return hundsplace(N_hund) + str(onesplace(N_ones))
    elif N_tens == 1:
        if (N_ones == 0) and (N_hund == 0):
            return "sampu"
        elif (N_ones == 0) and (N_hund != 0):
            return str(hundsplace(N_hund)) + " at " + "sampu"
        elif N_ones == 7:
            return str(hundsplace(N_hund)) + "labim" + str(onesplace(N_ones))
        elif (N_ones == 2) or (N_ones ==3) or (N_ones ==5) or (N_ones ==9):
            return str(hundsplace(N_hund)) + "labin" + str(onesplace(N_ones))
        elif (N_ones == 1) or (N_ones ==4) or (N_ones ==6) or (N_ones == 8): 
            return str(hundsplace(N_hund)) + "labing-" + str(onesplace(N_ones))
        else: 
            return str(hundsplace(N_hund)) + ""
    elif (N_ones == 0) and ((N_tens == 2) or (N_tens==3) or (N_tens ==4) or (N_tens ==5) or (N_tens ==6) or (N_tens ==7) or (N_tens ==8) or (N_tens ==9)):
        return str(hundsplace(N_hund)) + " at " + str(tensplace(N_tens))
    elif (N_tens == 2) or (N_tens == 3) or (N_tens == 4) or (N_tens == 5) or (N_tens == 6) or (N_tens == 7) or (N_tens == 8) or (N_tens == 9):
        return str(hundsplace(N_hund)) + str(tensplace(N_tens)) + "'t " + str(onesplace(N_ones))
    
#MAIN FUNCTION
X = True
while X == True:
    num = int(input("Input a number: "))
    thou = int((num/1000)%1000)
    mil = int((num/1000000)%1000000)
    bil = int((num/1000000000)%1000000000)
    print(bilyonplace(bil) + ", " + milyonplace(mil) + ", " + thouplace(thou) + ", " + take3places(num)) 
    
#FOR ASKING NEW INPUTS  
    ans = input("Another number? (Y/N) ")
    if ans == "Y" or ans == "y":
        X = True
    elif ans == "N" or ans == "n":
        X = False
