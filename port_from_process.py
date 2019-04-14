import psutil

procs = list(psutil.process_iter())


for x in procs:
    if x.name()=="UnityPackageManager.exe":
        print(x,"\n------------\n")
        print(x.connections())
    '''
    else :
        print(x)
    '''

