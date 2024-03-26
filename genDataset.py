import os
out="filename,words"
for i in os.listdir("/Users/lucaszhang/captchSolver/trainer/all_data/en_train_filtered/"):
    out+="\n"+i+","+i.split(".")[0]
with open("labels.csv","w") as f:
    f.write(out)