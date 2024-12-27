import csv, requests, pathlib, os
from collections import defaultdict
# v 3.6.4
def writeHtml(page_name: str, csv_name: str,  html_name: str = None, sort_order_keys: list = ['name'], int_sort = [], in_exclude_keys: list = ['series', 'type'], include: set = set(), 
              exclude: set = set(), compress_series_entries: bool = False, start_compressed: bool = True, displayed_entry_name_keys: list = ['name'], needed_breaks: int = 0, download_image: bool = True, force_download: bool = False) -> None: 
    '''
    page_name: name of the page
    csv_name: name of the csv file without '.csv'
    html_name: name of the html file without '.html', default csv_name
    sort_order_keys: the order which the csv file will be sorted, indicated by dict keys, default sorts only by key 'name'
    int_sort: indicates which key should be sorted as int
    in_exclude_keys: list of dict keys that include and exclude will look at, default ['series', 'type']
    include: will only add elements from the csv file to the html file, if the element has the types from the list, in the dict key indicated by in_exclude_keys, will add all elements if empty, default set()
    exclude: will not add element from csv file to the html file, if the element has the types from the list, in the dict key indicated by in_exclude_keys, default set()
    compress_series_entries: if set to True, compress entries with more than one entry in its series, default False
    displayed_entry_name_keys: a list of the columns the displayed name will be, a 'break' in the list will make a line break between the former and next key in the list
    needed_breaks:
    download_image: bool that determines if the image provided should be download to local storage or it should use the url for the image data, default True
    force_download: bool that force the function to download the image even if download image is False and if the image is already downloaded, default False
    '''
    

    if start_compressed:
        uncompress_on_load = 'uncompress_on_load = false;'
    else:
        uncompress_on_load = 'uncompress_on_load = true;'

    if compress_series_entries:
        compressed_entries = 'compressed_entries = true;'
    else:
        compressed_entries = 'compressed_entries = false;'
    

    start_string = '<!DOCTYPE html>\n<html lang = "en" dir = "ltr">\n<link rel = "stylesheet" href = "../style.css">\n<head>\n\t<meta charset = "utf-8" name = "viewport" content = "width=device-width, initial-scale = 0.6">\n</head>\n\n'
    side_bar_string = '\t<script>\n\t\t' + compressed_entries + '\n\t\t'  + uncompress_on_load + '\n\t</script>\n\t<script src = "../sidebar.js"></script>\n'

    if html_name == None:
        html_name = csv_name
    else:
        html_name += '_' + csv_name


    remove_str_list = ['<br>', ':', '?', ',', '!', "'", '.', '-']

    # replaces space with underscore for the html file
    html_name = html_name.replace(' ', '_')

    # if the folder for html files does not exits creates it
    if not os.path.exists('html_lists'):
        os.makedirs('html_lists')

    # gets the number of entires om each series
    counts_dict = getAttributeCount(csv_name, "series")

    if csv_name == 'boardgame':
        number_of_entries_in_series = getAttributeCount(csv_name, 'base_game')

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
            i = 0
            first_entry_stuff = True

            # for entry in csv_dict:
            while i < len(csv_dict):
                entry = csv_dict[i]
                i += 1
                compress_id = ''
                hide_class = ''

                # check if the entry shall be included or excluded
                type_set = set(entry[key] for key in in_exclude_keys)
                include_intersection_len = len(include.intersection(type_set))
                exclude_intersection_len = len(exclude.intersection(type_set))

                if (len(include) == 0 or include_intersection_len != 0) and exclude_intersection_len  == 0:

                    # adds more display name info from column chosen by displayed_entry_name_keys
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


                    # the number of entries in the series of the current entry
                    if csv_name != 'boardgame':
                        number_of_entries_in_series = counts_dict[entry['series']]
    

                    # how many line breaks in the displayed name
                    break_count = displayed_name.count('<br>')

                    # adds the number the current entry is in its series, used mainly for books
                    if break_count == 1 and 'series_number' in entry.keys():
                        # index for the first html line break
                        first_break_index = displayed_name.find('<br>')

                        # adds the number of the series if there is more than one the entry in it
                        if number_of_entries_in_series != 1 and entry['series'] != 'All You Need is Kill':
                            displayed_name = displayed_name[:first_break_index] + '<br>#' + entry['series_number'] + displayed_name[first_break_index:]
                        
                        else: # adds line break if the entry is the only in its series
                            displayed_name = displayed_name[:first_break_index] + '<br>' + displayed_name[first_break_index:]

                    
                    # compress entries if there is more than one entry in its series and if only_first_in_series is True
                    if number_of_entries_in_series != 1 and compress_series_entries:
                        if 'series_number' in entry.keys():
                            if int(entry['series_number']) == 1 and first_entry_stuff: # if the entry uses 'vol' as the series counter
                                if vol_index != -1: # if it is the first in its series
                                    last_break_index = displayed_name.rfind('<br>')
                                    displayed_name = displayed_name[:(vol_index + 9)] + ' - ' + str(number_of_entries_in_series) + displayed_name[last_break_index:]
        
                                elif displayed_name.count('#') != 0:
                                    number_index = displayed_name.find('#')
                                    displayed_name = displayed_name[:(number_index + 2)] + ' - ' + str(number_of_entries_in_series) + displayed_name[(number_index+2):]
                                compress_id = 'name = "compressed"'
                                first_entry_stuff = False
                                i -= 1 
                            else: # skip other entries in a series
                                
                                compress_id = 'name = noncompressed'
                                hide_class = 'hide_entry'
                                first_entry_stuff = True

                        # boardgame compression
                        elif 'base_game' in entry.keys():
                            if len(entry['base_game']) != 0:

                                if entry['type'] == 'base' and first_entry_stuff and number_of_entries_in_series[entry['name']] != 0:

                                    displayed_name += '<br>Plus ' + str(number_of_entries_in_series[entry['name']] - 1) + ' udvidelse'

                                    if number_of_entries_in_series[entry['name']] > 2:
                                        displayed_name += 'r'
                                        
                                    compress_id = 'name = compressed'
                                    first_entry_stuff = False
                                    i -= 1
                                else:
                                    first_entry_stuff = True
                                    compress_id = 'name = noncompressed'
                                    hide_class = 'hide_entry'


                    # adds more breaks to the displayed name if needed, for alignment of images
                    break_count = displayed_name.count('<br>')
                    while needed_breaks > break_count:
                        displayed_name += '<br>‎ '
                        break_count = displayed_name.count('<br>')
                        

                    # replaces space with underscore for the html file
                    sub_list_ref = entry['series'].replace(' ', '_') + '_' + csv_name

                    # should it download the image or not
                    if download_image or force_download:
                        # replaces space with underscore in the image name
                        img_path = entry['name'].replace(' ', '_')

                        # removes all instances from element of remove_str_list from img_path
                        
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
                    html_file.write(f'\t\t<div class = "grid_entry {hide_class}" {compress_id}>\n\t\t\t<a href = "{sub_list_ref}.html">\n\t\t\t\t<img src = "{img_path}">\n\t\t\t</a>\n\t\t\t<br>\n\t\t\t<a class = "entry_name">\n\t\t\t\t{displayed_name}\n\t\t\t</a>\n\t\t</div>\n')

            # ends html file        
            html_file.write('\t</div>\n</body>')

            print(page_name)


