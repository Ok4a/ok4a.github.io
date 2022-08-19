import csv , operator

with open('Switch.csv') as csv_file:
    with open('switch.html', 'w') as txt:
        csv_reader = csv.reader(csv_file, delimiter=';')
        csv_reader = sorted(csv_reader, key=operator.itemgetter(0))
        tablewidth = 6
        count = 0
        sid ='id="switch_td"'

        txt.write('<!DOCTYPE html> \n<html>\n<link rel="stylesheet" href="style.css">\n<title>Boardgames</title>\n<body>')
        txt.write(f'<table id="maintable">\n \t <tr> <th colspan="{tablewidth}">Nintendo Switch Games</th> </tr> \n \t <tr> \n')

        for row in csv_reader:
            if  count == tablewidth:
                 txt.write(f'\t </tr> \n \t <tr>\n')
                 count = 0

            txt.write(f'\t\t <td {sid}> \n \t\t\t  <table  id="innertable"><tr> <td {sid}><img src="{row[2]}"> </td></tr> <tr> <td {sid}>{row[0]}</td {sid}></tr></table></td> \n')
            count += 1

        txt.write('</tr>\n</table>')

        print('done')