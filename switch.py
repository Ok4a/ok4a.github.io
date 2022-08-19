import csv , operator

with open('Switch.csv') as csv_file:
    with open('switch.txt', 'w') as txt:
        csv_reader = csv.reader(csv_file, delimiter=';')
        csv_reader = sorted(csv_reader, key=operator.itemgetter(3))
        csv_reader = sorted(csv_reader, key=operator.itemgetter(5))

        line_count = -1
        tablewidth = 6
        count = 0
        
        txt.write(f'<table id="maintable">\n \t <tr colspan="{tablewidth}"> <th>Bog liste</th> </tr> \n \t <tr> \n')
        for row in csv_reader:

            if  count == tablewidth:
                txt.write(f'\t </tr> \n \t <tr>\n')
                count = 0

            txt.write(f'\t\t <td> \n \t\t\t  <table><tr> <td><img src="{row[7]}"> </td></tr> <tr> <td>{row[2]} <br> {row[5]} </td></tr></table></td> \n')
            count += 1

        txt.write('</tr>\n</table>')

        print('done')