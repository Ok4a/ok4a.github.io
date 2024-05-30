import csv, requests,  pathlib
# v 3
def writeHtml(page_name: str, csv_name: str,  html_name: str = None, sort_list: list = [0], int_sort = [], display_type: list = [], display_entry_list: list = [0], img_col: int = 1) -> None: 
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

    # replaces space with underscore for the html file
    if ' ' in html_name:
        html_name = html_name.replace(' ', '_')

    with open(csv_name + '.csv') as csv_file:
        with open('html_lists/' + html_name + '.html', 'w', encoding = 'utf-8') as html_file:
            csv_reader = csv.reader(csv_file, delimiter = ';')
            
            # sorts the csv file by column, order base on sort_list
            for n in sort_list:
                if n in int_sort: # sort by int
                    csv_reader = sorted(csv_reader, key = lambda x: int(x[n]))
                else:
                    csv_reader = sorted(csv_reader, key = lambda x: x[n])
      

            # writes first lines of html file
            html_file.write(f'{start_string}<title>{page_name}</title>\n\n<body>\n{side_bar_string}\t<div class = "top_bar">\n\t\t<h1>{page_name}</h1>\n\t</div>\n\t<div class = "grid">\n')

            for entry in csv_reader:
                # adds more display name info from column choosen by display_row_list
                new_line = True
                displayed_name = ''
                for o in display_entry_list:
                    if o == 'b':
                        displayed_name += '<br>'
                        new_line = True
                    else:
                        if new_line:
                            displayed_name += entry[o]
                            new_line = False
                        else:
                            displayed_name += ' ' + entry[o]

                # finds the first index of 'vol.' in display_name, if it exist it add a line break before. made for book sites
                vol_index = displayed_name.find('vol.')
                if vol_index != -1:
                    displayed_name = displayed_name[:(vol_index - 1)] + '<br>' + displayed_name[vol_index:]

                # finds the last index of ':' in display_name, if it exist it add a line break before.
                colon_index = displayed_name.rfind(':')
                if colon_index != -1:
                    displayed_name = displayed_name[:(colon_index + 1)] + '<br>' + displayed_name[(colon_index + 2):]

                # replaces space with underscore for the html file
                sub_list_ref = entry[2]
                if ' ' in sub_list_ref:
                    sub_list_ref = sub_list_ref.replace(' ', '_')

                # img stuff
                img_path = entry[0]
                # replaces space with underscore in the image name
                if ' ' in img_path:
                    img_path = img_path.replace(' ', '_')
                
                # removes all intances from element of remove_str_list from imag_path
                remove_str_list = ['<br>', ':', '?', ',', '!', "'", '.', '-']
                for string in remove_str_list:
                    if string in img_path:
                        img_path = img_path.replace(string, '') 

                
                img_path = 'list_img/' + img_path + '_'+ entry[3] +'.jpg' 

                # checks if the image is already downloaded, if not downloads it
                if  not pathlib.Path(img_path).is_file():
                    img_data = requests.get(entry[img_col]).content
                    with open(img_path, 'wb') as handler:
                        handler.write(img_data) 

                # writing each object from the csv to the html
                if entry[2] in display_type or entry[3] in display_type or display_type == []: # only write cell if type indicated
                    html_file.write(f'\t\t<div class = "grid_entry">\n\t\t\t<a href = "{sub_list_ref}.html">\n\t\t\t\t<img src = "../{img_path}">\n\t\t\t</a>\n\t\t\t<br>\n\t\t\t<a class = "entry_name">\n\t\t\t\t{displayed_name}\n\t\t\t</a>\n\t\t</div>\n')

            # ends html file        
            html_file.write('\t</div>\n</body>')

            print(page_name)


def getSeriesType(csv_name: str, col_index: list, non_unique: bool = False) -> set:
    with open(csv_name + '.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ';')
        attribute_set = set()
        non_unique_set = set()

        for entry in csv_reader:
            if entry[col_index] in attribute_set:
                non_unique_set.add(entry[col_index])
            attribute_set.add(entry[col_index])
            
    if non_unique:
        return non_unique_set
    else:
        return attribute_set
    

#Boardgames
csv_file = 'boardgame'

# makes main boardgame html file
writeHtml('Brætspil', csv_file)

# makes a html file for only base games
writeHtml('Grund Spil', csv_file, html_name = 'base', display_type = ['base'])

# makes a html file for each boardgame series
boargame_series = getSeriesType(csv_file, 2)
for entry in boargame_series:
    writeHtml(entry, csv_file, html_name = entry, display_type=[entry])

#BOOKS
csv_file = 'books'

# make main book html file
writeHtml('Bøger', csv_file, sort_list = [6, 3, 5], int_sort = [6], display_entry_list = [0, 'b', 4, 5])

# makes html file for each type of book
book_type = getSeriesType(csv_file, 3)
for entry in book_type:
    writeHtml(entry, csv_file, html_name = entry, sort_list = [6, 3, 5], int_sort = [6], display_entry_list = [0, 'b', 4, 5], display_type = [entry])

# makes html file for each book series
book_series = getSeriesType(csv_file, 2)
for entry in book_series:
    writeHtml(entry, csv_file, html_name = entry, sort_list = [6, 3, 5], int_sort = [6], display_entry_list = [0, 'b', 4, 5], display_type = [entry])


#Switch games
csv_file = 'switch'

# make main switch game html
writeHtml('Switch Spil', csv_file)

# make a html for each switch series
switch_series = getSeriesType(csv_file, 2)
for entry in switch_series:
    writeHtml(entry, csv_file, html_name = entry, display_type = [entry])


#LEGO
csv_file = 'lego'

# makes main html file for LEGO
writeHtml('LEGO', csv_file, display_entry_list=[0, 'b', 3])

# makes a html file for each LEGO series
lego_series = getSeriesType(csv_file, 2)
for entry in lego_series:
    writeHtml(entry, csv_file, html_name = entry, display_entry_list = [0, 'b', 3], display_type = [entry])