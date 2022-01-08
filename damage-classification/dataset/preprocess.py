import csv
import os
import shutil

file = open('raw/index.csv', 'r')
csvreader = csv.reader(file)

classes = []
content_list = []
for index, row in enumerate(csvreader):
    if row[1] not in classes:
        if index is not 0:
            content_list.append(row)
            try:
                os.mkdir('final/' + row[1])
            except FileExistsError:
                pass

for content in content_list:
    print(os.path.join(f'raw', content[0]), os.path.join(f'final/{content[1]}', content[0].split('/')[-1]))
    shutil.copy(os.path.join(f'raw', content[0]), os.path.join(f'final/{content[1]}', content[0].split('/')[-1]))