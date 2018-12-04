import glob2
import datetime
files = glob2.glob("files/*.txt")
#print(files)
#file name will need to be updated but will be calling it Merged_Files.txt for now
#test =open(files[0],"r")
#print(test.read())
#print(datetime.datetime.now())
date_time = datetime.datetime.now();
# with open(str(date_time) + ".txt","w") as file:
#     for i in files:
#         test = open(i,"r")
#         file.write(test.read()+"\n")
#         test.close()
    #file.write("Stuff and Things")
date_time = datetime.datetime.now();
with open(str(date_time) + ".txt","w") as file:
    for i in files:
        with open(i,"r") as f:
            file.write(f.read() +"\n")
