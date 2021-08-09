open_file = open("CupcakeInvoices.csv")
for type in open_file:
    type = type.split(",")
    print(type[2])
open_file.close()

open_file = open("CupcakeInvoices.csv")
purchase = []
for row in open_file:
    row = row.rstrip('\n').split(",")
    row_total = float(row[3]) * float(row[4])
    purchase.append(row_total)
print(purchase)
purchase_total = sum(purchase)
print(purchase_total)
open_file.close()
