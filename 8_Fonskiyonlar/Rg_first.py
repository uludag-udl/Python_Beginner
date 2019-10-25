firstNumber=int(input("Bir Sayı Giriniz: "))
secondNumber=int(input("Bir Daha Sayi Giriniz: "))
print("\nfirstNumber : {}\nsecondNumber : {}\n".format(firstNumber,secondNumber))


def calculator(firstNumber,secondNumber,default):
    if default=="add":
        return firstNumber+secondNumber
    if default=="sub":
        return firstNumber-secondNumber
    if default=="div":
        return firstNumber/secondNumber
    if default=="mul":
        return firstNumber*secondNumber

operation=calculator(firstNumber,secondNumber,"add")
print(f"Yapılan işlemin Sonucu ==> {operation}") #f print ile 
