import csv

def read_csv():
    sales = []

    with open('sales.csv', 'r') as csv_file:
        sale = csv.DictReader(csv_file)
        for row in sale:
            sales.append(row)

    return sales

def print_sales():
    data = read_csv()
    sales = []

    for row in data:
        sales.append(row)
        print((row['sales']))

def total_sale():
    

    for row in data:
        total_sales = int(row[sales])
        sales.append(total_sales)

    total = sum(sales)
    print("The total sales across the 12 months = {}" .format(total))

read_csv()
print_sales()