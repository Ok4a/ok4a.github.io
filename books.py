import csv , operator

with open('Books.csv') as csv_file:
    with open('books.html', 'w') as txt:
        csv_reader = csv.reader(csv_file, delimiter=';')
        csv_reader = sorted(csv_reader, key=operator.itemgetter(3))
        csv_reader = sorted(csv_reader, key=operator.itemgetter(1))
        csv_reader = sorted(csv_reader, key=operator.itemgetter(4))
        line_count = -1
        tablewidth = 6
        count = 0
        

        txt.write(f'<!DOCTYPE html> \n<html>\n<link rel="stylesheet" href="style.css">\n<title>BOOKS</title>\n<body>')
        txt.write(f'<table id="maintable">\n \t <tr><td colspan="2"><a href="boardgame.html">Boardgames</a></td><td colspan="2"><a href="books.html">Books</a></td><td colspan="2"><a href="switch.html">Nindtendo Switch</a></td></tr>\n \t <tr> <th colspan="{tablewidth}">Books</th> </tr> \n \t <tr> \n')
        
        for row in csv_reader:

            if  count == tablewidth:
                txt.write(f'\t </tr> \n \t <tr>\n')
                count = 0

            txt.write(f'\t\t <td> \n \t\t\t  <table id="innertable"><tr> <td><img src="{row[6]}"> </td></tr> <tr> <td>{row[1]} <br>{row[5]} {row[4]} </td></tr></table></td> \n')
            count += 1

        txt.write('</tr>\n</table>')

        print('done')