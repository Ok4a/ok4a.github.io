import csv, requests,  pathlib, os
# v 3.3
def writeHtml(page_name: str, csv_name: str,  html_name: str = None, sort_order_keys: list = ['name'], int_sort = [], in_exclude_keys: list = ['series', 'type'], include: set = set(), 
              exclude: set = set(), displayed_entry_name_keys: list = ['name'], download_image: bool = True, force_download: bool = False) -> None: 
    '''
    page_name: name of the page
    csv_name: name of the csv file without '.csv'
    html_name: name of the html file without '.html', default csv_name
    sort_order_keys: the order which the csv file will be sorted, indecated by dict keys, default sorts only by key 'name'
    int_sort: indicates which key should be sorted as int
    in_exclude_keys: list of dict keys that include and exlude will look at, default ['series', 'type']
    include: will only add elements from the csv file to the html file, if the element has the types from the list, in the dict key indecated by in_exclude_keys, will add all elements if empty, default set()
    exclude: will not add element from csv file to the html file, if the element has the types from the list, in the dict key indecated by in_exclude_keys, default set()
    displayed_entry_name_keys: a list of the columns the displayed name will be, a 'break' in the list will make a line break between the former and next key in the list
    download_image: bool that determins if the image probided should be download to local storage or it should use the url for the image data, default True
    force_download: bool that force the function to download the image even if download image is False and if the image is already downloaded, default False
    '''
    
    start_string = '<!DOCTYPE html>\n<html lang = "en" dir = "ltr">\n<link rel = "stylesheet" href = "../style.css">\n<head>\n\t<meta charset = "utf-8" name = "viewport" content = "width=device-width, initial-scale = 0.6">\n</head>\n\n'
    side_bar_string = '\t<script src = "../sidebar.js"></script>\n'

    include
    if html_name == None:
        html_name = csv_name

    # replaces space with underscore for the html file
    html_name = html_name.replace(' ', '_')

    # if the folder for html files does not exits creates it
    if not os.path.exists('html_lists'):
        os.makedirs('html_lists')

    # opens the csv file
    with open('CSV/' + csv_name + '.csv', mode = 'r') as csv_file:

        # opens/creates the html file
        with open('html_lists/' + html_name + '.html', mode = 'w', encoding = 'utf-8') as html_file:
            
            # reads the csv as a dict with keys from first row (header)
            csv_dict = csv.DictReader(csv_file, delimiter = ';')
            
            # sorts the csv file by column, order base on sort_order_list
            for key in sort_order_keys:
                if key in int_sort or key == "series_number": # sort by int
                    csv_dict = sorted(csv_dict, key = lambda x: int(x[key]))
                else:
                    csv_dict = sorted(csv_dict, key = lambda x: x[key])
      

            # writes first lines of html file
            html_file.write(f'{start_string}<title>{page_name}</title>\n\n<body>\n{side_bar_string}\t<div class = "top_bar">\n\t\t<h1>{page_name}</h1>\n\t</div>\n\t<div class = "grid">\n')

            for entry in csv_dict:

                # check if the entry shall be included or exluded
                type_set = set(entry[key] for key in in_exclude_keys)
                include_intersection_len = len(include.intersection(type_set))
                exclude_intersection_len = len(exclude.intersection(type_set))
                if (len(include) == 0 or include_intersection_len != 0) and (exclude_intersection_len  == 0):

                    # adds more display name info from column choosen by displayed_entry_name_keys
                    is_new_line = True
                    displayed_name = ''
                    for key in displayed_entry_name_keys:
                        # should it make a line break in the displayed name
                        if key == 'break':
                            displayed_name += '<br>'
                            is_new_line = True

                        else:
                            # is it starting a new line
                            if is_new_line:
                                displayed_name += entry[key]
                                is_new_line = False

                            else:
                                displayed_name += ' ' + entry[key]


                    # finds the first index of 'vol.' in display_name, if it exist it adds a line break before. made for book sites
                    vol_index = displayed_name.find('vol.')
                    if vol_index != -1:
                        displayed_name = displayed_name[:(vol_index - 1)] + '<br>' + displayed_name[vol_index:]

                    # finds the last index of ':' in display_name, if it exist it add a line break after.
                    colon_index = displayed_name.rfind(':')
                    if colon_index != -1:
                        displayed_name = displayed_name[:(colon_index + 1)] + '<br>' + displayed_name[(colon_index + 2):]

                    # replaces space with underscore for the html file
                    sub_list_ref = entry['series'].replace(' ', '_')


                    # should it download the image or not
                    if download_image or force_download:
                        # replaces space with underscore in the image name
                        img_path = entry['name'].replace(' ', '_')

                        # removes all intances from element of remove_str_list from img_path
                        remove_str_list = ['<br>', ':', '?', ',', '!', "'", '.', '-']
                        for string in remove_str_list:
                            img_path = img_path.replace(string, '') 

                        img_path = 'list_img/' + img_path + '_' + entry['type'] + '.jpg'

                        # if the folder for the images does not exits, creates it
                        if not os.path.exists('list_img'):
                            os.makedirs('list_img')                    

                        # checks if the image is already downloaded, if not downloads it
                        if  not pathlib.Path(img_path).is_file() or force_download:
                            # gets image data from url
                            img_data = requests.get(entry['image']).content
                            with open(img_path, mode = 'wb') as img_file:
                                img_file.write(img_data)

                        img_path = '../' + img_path
                    else:
                        img_path = entry['image']


                    # writes the element from the csv file
                    html_file.write(f'\t\t<div class = "grid_entry">\n\t\t\t<a href = "{sub_list_ref}.html">\n\t\t\t\t<img src = "{img_path}">\n\t\t\t</a>\n\t\t\t<br>\n\t\t\t<a class = "entry_name">\n\t\t\t\t{displayed_name}\n\t\t\t</a>\n\t\t</div>\n')

            # ends html file        
            html_file.write('\t</div>\n</body>')

            print(page_name)


