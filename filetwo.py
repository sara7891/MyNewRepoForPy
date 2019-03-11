import fileone 
print("top level in filetwo.py")

fileone.func()

if __name__=="__main__":
    print("two.py is bring execute directly")
else:
    print("filetwo.py is being imported into anoter module")
