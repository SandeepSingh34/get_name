def getfun():
    import os
    ob=open("uni.py",mode="w")
    ob.write("import os")
    ob.write("\n")
    ob.write("try:")
    ob.write("\n")
    ob.write("    ")
    a="import"
    
    ob.write(a)
    ob.write(" ")
    b=input("enter the module name:")
    ob.write(b)
    ob.write("\n")
    ob.write("    ")
    
    
    c="""
    
    n=dir(q)
    ob=open('mym.txt',mode='w')
    ob.write("The module name is :")
    ob.write(" ")
    ob.write(name)
    ob.write("\\n")
    ob.write("These are the function or properties or method of your library")
    ob.write("\\n \\n")
    j=1
    for i in n:
        line_number=str(j)
        ob.write(line_number)
        ob.write(". ")
        ob.write(i)
        ob.write("\\n")
        j=j+1
            
    ob.close()
    """
    q=b
    ob.write("\n")
    
    ob.write("    ")
    
    #ob.write("    ")
    #ob.write("print('module error')")
    
    ob.write("q=")
    ob.write(q)
    ob.write("\n")
    ob.write("    ")
    ob.write("name=' ")
    ob.write(q)
    ob.write(" '")
    ob.write("\n")
    ob.write("    ")
    ob.write(c)
    ob.write("\n")
    ob.write("except Exception:")
    ob.write("\n")
    ob.write("    ")
    ob.write("print('invalid module or packege name ')")
    ob.write("\n")
    ob.write("    ")
    ob.write("print('please wait for checking library....')")
    ob.write("\n")
    ob.write("    ")
    ob.write("print('make sure that your internet should be On for downloading....')")
    ob.write("\n")
    ob.write("    ")
    ob.write("os.system('cmd /k ")
    ob.write(" \" pip install")
    ob.write(" ")
    ob.write(b)
    ob.write(" \" \') ")
    ob.write("\n")
   #ob.write("else:")
   #ob.write("\n")
   #ob.write("    ")
   #ob.write("print('completed ...')")
    ob.close()
    import uni
    print("completed")
    print("ALL  module and function is copied on this path","(",os.getcwd()+"\mym.txt",")")
    
    os.remove("uni.py")
