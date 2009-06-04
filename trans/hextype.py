

def gethextype(filename):

    try:
            f=open(filename, 'r')
    except IOError:
            message="Can't open file:"+filename+"\n\n"
            return None
        
    hexfile=f.readlines()
    f.close()
    le=len(hexfile)
    
    for rec in hexfile:
        print rec      