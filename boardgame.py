import csv , operator

with open('Boardgame.csv') as csv_file:
    with open('boardgame.html', 'w') as txt:
        csv_reader = csv.reader(csv_file, delimiter=';')
        csv_reader = sorted(csv_reader, key=operator.itemgetter(0))
        line_count = -1
        tablewidth = 6
        count = 0


        txt.write(f'<!DOCTYPE html> \n<html>\n<link rel="stylesheet" href="style.css">\n<title>Boardgames</title>\n<body>')
        txt.write(f'<table id="maintable">\n \t <tr colspan="{tablewidth}"> <th>Brætpils liste</th> </tr> \n \t <tr> \n')

        for row in csv_reader:
            if  count == tablewidth:
                 txt.write(f'\t </tr> \n \t <tr>\n')
                 count = 0
            else:
                txt.write(f'\t\t <td> \n \t\t\t  <table  id="innertable"><tr> <td><img src="{row[3]}"> </td></tr> <tr> <td>{row[0]}</td></tr></table></td> \n')
                count += 1

        txt.write('</tr>\n</table>')

        print('done')