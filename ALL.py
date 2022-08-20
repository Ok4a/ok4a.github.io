import csv , operator

tablewidth = 6

sid ='id="switch_td"'
cid ='id=cont_td'

start_string = '<!DOCTYPE html> \n<html>\n<link rel="stylesheet" href="style.css">\n<title>Boardgames</title>\n<body>'
topbar_string = '<table id="topbar"> <tr> <th colspan="3">Mine lister over brætspil, bøger og spil til nintendo Switch</th> </tr> <tr><td><a href="boardgame.html">Boardgames</a></td><td ><a href="books.html">Books</a></td><td><a href="switch.html">Nindtendo Switch</a></td></tr> </table>'

#Boardgames
with open('Boardgame.csv') as boardgame_csv:
    with open('boardgame.html', 'w') as boardgame_html:
        csv_reader = csv.reader(boardgame_csv, delimiter=';')
        csv_reader = sorted(csv_reader, key=operator.itemgetter(0))

        count = 0

        boardgame_html.write(start_string)
        boardgame_html.write(topbar_string)
        boardgame_html.write(f'<table id="maintable">\n \t <tr> <th colspan="{tablewidth}">Boardgames</th> </tr> \n \t <tr> \n')

        for row in csv_reader:
            if  count == tablewidth:
                 boardgame_html.write(f'\t </tr> \n \t <tr>\n')
                 count = 0

            boardgame_html.write(f'\t\t <td> \n \t\t\t  <table  id="innertable"><tr> <td {cid}><img src="{row[3]}"> </td></tr> <tr> <td {cid}>{row[0]}</td></tr></table></td> \n')
            count += 1

        boardgame_html.write('</tr>\n</table>')

        boardgame_csv.close()
        boardgame_html.close()
        print('done')


#BOOKS
with open('Books.csv') as book_csv:
    with open('books.html', 'w') as book_html:
        csv_reader = csv.reader(book_csv, delimiter=';')
        csv_reader = sorted(csv_reader, key=operator.itemgetter(7))
        csv_reader = sorted(csv_reader, key=operator.itemgetter(2))
        csv_reader = sorted(csv_reader, key=operator.itemgetter(4))

        count = 0

        book_html.write(start_string)
        book_html.write(topbar_string)
        book_html.write(f'<table id="maintable">\n \t <tr> <th colspan="{tablewidth}">Books</th> </tr> \n \t <tr> \n')
        
        for row in csv_reader:

            if  count == tablewidth:
                book_html.write(f'\t </tr> \n \t <tr>\n')
                count = 0
            book_html.write(f'\t\t <td> \n \t\t\t  <table id="innertable"><tr> <td {cid}><img src="{row[6]}"> </td></tr> <tr> <td {cid}>{row[1]} <br>{row[5]} {row[4]} </td></tr></table></td> \n')
            count += 1

        book_html.write('</tr>\n</table>')

        book_csv.close()
        book_html.close()
        print('done')


#Switch games
with open('Switch.csv') as switch_csv:
    with open('switch.html', 'w') as switch_html:
        csv_reader = csv.reader(switch_csv, delimiter=';')
        csv_reader = sorted(csv_reader, key=operator.itemgetter(0))

        count = 0



        switch_html.write(start_string)
        switch_html.write(topbar_string)
        switch_html.write(f'<table id="maintable">\n \t <tr> <th colspan="{tablewidth}">Nintendo Switch Games</th> </tr> \n \t <tr> \n')

        for row in csv_reader:
            if  count == tablewidth:
                 switch_html.write(f'\t </tr> \n \t <tr>\n')
                 count = 0

            switch_html.write(f'\t\t <td {sid}> \n \t\t\t  <table  id="innertable"><tr> <td {cid}><img src="{row[2]}"> </td></tr> <tr> <td {cid}>{row[0]}</td {sid}></tr></table></td> \n')
            count += 1

        switch_html.write('</tr>\n</table>')

        switch_csv.close()
        switch_html.close()
        print('done')


