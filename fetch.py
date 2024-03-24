from claptcha import Claptcha
from PIL import Image
import random,tqdm
def randomString():
    rndLetters = (random.choice("qwertyuiopasdfghjklzxcvbnm1234567890") for _ in range(5))
    return "".join(rndLetters)

for i in tqdm.tqdm(range(10000)):
    string=randomString()
    c = Claptcha(string, "Consolas.ttf", noise=0.1)
    # c.write(""+string+'.png')
    c.write("./imgs/"+string+'.png')