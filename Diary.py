import re

#unbearbeitete txt-Datei öffnen und lesen (mode ="r" steht für Lesemodus
file = open('C:/Dokumente/polletti_diary_copy.txt', mode='r', encoding='UTF-8')

text = file.read()

# Text bearbeiten, indem alle Passagen aus dem rohen String entfernt werden die in [...] stehen

new_text = re.sub(r'\[.*?\]', '', text, flags=re.DOTALL)
file.close()

#öffnen der leeren Datei (mode="w" steht für Schreibemodus) und output des neuen Textes in selbige
new_file = open('C:/Dokumente/polletti_diary_output.txt', mode='w', encoding='UTF-8')

new_file.write(new_text)

new_file.close()