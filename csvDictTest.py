import csv

csv_name = 'switch'


with open(csv_name + '.csv') as csv_file:
    # csv_reader = csv.reader(csv_file, delimiter = ';')

    records = csv.DictReader(csv_file, delimiter=';')

    csv_sort = sorted(records, key= lambda x: x["name"])

    # for n in sort_list:
    #     if n in int_sort: # sort by int
    #         csv_reader = sorted(csv_reader, key = lambda x: int(x[n]))
    #     else:
    #         csv_reader = sorted(csv_reader, key = lambda x: x[n])
    for entry in csv_sort:
        print(entry['name'])
        print()
