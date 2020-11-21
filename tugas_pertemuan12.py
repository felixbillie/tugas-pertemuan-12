# 1 => one

kata = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def terbilang(n):
    if n < 10:
        return kata[n]
    elif n >= 1_000_000_000:
        return terbilang(n//1000000000) + " billion " + terbilang(n%1000000000)   
    elif n >= 1_000_000:
        return terbilang(n//1000000) + " million " + terbilang(n%1000000)   
    elif n >= 1_000:
        return terbilang(n//1000) + " thousand " + terbilang(n%1000)  
    elif n >= 100:
        return terbilang(n//100) + " hundred " + ("and "if (n%100)!=0 else "") + terbilang(n%100)    
    elif n >= 20:
        if n // 10 == 2:
            return "twenty " + terbilang(n%20)
        elif n // 10 == 3:
            return "thirty " + terbilang(n%30)
        elif n // 10 == 4:
            return "forty " + terbilang(n%40)
        elif n // 10 == 5: 
            return "fifty " + terbilang(n%50) 
        else:
            return terbilang(n//10) + ("ty "if (n//10)!=8 else "y ")+ terbilang(n%10)
    else:
        if n == 10:
            return "ten"
        elif n == 11:
            return "eleven"
        elif n == 12:
            return "twelve"
        elif n == 13:
            return "thirteen"
        elif n == 15:
            return "fifteen"     
        else:
            return terbilang(n%10) + "teen"

import os
while True:
    os.system("cls")         
    print("Counting")
    print("========")
    try:
        angka = int(input("Input a Number : "))
        print(f"{angka} = {terbilang(angka)}")
    except:
        print("Input Numbers Only")
    os.system("pause")
    
    

