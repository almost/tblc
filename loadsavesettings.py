import wx,os, ConfigParser, taskbaricon

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

def OnInit(WxTbl):
    WxTbl.tbicon = wx.TaskBarIcon() 
    taskbaricon.ChangeTaskBarIcon(WxTbl,'blue')

    cfg = ConfigParser.ConfigParser()
    configfile = os.path.join(os.environ.get("HOME", "."), ".tinybldlin")
     
    if not cfg.read(configfile):  
        print "No config file" 
        return  
        
    #Getting Saved and restoring Values
    if cfg.has_option("WINDOW", "top") and cfg.has_option("WINDOW", "left"):
        Top=int(GetRestoreSettings('WINDOW','top'))
        Left=int(GetRestoreSettings('WINDOW','left'))
        WxTbl.SetPosition((Top,Left))
    
    if cfg.has_option("WINDOW", "height") and cfg.has_option("WINDOW", "width"):
        Height=int(GetRestoreSettings('WINDOW','height'))
        Width=int(GetRestoreSettings('WINDOW','width'))
        WxTbl.SetSize((Width,Height))
    
    if cfg.has_option("FILES", "hexfile"): 
        HexFile=GetRestoreSettings('FILES','hexfile')
        WxTbl.combo_box_hex.SetValue(HexFile)
    
    if cfg.has_option("PIC", "comspeed"): 
        COMspeed=GetRestoreSettings('PIC','comspeed')
        WxTbl.combo_box_speed.SetValue(COMspeed)
    
    if cfg.has_option("TERMINAL", "termspeed"):
        TERMspeed=GetRestoreSettings('TERMINAL','termspeed')
        WxTbl.combo_box_speed_terminal.SetValue(TERMspeed)
        
    if cfg.has_option("PIC", "comport"):
        COMport=GetRestoreSettings('PIC','comport')
        WxTbl.port.SetValue(COMport)

   

def OnClose(WxTbl):
        

    #seving Settings
    try:        
        SaveSettings('FILES','HexFile',WxTbl.combo_box_hex.GetValue())
        SaveSettings('PIC','COMport',WxTbl.port.GetValue())
        SaveSettings('PIC',"COMspeed",WxTbl.combo_box_speed.GetValue())
        SaveSettings('TERMINAL',"TERMspeed",WxTbl.combo_box_speed_terminal.GetValue())
        Width,Height=WxTbl.GetSize()
        SaveSettings('WINDOW',"Width",Width)
        SaveSettings('WINDOW',"Height",Height)
        Top,Left=WxTbl.GetPosition()
        SaveSettings('WINDOW',"Top",Top)
        SaveSettings('WINDOW',"Left",Left)
  
    except:
        print 'there was an error savig settings'
    WxTbl.Destroy()