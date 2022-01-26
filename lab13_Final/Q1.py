import os

f = open('myfile.txt', 'w')
f.write('\N{HANGUL SYLLABLE TAEG}')
f.close()

print(os.stat('myfile.txt').st_size)