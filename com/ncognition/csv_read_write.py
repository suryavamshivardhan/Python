import csv
def csv_read_write():
    with open('C:/MyDocs/Training/Python/WorkSpace/resources/input.csv','w',newline='') as csvfile:
        csvdatawriter = csv.writer(csvfile,delimiter=',',quotechar='"')
        csvdatawriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        csvdatawriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

    with open('C:/MyDocs/Training/Python/WorkSpace/resources/input.csv') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',',quotechar='"')
        for row in csvreader:
            print(row)
csv_read_write()