def getAttributes(csv_name: str, dict_key: str) -> set:
    '''
    csv_name: the name of the csv file without .csv
    dict_key: which column of the csv file that will be looked at
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


def getAttributeCount(csv_name: str, dict_key: str) -> dict:
    '''
    csv_name: the name of the csv file without .csv
    dict_key: which column of the csv file that will be looked at
    '''
    with open('CSV/' + csv_name + '.csv') as csv_file:
        csv_dict = csv.DictReader(csv_file, delimiter = ';')
        series_count = defaultdict(int)

        for entry in csv_dict:
            series_count[entry[dict_key]] += 1

    return series_count


# Boardgames
csv_file = 'boardgame'

# makes main boardgame html file
writeHtml('Brætspil', csv_file, needed_breaks = 1, compress_series_entries = True)

# makes a html file for only base games
#writeHtml('Grund Spil', csv_file, html_name = 'base', include = {'base'}, needed_breaks = 1)

# makes a html file for each boardgame series
boardgame_series = getAttributes(csv_file, 'series')[0]
for series in boardgame_series:
    writeHtml(series, csv_file, html_name = series, include = {series}, needed_breaks = 1, compress_series_entries = True, start_compressed = False)


# Books
csv_file = 'books'

# make main book html file
writeHtml('Bøger', csv_file, sort_order_keys = ['series_number', 'series', 'last_name'], displayed_entry_name_keys = ['name', 'break', 'first_name', 'last_name'], exclude = {'Math', 'Digt'}, compress_series_entries = True)

# makes html file for each type of book
book_type = getAttributes(csv_file, 'type')[0]
for series in book_type:
    writeHtml(series, csv_file, html_name = series, sort_order_keys = ['series_number', 'series', 'last_name'], displayed_entry_name_keys = ['name', 'break', 'first_name', 'last_name'], include = {series}, compress_series_entries = True)

# makes html file for each book series
book_series = getAttributes(csv_file, 'series')[0]
for series in book_series:
    writeHtml(series, csv_file, html_name = series, sort_order_keys = ['series_number', 'series', 'last_name'], displayed_entry_name_keys = ['name', 'break', 'first_name', 'last_name'], include = {series}, compress_series_entries = True, start_compressed = False)


# Switch games
csv_file = 'switch'

# make main switch game html
writeHtml('Switch Spil', csv_file, needed_breaks = 1)

# make a html for each switch series
switch_series = getAttributes(csv_file, 'series')[0]
for series in switch_series:
    writeHtml(series, csv_file, html_name = series, include = {series}, needed_breaks = 1)


# LEGO
csv_file = 'lego'

# makes main html file for LEGO
writeHtml('LEGO', csv_file, displayed_entry_name_keys = ['name', 'break', 'number'])

# makes a html file for each LEGO series
lego_series = getAttributes(csv_file, 'series')[0]
for series in lego_series:
    writeHtml(series, csv_file, html_name = series, displayed_entry_name_keys = ['name', 'break', 'number'], include = {series})