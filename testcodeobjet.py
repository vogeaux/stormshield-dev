


def text ():

    with open("configfile_1.txt", "r+") as f:
        old = f.read()  # read everything in the file
        old = old.replace("SYSTEM", "SYSTEM01")
        old = old.replace("CONFIG", "CONFIG01")
        #f.seek(0)  # rewind
        print(old)
        f.close()
    with open("configfile_2.txt", "w") as f:
        f.write(old)
        f.close()



text()