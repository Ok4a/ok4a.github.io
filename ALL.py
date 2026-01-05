from util import *
# v 4.0.0


csv_name = 'LEGO'
Ser, Ent = loadData(csv_name, createFun = createLegoData)
writeHTML(Ent, csv_name, csv_name)

for series in Ser:
    writeHTML(series.entries, series.name, f'{series.name}_{csv_name}')

csv_name = 'switch'
Ser, Ent = loadData(csv_name, createFun = createSwitchData)
writeHTML(Ent, csv_name, csv_name)
for series in Ser:
    writeHTML(series.entries, series.name, f'{series.name}_{csv_name}')



csv_name = 'boardgame'
Ser, Ent = loadData(csv_name, createFun = createBoardgameData)
writeHTML(Ent, 'Brætspil', csv_name, compress_series_entries = True, start_compressed = True)
for series in Ser:
    writeHTML(series.entries, series.name, f'{series.name}_{csv_name}', compress_series_entries = True)


csv_name = 'books'
Ser, Ent = loadData(csv_name, createFun = createBookData)
writeHTML(Ent, 'Bøger', csv_name, compress_series_entries = True, start_compressed = True)
for series in Ser:
    writeHTML(series.entries, series.name, f'{series.name}_{csv_name}', compress_series_entries = True)
