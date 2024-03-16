import csv , operator

table_width = 4

sid ='id ="switch_td"'
cid ='id = cont_td'

start_string = '<!DOCTYPE html> \n <html lang="en" dir="ltr">\n<link rel="stylesheet" href="style.css"> <head> <meta charset="utf-8"> </head>\n'
topbar_string = '<table id="topbar"> <tr> <th colspan="4">Mine lister over brætspil, bøger, LEGO og spil til Nintendo Switch</th> </tr> <tr><td><a href="boardgame.html">Brætspil</a></td><td ><a href="books.html">Bøger</a></td><td ><a href="lego.html">LEGO</a></td><td><a href="switch.html">Nintendo Switch</a></td></tr> </table>'


def beginHtmlFile(html_file, page_name: str, top_bar: str, start_str: str) -> None: 
    html_file.write(f'{start_str} <title>{page_name}</title>\n<body>')
    html_file.write(top_bar)
    html_file.write(f'<table id="maintable">\n \t <tr> <th colspan="{table_width}">{page_name}</th> </tr> \n \t <tr> \n')
    print("test")




#Boardgames
with open('Boardgame.csv') as boardgame_csv:
    with open('boardgame.html', 'w', encoding = 'utf-8') as boardgame_html:
        csv_reader = csv.reader(boardgame_csv, delimiter=';')
        csv_reader = sorted(csv_reader, key=operator.itemgetter(0))

        name_of_page = "Brætspil"

        count = 0

        boardgame_html.write(f'{start_string} <title>{name_of_page}</title>\n<body>')
        boardgame_html.write(topbar_string)
        boardgame_html.write(f'<table id="maintable">\n \t <tr> <th colspan="{table_width}">{name_of_page}</th> </tr> \n \t <tr> \n')

        for row in csv_reader:
            if  count == table_width:
                 boardgame_html.write(f'\t </tr> \n \t <tr>\n')
                 count = 0

            boardgame_html.write(f'\t\t <td> \n \t\t\t  <table  id="innertable"><tr> <td {cid}><img src="{row[3]}"> </td></tr> <tr> <td {cid}>{row[0]}</td></tr></table></td> \n')
            count += 1

        boardgame_html.write('</tr>\n</table>')


        print('Boardgame')



#BOOKS
with open('Books.csv') as book_csv:
    with open('books.html', 'w', encoding='utf-8') as book_html:
        csv_reader = csv.reader(book_csv, delimiter=';')
        csv_reader = sorted(csv_reader, key=operator.itemgetter(7))
        csv_reader = sorted(csv_reader, key=operator.itemgetter(2))
        csv_reader = sorted(csv_reader, key=operator.itemgetter(4))

        # write first lines of html file
        book_html.write(f'{start_string} <title>{name_of_page}</title>\n<body>')
        book_html.write(topbar_string)
        book_html.write(f'<table id="maintable">\n \t <tr> <th colspan="{table_width}">{name_of_page}</th> </tr> \n \t <tr> \n')
        
        name_of_page = "Bøger"

        count = 0 # counter for table width
        for row in csv_reader:
            if  count == table_width: # rests count and writes table new row to file
                book_html.write(f'\t </tr> \n \t <tr>\n')
                count = 0

            # writing each object from the csv to the html
            book_html.write(f'\t\t <td> \n \t\t\t  <table id="innertable"><tr> <td {cid}><img src="{row[6]}"> </td></tr> <tr> <td {cid}>{row[1]} <br>{row[5]} {row[4]} </td></tr></table></td> \n')
            count += 1
            
        # ends html table
        book_html.write('</tr>\n</table>')


        print('Books')


#Switch games
name_of_page = "Switch Spil"        
with open('Switch.csv') as switch_csv: # open csv file for read
    with open('switch.html', 'w', encoding='utf-8') as switch_html: # open html file for write
        csv_reader = csv.reader(switch_csv, delimiter=';')
        csv_reader = sorted(csv_reader, key=operator.itemgetter(0)) # sorting csv data based on first column (name of game)

        
        # write first lines of html file
        switch_html.write(f'{start_string} <title>{name_of_page}</title>\n<body>')
        switch_html.write(topbar_string)
        switch_html.write(f'<table id="maintable">\n \t <tr> <th colspan="{table_width}">{name_of_page}</th> </tr> \n \t <tr> \n')

        

        beginHtmlFile(switch_csv,name_of_page, topbar_string, start_string)

        count = 0 # counter for table width
        for row in csv_reader:
            if  count == table_width: # rests count and writes table new row to file
                 switch_html.write(f'\t </tr> \n \t <tr>\n')
                 count = 0

            # writing each object from the csv to the html
            switch_html.write(f'\t\t <td > \n \t\t\t  <table  id="innertable"><tr> <td {cid}><img src="{row[2]}"> </td></tr> <tr> <td {cid}>{row[0]}</td></tr></table></td> \n')
            count += 1

        # ends html table
        switch_html.write('</tr>\n</table>')


        print('Switch')


#Lego
with open('Lego.csv') as lego_csv: # open csv file for read
    with open('lego.html', 'w', encoding = 'utf-8') as lego_html: # open html file for write
        csv_reader = csv.reader(lego_csv, delimiter = ';')
        csv_reader = sorted(csv_reader, key = operator.itemgetter(0)) # sorting csv data based on first column (name of lego set)

        # write first lines of html file
        #lego_html.write(f'{start_string} <title>{name_of_page}</title>\n<body>')
        #lego_html.write(topbar_string)
        #lego_html.write(f'<table id="maintable">\n \t <tr> <th colspan="{table_width}">{name_of_page}</th> </tr> \n \t <tr> \n')
        name_of_page = "Lego"
        beginHtmlFile(lego_html,name_of_page, topbar_string, start_string)
        

        count = 0 # counter for table width
        for row in csv_reader:
            if  count == table_width: # rests count and writes table new row to file
                 lego_html.write(f'\t </tr> \n \t <tr>\n')
                 count = 0

            # writing each object from the csv to the html
            lego_html.write(f'\t\t <td> \n \t\t\t  <table  id="innertable"><tr> <td {cid}><img src="{row[2]}"> </td></tr> <tr> <td {cid}>{row[0]}<br>{row[1]}</td></tr></table></td> \n')
            count += 1

        # ends html table
        lego_html.write('</tr>\n</table>')

        print('Lego')



