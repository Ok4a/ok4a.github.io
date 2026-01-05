from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Dict
from csv import DictReader
import requests, pathlib, os



@dataclass(order = True)
class seriesData:
    '''
    Docstring for seriesData

    :param name: name of the series
    :param entries: list of entries in the series
    :param count: number of entries in the series
    :param subSeries: dict of seriesData
    :param sub: is it a subseries
    '''
    name: str
    # type: str = field(compare = False)
    entries: list = field(default_factory = list, compare = False, repr = True)
    count: int = field(default = 0, compare = False)
    subSeries: dict = field(default_factory = dict, compare = False)
    sub: bool = field(default = False, compare = False)

    
    def __len__(self) -> int: 
  
        return self.count

    def addEntry(self, entry: baseData) -> None: # add an entry to the series

        self.count += 1
        self.entries.append(entry)
        self.entries.sort()

    

@dataclass
class baseData:

    name: str
    img: str = field(compare = False, repr = False)
    series: seriesData = field(compare = False)
    type: str = field(compare = False)
    # dataType: str = field(compare = False)


    def __repr__(self) -> str:

        return f'D({self.name})'
    
    def isFirst(self):
        pass

    def isPartOfSubSeries(self) -> bool:
        pass

    def hasImage(self) -> bool:
        return self.img != ''
    
    def getNumber(self) -> int | None:
        try:
            return self.number
        except:
            return None
        
    def getType(self):
        try:
            return self.type
        except:
            return ''

    def ref(self):
 
        string = f'{self.series.name}_{self.dataType}'

        return f'{cleanStr(string)}.html'

    def getImg(self, download: bool) -> str:

        if download:
            img_folder = f'list_img/{self.dataType}'
            if not os.path.exists(img_folder):
                os.makedirs(img_folder)

            tempNum = f'_{self.getNumber()}' if self.getNumber() is not None else ''

            imgFileName = f'{img_folder}/{cleanStr(self.name)}{tempNum}_{self.getType()}.jpg'

            if not pathlib.Path(imgFileName).is_file() and self.hasImage():
                img_data = requests.get(self.img).content
                with open(imgFileName, mode = 'wb') as imgFile:
                    imgFile.write(img_data)

            return f'../{imgFileName}'
        else:
            return self.img

            


        
 

# @validate_call
@dataclass(order = True)
class bookData(baseData):
    name: str = field(compare = False)
    first: str = field(compare = False)
    last: str
    number: int
    subSeries: seriesData | None = field(default = None, repr = False)
    dataType: str = field(default = 'books', compare = False)

    def __repr__(self) -> str:
        return f"D({self.name} {self.number})"
    
    def isPartOfSubSeries(self) -> bool:
        return self.subSeries is not None
    
    def displayedName(self, compress: bool) -> str:
        string = colonBreak(self.name)
        

        if self.isPartOfSubSeries():
            if len(self.subSeries) > 1 or self.getType() == "Manga":
                string = breakAfter(string, 1)
                string += f'<br>\n\t\t\t\t# {self.number}'
                if compress and len(self.subSeries):
                    string += f' - {self.subSeries.entries[-1].number}'
        else:

            if len(self.series) > 1 or self.getType() == "Manga":
                string = breakAfter(string, 1)
                string += f'<br>\n\t\t\t\t# {self.number}'
                if compress and len(self.series) > 1:
                    string += f' - {self.series.entries[-1].number}'

        

        string = breakAfter(string, 2)
        string += f'<br>{self.first} {self.last}'

        return string
    
    def isFirst(self) -> bool:
        return self.number == self.series.entries[0].number

def createBookData(entry: dict, series: list[seriesData]) -> bookData:
    return bookData(name = entry['name'], first = entry['first_name'], last = entry['last_name'], series = series[0], subSeries = series[1], number = entry['series_number'], img = entry['image'], type = entry['type'])


@dataclass(order = True)
class legoData(baseData):
    number: int = field(compare = False)
    dataType: str = field(default = 'lego', compare = False)

    def __repr__(self) -> str:
        return f'D({self.name} {self.number})'
    
    def displayedName(self, compress: bool) -> str:
        return f'{self.name} <br>\n\t\t\t\t{self.number}'
    
def createLegoData(entry:dict, series: list[seriesData]):
    return legoData(name = entry['name'], number = entry['number'], series = series[0], img = entry['image'], type = entry['type'])
    

@dataclass(order = True)
class switchData(baseData):
    series: seriesData = field(compare = False)
    dataType: str = field(default = 'switch', compare = False)

    
    def displayedName(self, compress: bool) -> str:
        string = colonBreak(self.name)
        if string.count('<br>') < 1:
            string += '<br /><br />'
        return string

def createSwitchData(entry, series):
    return switchData(name = entry['name'], series = series[0], type = entry['type'], img = entry['image'])
    
