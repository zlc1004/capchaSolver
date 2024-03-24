import os
out="filename,words"
for i in os.listdir("./imgs"):
    out+="\n"+i+","+i[:-4]
with open("labels.csv","w") as f:
    f.write(out)