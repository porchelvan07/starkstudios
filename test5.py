import os
path="/home/porchy/Downloads/anydesk-5.5.1/"
FList=[]
def init():  
    for File in os.listdir(path):
        if File.find('.run')>0 and os.path.isfile(path+File):
            FList.append(File)
            #FList.sort()
    print(FList[1]+" "+FList[3] )
    
    if FList[1]>FList[3]:
        print ("Greater")
    else:
        print ("Smaller")
        
    print (os.getcwd())
    print ("Error Occured")
init() 
