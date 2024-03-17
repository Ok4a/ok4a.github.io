import csv
# v 3?
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

    start_string = '<!DOCTYPE html> \n<html lang = "en" dir = "ltr">\n<link rel = "stylesheet" href="../style.css"> <head><meta charset = "utf-8" name="viewport" content="width=device-width,initial-scale=0.7"> </head>\n<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n'
    side_bar_string = '\t<script src="../sidebar.js"></script>\n'
       

    colour_list = ["#FFF4A3","#FFC0C7","#D9EEE1","#4f35c4"]

    if html_name == None:
        html_name = csv_name

    with open(csv_name+'.csv') as csv_file:
        with open("html_lists/"+html_name+'.html', 'w', encoding = 'utf-8') as html_file:
            csv_reader = csv.reader(csv_file, delimiter = ';')
            
            # sorts the csv file by column, order base on sort_list
            for n in sort_list:
                if n in int_sort: # sor by int
                    csv_reader = sorted(csv_reader, key = lambda x: int(x[n]))
                else:
                    csv_reader = sorted(csv_reader, key = lambda x: x[n])
      

            # writes first lines of html file
            html_file.write(f'{start_string}<title>{page_name}</title>\n<body>\n')
            html_file.write(side_bar_string)
            #html_file.write(f'\n\t<table id="maintable"> \n \t\t<tr> <th colspan = "{table_width}"> {page_name} </th> </tr> \n\t\t<tr> \n')
            html_file.write(f'\t<div class="top_bar"><h1>{page_name}</h1></div> \n<div class = "grid">\n\t\t\n')

            count = 0 # counter for table width
            for row in csv_reader:

                """if  count == table_width:  # rests count and writes table new row to file
                    html_file.write(f'\t </tr> \n<tr>\n')
                    count = 0"""

                # adds more display name info form column choosen by display_row_list
                display_name = ""
                for o in display_row_list:
                    if o == "b":
                        display_name += "<br>"
                    else:
                        display_name += " " + row[o]
                
                    
                # writing each object from the csv to the html
                if row[2] in display_type or row[3] in display_type or display_type == []: # only wirte cell if type indicated
                    html_file.write(f'\t\t<div> <a href="{row[2]}.html"><img src = "{row[img_col]}"></a> <br>{display_name}</div>\n')

                    #style="background-color:{colour_list[count%4]}"
                    count += 1
                    
            html_file.write('\t</div>\n</body>')

            print(page_name)


def getSeriesType(csv_name: str, col_index: list, non_unique: bool = False):
    with open(csv_name+'.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ';')
        attribute_set = set()
        non_unique_set = set()
        for row in csv_reader:
            if row[col_index] in attribute_set:
                non_unique_set.add(row[col_index])
            attribute_set.add(row[col_index])
    if non_unique:
        return non_unique_set
    else:
        return attribute_set

#Boardgames
writeHtml("Brætspil", "boardgame")
writeHtml("Grund Spil", "boardgame", html_name="base", display_type=["base"])
boargame_series = getSeriesType("boardgame", 2)
for elem in boargame_series:
    writeHtml(elem, "boardgame", html_name=elem, display_type=[elem])

#BOOKS
writeHtml("Bøger", "books" , sort_list=[6,3,5], int_sort=[6], display_row_list=[0,"b",4,5])

book_type = getSeriesType("books", 3)
for elem in book_type:
    writeHtml(elem, "books", html_name=elem , sort_list = [6,3,5], int_sort = [6], display_row_list=[0,"b",4,5], display_type = [elem])

book_series = getSeriesType("books", 2)
for elem in book_series:
    writeHtml(elem, "books", html_name=elem , sort_list = [6,3,5], int_sort = [6], display_row_list = [0,"b",4,5], display_type = [elem])

#Switch games
writeHtml("Switch Spil", "switch")

switch_series = getSeriesType("switch", 2)
for elem in switch_series:
    writeHtml(elem, "switch", html_name = elem, display_type=[elem])

#Lego
writeHtml("LEGO", "lego", display_row_list=[0,"b",3])

lego_series = getSeriesType("lego", 2)
for elem in lego_series:
    writeHtml(elem, "lego", html_name = elem , display_row_list = [0,"b",3], display_type = [elem])