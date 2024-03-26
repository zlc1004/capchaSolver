CHECKS=100

from betterClaptcha import Claptcha
import easyocr
from PIL import Image
import random,tqdm
def randomColor():
    # return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return (255,255,255)
def randomString():
    rndLetters = (random.choice("qwertyuiopasdfghjklzxcvbnm1234567890") for _ in range(random.randint(4, 8)))
    return "".join(rndLetters)
reader = easyocr.Reader(['en'],download_enabled=False,recog_network="iter_50000",user_network_directory="./models/net",model_storage_directory="./models/models") # this needs to run only once to load the model into memory
out=""
correct=0
for i in tqdm.tqdm(range(CHECKS)):
    string=randomString()
    c = Claptcha(string, "Consolas.ttf",size=(int(200*1.25), int(80*1.25)), noise=random.random()/3,lines=random.randint(1,3),color=randomColor())
    # c.write(""+string+'.png')
    c.write("./valid/"+string+'.png')
    # Image.open("./valid/"+string+'.png').convert('L').convert('RGB').save("./valid/"+string+'.gray.png')
    result = reader.readtext("./valid/"+string+'.png')
    try:
        text = result[0][1]
    except IndexError:
        text="error"
        print(result)
    out+=text
    out+="\t"
    out+=(string)
    out+="\t"
    out+=str(string==text)
    out+="\n"
    if string==text:
        correct+=1
print(out)
print("Accuracy: ",(correct/CHECKS)*100,"%")