def getAttributes(csv_name: str, dict_key: int) -> set:
    '''
    csv_name:
    dict_key:
    '''
    with open('CSV/' + csv_name + '.csv') as csv_file:
        csv_dict = csv.DictReader(csv_file, delimiter = ';')
        attribute_set = set()
        non_unique_set = set()

        for entry in csv_dict:
            if entry[dict_key] in attribute_set:
                non_unique_set.add(entry[dict_key])
            attribute_set.add(entry[dict_key])

    return [attribute_set, non_unique_set]


# # Boardgames
csv_file = 'boardgame'

# # makes main boardgame html file
writeHtml('Brætspil', csv_file)

# # makes a html file for only base games
writeHtml('Grund Spil', csv_file, html_name = 'base', include = {'base'})

# makes a html file for each boardgame series
boargame_series = getAttributes(csv_file, 'series')[0]
for series in boargame_series:
    writeHtml(series, csv_file, html_name = series, include = {series})


# Books
csv_file = 'books'

# # make main book html file
writeHtml('Bøger', csv_file, sort_order_keys = ['series_number', 'series', 'last_name'], displayed_entry_name_keys = ['name', 'break', 'first_name', 'last_name'], exclude = {'Math', 'Digt'})

# makes html file for each type of book
book_type = getAttributes(csv_file, 'type')[0]
for series in book_type:
    writeHtml(series, csv_file, html_name = series, sort_order_keys = ['series_number', 'series', 'last_name'], displayed_entry_name_keys = ['name', 'break', 'first_name', 'last_name'], include = {series})

# makes html file for each book series
book_series = getAttributes(csv_file, 'series')[0]
for series in book_series:
    writeHtml(series, csv_file, html_name = series, sort_order_keys = ['series_number', 'series', 'last_name'], displayed_entry_name_keys = ['name', 'break', 'first_name', 'last_name'], include = {series})


# Switch games
csv_file = 'switch'

# make main switch game html
writeHtml('Switch Spil', csv_file)

# make a html for each switch series
switch_series = getAttributes(csv_file, 'series')[0]
for series in switch_series:
    writeHtml(series, csv_file, html_name = series, include = {series})


# LEGO
csv_file = 'lego'

# makes main html file for LEGO
writeHtml('LEGO', csv_file, displayed_entry_name_keys = ['name', 'break', 'number'])

# makes a html file for each LEGO series
lego_series = getAttributes(csv_file, 'series')[0]
for series in lego_series:
    writeHtml(series, csv_file, html_name = series, displayed_entry_name_keys = ['name', 'break', 'number'], include = {series})