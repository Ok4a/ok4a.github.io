import csv, requests

from pathlib import Path

csv_file = "boardgame"
with open(csv_file + '.csv') as csv_file:
       csv_reader = csv.reader(csv_file, delimiter = ';')

       for row in csv_reader:
            # print(row[1])
            img_data = requests.get(row[1]).content

            img_name = row[0]
            if ' ' in img_name:
                img_name = img_name.replace(' ', '_')

            remove_str = ['<br>', ':', '?', ',', '!', "'"]
            for s in remove_str:
                if s in img_name:
                    img_name = img_name.replace(s , '')   

            img_name = 'imgTest/'+img_name+'.jpg'

            img_path = Path(img_name)
            if  not img_path.is_file():
                print(img_path)
                with open(img_name, 'wb') as handler:
                    handler.write(img_data)