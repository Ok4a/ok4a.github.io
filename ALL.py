import csv

def writeHtml(page_name: str, csv_name: str,  html_name: str = None, sort_list: list = [0], int_sort = [], display_type: list = [], display_row_list: list = [0], table_width: int = 4, img_col: int = 1) -> None: 
    """
    page_name: name of the page
    csv_name: name of the csv file without '.csv'
    html_name: name of the html file without '.html', default html_name = csv_name
    sort_list: the order which the csv file will be sorted by column index, default sorts by first column
    int_sort: indicates which sorted column contain integers
    
    
    table_width: how many column that will be created, default 4
    img_col: index for which column contains image links, default 1
    """
    start_string = '<!DOCTYPE html> \n <html lang = "en" dir = "ltr">\n<link rel = "stylesheet" href="style.css"> <head> <meta charset = "utf-8"> </head>\n'
    topbar_string = '<table id = "topbar"> <tr> <th colspan = "4">Mine lister over brætspil, bøger, LEGO og spil til Nintendo Switch</th> </tr> <tr> <td><a href = "boardgame.html">Brætspil</a></td><td ><a href="books.html">Bøger</a></td><td ><a href="lego.html">LEGO</a></td><td><a href="switch.html">Nintendo Switch</a></td></tr> </table>'
    cid = 'id = cont_td'

    if html_name == None:
        html_name = csv_name

    with open(csv_name+'.csv') as csv_file:
        with open(html_name+'.html', 'w', encoding = 'utf-8') as html_file:
            csv_reader = csv.reader(csv_file, delimiter = ';')
            
            # sorts the csv file by column, order base on sort_list
            for n in sort_list:
                if n in int_sort: # sor by int
                    csv_reader = sorted(csv_reader, key = lambda x: int(x[n]))
                else:
                    csv_reader = sorted(csv_reader, key = lambda x: x[n])
      


            # writes first lines of html file
            html_file.write(f'{start_string} <title>{page_name}</title>\n<body>')
            html_file.write(topbar_string)
            html_file.write(f'<table id="maintable"> \n \t <tr> <th colspan = "{table_width}"> {page_name} </th> </tr> \n \t <tr> \n')

            count = 0 # counter for table width
            for row in csv_reader:


                if  count == table_width:  # rests count and writes table new row to file
                    html_file.write(f'\t </tr> \n \t <tr>\n')
                    count = 0

                # adds more display name info form column choosen by display_row_list
                """display_name = row[0]
                if display_row_list != []:
                    display_name += "<br>"
                    for o in display_row_list:
                        display_name += " " + row[o]"""

                display_name = ""
                for o in display_row_list:
                    if o == "b":
                        display_name += "<br>"
                    else:
                        display_name += " " + row[o]
                
                    
                # writing each object from the csv to the html
                if row[2] in display_type or row[3] in display_type or display_type == []: # only wirte cell if type indicated
                    html_file.write(f'\t\t <td> \n \t\t\t  <table id = "innertable"><tr> <td {cid}><img src = "{row[img_col]}"> </td> </tr> <tr> <td {cid}> {display_name} </td> </tr> </table> </td> \n')
                    count += 1
                    
            html_file.write('</tr>\n</table>')

            print(page_name)


def test(csv_name: str):
    with open(csv_name+'.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ';')
        series_set = set()
        type_set = set()
        for row in csv_reader:
            series_set.add(row[2])
            type_set.add(row[3])
    return series_set, type_set

"""
series_set, type_set = test("books")
for i in type_set:
    writeHtml(i, "books", html_name="test/"+i, sort_list=[6,3,5], int_sort=[6], display_row_list=[0,"b",4,5], display_type=[i])"""

#Boardgames
writeHtml("Brætspil", "boardgame")

#BOOKS
writeHtml("Bøger", "books" , sort_list=[6,3,5], int_sort=[6], display_row_list=[0,"b",4,5])

#Switch games
writeHtml("Switch Spil", "switch")

#Lego
writeHtml("LEGO", "lego", display_row_list=[0,"b",3])
