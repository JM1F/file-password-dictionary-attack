import zipfile 
from tqdm import tqdm 
import sys

filename = 'secret.zip' 
dictionary = 'dictionary.txt' 
passFound = False

file_to_open = zipfile.ZipFile(filename)
n_words = len(list(open(dictionary, "rb")))
print("Length of Dictionary: ", n_words)
dicAttack = open(dictionary, "rb")

for word in tqdm(dicAttack, total=n_words , unit="word"): 
    try:
        file_to_open.extractall(pwd=word.strip())
    except:
        continue
    else:   
        print("\n Pass Found", word.decode().strip())
        sys.exit(0)

print("Pass not found")
