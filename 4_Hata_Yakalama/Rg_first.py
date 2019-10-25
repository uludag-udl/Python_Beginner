"""
Bazı Hatalar:
int("20asd") ==> ValueError
print(20/0) ==> ZeroDivisionError
print("Uluda"g) ==> SyntaxError


"""
try:
    print("Bölme işlemi Gerçekleştirilecektir.")
    x=int(input("Pay Giriniz: "))
    y=int(input("Payda Giriniz: "))
    z=x/y
    print("\n\nGirilen Pay: {}\nGirilen Payda: {} \nSonuc: {}".format(x,y,z))
except ZeroDivisionError:
    print("Bir Hata Bulundu..... => Bir sayı sifira bölünemez")


