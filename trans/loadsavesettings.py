import os, ConfigParser

def SaveSettings(SECTION,NAME,VALUE):
    
    cfg = ConfigParser.ConfigParser()  
    configfile = os.path.join(os.environ.get("HOME", "."), ".tinybldlin")
    sections=["FILES","PIC","WINDOW","OPTIONS","TERMINAL"]
    if not cfg.read(configfile):   
        print "No existe el archivo intentando crear uno nuevo"
        for disp in sections:
            try:
                cfg.add_section(disp) 
                f = open(configfile, "w")  
                cfg.write(f)  
                f.close() 
            except:
                pass
    else:
        try:      
            cfg.set(SECTION, NAME, VALUE) 
            f = open(configfile, "w")  
            cfg.write(f)  
            f.close()    
        except:   
            cfg.add_section(SECTION)
            cfg.set(SECTION, NAME, VALUE) 
            f = open(configfile, "w")  
            cfg.write(f)  
            f.close() 
    return

def GetRestoreSettings(SECTION,NAME):
    cfg = ConfigParser.ConfigParser()  
    configfile = os.path.join(os.environ.get("HOME", "."), ".tinybldlin")
    cfg.read(configfile)  
    VALUE= cfg.get(SECTION, NAME)  
    return VALUE

