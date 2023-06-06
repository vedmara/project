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

    print("The monthly sales for the past 12 Months are as follows: ")

    for row in data:
        sales.append(row)
        print(row['month'], ':', row['sales'])

def total_sale():
    data = read_csv()

    sales = []

    for row in data:
        total_sales = int(row['sales'])
        sales.append(total_sales)

    total = sum(sales)
    print("The total sales across the past 12 months = £{}" .format(total))



def avg_monthly_expenditure():
    data = read_csv()

    expenditure = []

    for row in data:
        sale_expenditure = int(row['expenditure'])
        expenditure.append(sale_expenditure)

    avg_expenditure = sum(expenditure) / len(expenditure)
    print("The average monthly expenditure = £{}" .format(avg_expenditure))


#1 Highest and Lowest Sales of the month
def highest_and_lowest():
    data = read_csv()
    sales = []
    for row in data:
        sort = int(row['sales'])
        sales.append(sort)
    sales = sorted(sales)
    high = sales[-1]
    low = sales[0]
    print('The highest sale of the years was: £{}' .format(high))
    print('The lowest sale of the year was: £{} ' .format(low))

#Profit from each month
def profit():
    data = read_csv()
    prof_it = []
    prof = 0
    for row in data:
        sale_expenditure = int(row['expenditure'])
        sales = int(row['sales'])
        profit = sales - sale_expenditure
        prof = prof + profit
        prof_it.append(profit)

    average = prof / len(prof_it)
    print("The profit for each month of the year is as follow:")
    print(*prof_it, sep="\n")
    print("The average profit is: £ {}" .format(average))

message = """ Please chose from the following options:
    1 = The sales for each month of the last year
    2 = Last Years Total sales
    3 = The average monthly expenditure
    4 = The Highest and Lowest sale of the year
    5 = The profit for each month
    6 = Exit Program

    """

while(True):
    try:
        print(message)

        x = int(input('Please make your choice:'))

        if x == 1:
            print_sales()

        elif x == 2:
            total_sale()
        elif x == 3:
            avg_monthly_expenditure()
        elif x == 4:
            highest_and_lowest()
        elif x == 5:
            profit()
        else:
            print('Exiting program')
            break

    except ValueError:
        print('Please enter a valid number.')