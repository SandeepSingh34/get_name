import os
try:
    import numpy
    
    q=numpy
    name=' numpy '
    

    n=dir(q)
    ob=open('mym.txt',mode='w')
    ob.write("The module name is :")
    ob.write(" ")
    ob.write(name)
    ob.write("\n")
    ob.write("These are the function or properties or method of your library")
    ob.write("\n \n")
    j=1
    for i in n:
        line_number=str(j)
        ob.write(line_number)
        ob.write(". ")
        ob.write(i)
        ob.write("\n")
        j=j+1
        
    ob.close()

except Exception:
    print('invalid module or packege name ')
    print('please wait for checking library....')
    print('make sure that your internet should be On for downloading....')
    os.system('cmd /k  " pip install numpy " ') 
else:
    print('completed ...')