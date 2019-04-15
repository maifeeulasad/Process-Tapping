import psutil

procs = list(psutil.process_iter())

data=dict()

for x in procs:
    if x.name()=="UnityPackageManager.exe":
        for y in x.connections():
            print(y.laddr.ip)
            print(y.laddr.port)
            data[y.laddr.ip]=y.laddr.port
        break


print(data)
