"""
print(),open(), type(), len(), pow(), bin(),abs(),memoryview()
iter(),next(),object(),property(),staticmethod()
super(),getattr(),hasattr()
delattr(),classmethod(),issubclass(),setattr()

ve şimdiye kadar kullandığımız bir çok fonksiyon gömülü fonksiyondur.
"""


dizi="Uludag Üniversitesi Yapay Zeka Topluluğu"
print(len(dizi))

dizi_list=["Uludag", "Üniversitesi","Yapay","Zeka","Topluluğu"]
print(dizi_list)

dizi_sorted=sorted(dizi_list)
print(dizi_sorted)

dizi_reversed=list(reversed(dizi_list)) # "dizi_list[::-1]" de aynı sonucu verir.
print(dizi_reversed)
