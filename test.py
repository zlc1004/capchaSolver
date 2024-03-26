from betterClaptcha import Claptcha
import random,tqdm
def randomColor():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
def randomString():
    rndLetters = (random.choice("qwertyuiopasdfghjklzxcvbnm1234567890") for _ in range(random.randint(4, 8)))
    return "".join(rndLetters)
for i in tqdm.tqdm(range(1)):
    string=randomString()
    c = Claptcha(string, "Consolas.ttf",size=(int(200*1.5), int(80*1.5)), noise=random.random()/3,lines=random.randint(1,3),color=randomColor())
    c.write("./valid/"+string+'.png')