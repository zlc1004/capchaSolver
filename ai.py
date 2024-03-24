from claptcha import Claptcha
import easyocr
from PIL import Image
import random,tqdm
def randomString():
    rndLetters = (random.choice("qwertyuiopasdfghjklzxcvbnm1234567890") for _ in range(5))
    return "".join(rndLetters)
reader = easyocr.Reader(['en'],recog_network="iter_10000") # this needs to run only once to load the model into memory
out=""
for i in tqdm.tqdm(range(10)):
    for i in (range(1)):
        string=randomString()
        c = Claptcha(string, "Consolas.ttf", noise=0.1)
        # c.write(""+string+'.png')
        c.write("./valid/"+string+'.png')
    result = reader.readtext("./valid/"+string+'.png')
    out+=(result[0][1])
    out+="\t"
    out+=(string)
    out+="\n"
print(out)