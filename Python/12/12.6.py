vocab = {}

with open("vokabel.txt", "r", encoding="ISO-8859-1") as file:
    lines = file.readlines()
    for line in lines:
        words = line.strip().split(';')
        vocab[words[0]] = words[1]


with open("vokabel.xml", "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<Vokabelliste>\n')
    for key, value in vocab.items():
        f.write('\t<Vokabel>\n')
        f.write(f'\t\t<deutsch>{key}</deutsch>\n')
        f.write(f'\t\t<english>{value}</english>\n')
        f.write('\t</Vokabel>\n')
    f.write('</Vokabelliste>\n') 

