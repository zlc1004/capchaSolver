CHECKS=10


from betterClaptcha import Claptcha
import easyocr
from PIL import Image
import random,tqdm
def randomColor():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
def randomString():
    rndLetters = (random.choice("qwertyuiopasdfghjklzxcvbnm1234567890") for _ in range(random.randint(4, 8)))
    return "".join(rndLetters)
reader = easyocr.Reader(['en'],download_enabled=False,recog_network="iter_50000",user_network_directory="./models/net",model_storage_directory="./models/models") # this needs to run only once to load the model into memory
out=""
correct=0
for i in tqdm.tqdm(range(CHECKS)):
    string=randomString()
    c = Claptcha(string, "Consolas.ttf", noise=random.random()/3,lines=random.randint(2,4))#,color=randomColor()
    # c.write(""+string+'.png')
    c.write("./valid/"+string+'.png')
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