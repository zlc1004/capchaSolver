from claptcha import Claptcha
from PIL import Image
import random,tqdm
def randomString():
    rndLetters = (random.choice("qwertyuiopasdfghjklzxcvbnm1234567890") for _ in range(random.randint(4, 8)))
    return "".join(rndLetters)

for i in tqdm.tqdm(range(10000)):
    string=randomString()
    c = Claptcha(string, "Consolas.ttf", noise=random.random()/3)
    # c.write(""+string+'.png')
    c.write("/Users/lucaszhang/captchSolver/trainer/all_data/en_train_filtered/"+string+'.png')