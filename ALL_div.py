import csv
# v 3
def writeHtml(page_name: str, csv_name: str,  html_name: str = None, sort_list: list = [0], int_sort = [], display_type: list = [], display_row_list: list = [0], img_col: int = 1) -> None: 
    '''
    page_name: name of the page
    csv_name: name of the csv file without '.csv'
    html_name: name of the html file without '.html', default html_name = csv_name
    sort_list: the order which the csv file will be sorted by column index, default sorts by first column
    int_sort: indicates which sorted column contain integers
    display_type: will only add elements from the csv file to the html file if csv element column 3 or 4 is in display_type. Will add all elements if empty
    display_row_list: a list of the columns the displayed name will be, a 'b' in the list will make a line break between the former and next column in the list
    img_col: index for which column contains image links, default 1
    '''
    
    start_string = '<!DOCTYPE html>\n<html lang = "en" dir = "ltr">\n<link rel = "stylesheet" href = "../style.css">\n<head>\n\t<meta charset = "utf-8" name = "viewport" content = "width=device-width, initial-scale = 0.6">\n</head>\n\n'
    side_bar_string = '\t<script src = "../sidebar.js"></script>\n'
       
    # colour_list = ['#FFF4A3', '#FFC0C7', '#D9EEE1', '#4f35c4']

    if html_name == None:
        html_name = csv_name


    if ' ' in html_name:
        html_name = html_name.replace(' ', '_')

    with open(csv_name + '.csv') as csv_file:
        with open('html_lists/' + html_name + '.html', 'w', encoding = 'utf-8') as html_file:
            csv_reader = csv.reader(csv_file, delimiter = ';')
            
            # sorts the csv file by column, order base on sort_list
            for n in sort_list:
                if n in int_sort: # sor by int
                    csv_reader = sorted(csv_reader, key = lambda x: int(x[n]))
                else:
                    csv_reader = sorted(csv_reader, key = lambda x: x[n])
      

            # writes first lines of html file
            html_file.write(f'{start_string}<title>{page_name}</title>\n\n<body>\n{side_bar_string}\t<div class = "top_bar">\n\t\t<h1>{page_name}</h1>\n\t</div>\n\t<div class = "grid">\n')

            for row in csv_reader:
                # adds more display name info from column choosen by display_row_list
                new_line = True
                displayed_name = ''
                for o in display_row_list:
                    if o == 'b':
                        displayed_name += '<br>'
                        new_line = True
                    else:
                        if new_line:
                            displayed_name += row[o]
                            new_line = False
                        else:
                            displayed_name += ' ' + row[o]

                # finds the index of 'vol.' in display_name, if it exist it add a line break before. made for book sites
                vol_index = displayed_name.find('vol.')
                if vol_index != -1:
                    displayed_name = displayed_name[:(vol_index - 1)] + '<br>' + displayed_name[vol_index:]

                colon_index = displayed_name.rfind(':')
                if colon_index != -1:
                    displayed_name = displayed_name[:(colon_index + 1)] + '<br>' + displayed_name[(colon_index + 2):]

                sub_list_ref = row[2]
                if ' ' in sub_list_ref:
                    sub_list_ref = sub_list_ref.replace(' ', '_')
 
                # writing each object from the csv to the html
                if row[2] in display_type or row[3] in display_type or display_type == []: # only wirte cell if type indicated
                    html_file.write(f'\t\t<div class = "grid_entry">\n\t\t\t<a href = "{sub_list_ref}.html">\n\t\t\t\t<img src = "{row[img_col]}">\n\t\t\t</a>\n\t\t\t<br>\n\t\t\t<a class = "entry_name">\n\t\t\t\t{displayed_name}\n\t\t\t</a>\n\t\t</div> \n')
                    
            html_file.write('\t </div> \n </body>')

            print(page_name)


def getSeriesType(csv_name: str, col_index: list, non_unique: bool = False):
    with open(csv_name + '.csv') as csv_file:
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
csv_file = 'boardgame'
writeHtml('Brætspil', csv_file)
writeHtml('Grund Spil', csv_file, html_name = 'base', display_type = ['base'])

boargame_series = getSeriesType(csv_file, 2)
for elem in boargame_series:
    writeHtml(elem, csv_file, html_name = elem, display_type=[elem])

#BOOKS
csv_file = 'books'
writeHtml('Bøger', csv_file, sort_list = [6, 3, 5], int_sort = [6], display_row_list = [0, 'b', 4, 5])

book_type = getSeriesType(csv_file, 3)
for elem in book_type:
    writeHtml(elem, csv_file, html_name = elem, sort_list = [6, 3, 5], int_sort = [6], display_row_list = [0, 'b', 4, 5], display_type = [elem])

book_series = getSeriesType(csv_file, 2)
for elem in book_series:
    writeHtml(elem, csv_file, html_name = elem, sort_list = [6, 3, 5], int_sort = [6], display_row_list = [0, 'b', 4, 5], display_type = [elem])


#Switch games
csv_file = 'switch'
writeHtml('Switch Spil', csv_file)

switch_series = getSeriesType(csv_file, 2)
for elem in switch_series:
    writeHtml(elem, csv_file, html_name = elem, display_type = [elem])

#Lego
csv_file = 'lego'
writeHtml('LEGO', csv_file, display_row_list=[0, 'b', 3])

lego_series = getSeriesType(csv_file, 2)
for elem in lego_series:
    writeHtml(elem, csv_file, html_name = elem, display_row_list = [0, 'b', 3], display_type = [elem])