from claptcha import Claptcha
from PIL import Image
import random,tqdm
def randomColor():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    # return(255,255,255)
def randomString():
    rndLetters = (random.choice("qwertyuiopasdfghjklzxcvbnm1234567890") for _ in range(random.randint(4, 8)))
    return "".join(rndLetters)

for i in tqdm.tqdm(range(10000)):
    string=randomString()
    int1=random.randint(1,3)
    for k in range(int1):
        c = Claptcha(string, "Consolas.ttf",size=(int(200*1), int(80*1)), noise=random.random()/3,lines=random.randint(1,2),color=randomColor())
        c.write("/Users/lucaszhang/captchSolver/trainer/all_data/en_train_filtered/"+string+'.'+str(k)+'.png')