@dataclass(order = True)
class boardgameData(baseData):
    name: str
    series: seriesData = field(compare = True)
    type: str = field(compare = False)
    img: str = field(compare = False, repr = False)
    subSeries: seriesData | None = field(default = None, repr = False)
    dataType: str = field(default = 'boardgame', compare = False)

    def isPartOfSubSeries(self) -> bool:
        return self.subSeries is not None
    
    def isBase(self) -> bool:
        return self.type == 'base'
    
    def isFirst(self) -> bool:
        return self.isBase()
    
    def displayedName(self, compress: bool) -> str:
        string = colonBreak(self.name)
        
        if compress and self.isPartOfSubSeries() and self.isBase():
            string += f'<br>Plus {len(self.subSeries)-1} udvidelse'
            if len(self.subSeries) > 2:
                string += 'r'
                


        string = breakAfter(string, 3)

        return string
    

def createBoardgameData(entry: dict, series: tuple[seriesData]) -> boardgameData:
    return boardgameData(name = entry['name'], series =series[0], subSeries = series[1], type = entry['type'],img =entry['image'])



def loadData(csv:str, createFun: function) -> tuple[list]:
    series = dict()
    entries = list()

    with open(f'CSV/{csv}.csv', mode = 'r') as csv_file:
        csv_dict = DictReader(csv_file, delimiter = ';')
        for entry in csv_dict:
            seriesName = entry['series']

            if seriesName not in series.keys():
                seri = seriesData(seriesName)
                series[seriesName] = seri
            else:
                seri = series[seriesName]

            # is the entry part of a sub series
            subSeries = None
            if 'sub_series' in entry.keys():
                if entry['sub_series'] != '':
                    subSeriesName = entry['sub_series']

                    # has the sub series been seen before
                    if subSeriesName not in seri.subSeries.keys():
                        subSeries = seriesData(subSeriesName, sub = True)
                        seri.subSeries[subSeriesName] = subSeries
                    else:
                        subSeries = seri.subSeries[subSeriesName]
                    

            ent = createFun(entry, (seri, subSeries))
            
            entries.append(ent)
            seri.addEntry(ent)

            if 'sub_series' in entry.keys() and entry['sub_series'] != '':
                subSeries.addEntry(ent)


    return list(series.values()), entries




def writeHTML(data: list[baseData], pageName: str, HTMLName: str = None, start_compressed: bool = False, compress_series_entries: bool = False):

    startString = '<!DOCTYPE html>\n<html lang = "en" dir = "ltr">\n<link rel = "stylesheet" href = "../style.css">\n<head>\n\t<meta charset = "utf-8" name = "viewport" content = "width = device-width, initial-scale = 0.6">\n</head>\n\n'
    sideBarString = f'\t<script>\n\t\tcompressed_entries = {str(compress_series_entries).lower()};\n\t\tuncompress_on_load = {str(not start_compressed).lower()};\n\t</script>\n\t<script src = "../sidebar.js"></script>\n'

    HTMLName = pageName if HTMLName is None else HTMLName
    is_first_entry = True
    hide_class = ''

    data.sort()
    with open(f'html_lists/{cleanStr(HTMLName)}.html', mode = 'w', encoding = 'utf-8') as HTMLFile:
        HTMLFile.write(f'{startString}<title>{pageName}</title>\n\n<body>\n{sideBarString}\t<div class = "top_bar">\n\t\t<h1>{pageName}</h1>\n\t</div>\n\t<div class = "grid">\n')
        compress_id = ''

        i = 0
        while i < len(data):
            entry: baseData = data[i]
            i += 1

            if is_first_entry and entry.isFirst():
                displayed_name = entry.displayedName(compress = True)
                is_first_entry = False
                hide_class = ''
                compress_id = 'name = compressed'
                i -= 1
            else:
                displayed_name = entry.displayedName(compress = False)
                is_first_entry = True
                compress_id = 'name = noncompressed'
                hide_class = ' hide_entry'


            HTMLFile.write(f'\t\t<div class = "grid_entry{hide_class}" {compress_id}>\n\t\t\t<a href = "{entry.ref()}">\n\t\t\t\t<img src = "{entry.getImg(True)}" title = "{entry.name.replace("<br>", "") }">\n\t\t\t</a>\n\t\t\t<br>\n\t\t\t<a class = "entry_name">\n\t\t\t\t{displayed_name}\n\t\t\t</a>\n\t\t</div>\n')




def colonBreak(string: str) -> str:
    return string.replace(':', ': <br>')

def breakAfter(string:str, minimum: int) -> str:
    count = string.count('<br>') + string.count('<br />')
    if  count < minimum:
        for _ in range(minimum-count):
            string += "<br />"


    return string


def cleanStr(string:str) -> str:
    string = string.replace(' ', '_')
    for s in {'<br>', ':', '?', ',', '!', "'", '.', '-'}:
        string = string.replace(s, '')
    return string