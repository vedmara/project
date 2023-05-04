year = int(input('What year is the book?'))
hund = year//100
dek = (year//10)%10
if hund == 18 or (hund ==18 and year%100 == 00):
    print("This book from 19 centure {} decade". format(dek))
else:
    print("This book from 20 centure {} decade". format(dek))
