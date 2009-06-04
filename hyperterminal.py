import wx,serial,nonascii




def OpenTerminal(WxTbl):
    
    WxTbl.terminal.Enable(1)
    WxTbl.closeterminalbutton.Enable(1)
    WxTbl.openterminalbutton.Enable(0)
    WxTbl.combo_box_speed_terminal.Enable(0)
    
    PORT=WxTbl.port.GetValue()
    BAUD=int(WxTbl.combo_box_speed_terminal.GetValue())
    
    try:
        global s    
        s = serial.Serial(PORT, BAUD)
        s.timeout=0.1
        
    except:
        print 'Could not connect'
        return
    WxTbl.fin=0
    WxTbl.tf=1
    reader(WxTbl)
    WxTbl.tf=0
    s.close()
    
    WxTbl.terminal.Enable(0)
    WxTbl.closeterminalbutton.Enable(0)
    WxTbl.openterminalbutton.Enable(1)
    WxTbl.combo_box_speed_terminal.Enable(1)
    
def reader(WxTbl):
    
      
    WxTbl.read=1
   
    while not(WxTbl.fin):
       
        wx.Yield()
        data = s.read(1)
      
        if len(data) != 0:
            WriteTerminal(WxTbl,data)
   
    WxTbl.read=0
    return
    
def WriteTerminal(WxTbl,rx):
    
    asciicode=ord(rx)
    
    if asciicode<128:
        WxTbl.terminal.AppendText(chr(asciicode))
        return
    
    else:
        na=nonascii.NonAscii(WxTbl,asciicode)
        WxTbl.terminal.AppendText(na)

    
def SendData(WxTbl,code):
    
    PORT=WxTbl.port.GetValue()
    BAUD=int(WxTbl.combo_box_speed_terminal.GetValue())
    
    
    try:
        s = serial.Serial(PORT, BAUD)
        s.timeout=0.1
        s.write(chr(code))
   
    except:
        print ord(code)
        
    type=WxTbl.combo_box_tx_type.GetValue()
    
    if type=='TypEcho':
            
        try:
            WxTbl.terminal.AppendText(chr(code))
        except:
            na=nonascii.NonAscii(WxTbl,code)
            WxTbl.terminal.AppendText(na)
            
    return
        
def SendTxData(WxTbl,txdata):
    
    PORT=WxTbl.port.GetValue()
    BAUD=int(WxTbl.combo_box_speed_terminal.GetValue())
    
    try:
        s = serial.Serial(PORT, BAUD)
        s.timeout=0.1
        s.write(str(txdata))
   
    except:
        print ord(code)
    
     
def ChangeDisplay(WxTbl):
    dump=WxTbl.terminal.GetValue()
    WxTbl.terminal.Clear()
    i=0
    type=WxTbl.combo_box_rx_type.GetValue()

    if type=='Hex':
        
        for disp in dump:
            hexa=hex(ord(disp))
            
            if hexa=='0xd':
                WxTbl.terminal.WriteText('0d ')
                
            elif hexa=='0xa':
                WxTbl.terminal.WriteText('0a ')
                
            elif hexa=='0xf':
                WxTbl.terminal.WriteText('ff ')
             
            else:   
                WxTbl.terminal.WriteText(str(hexa)[2:4]+' ')
            
    if type=='Char':
        
        le=len(dump)/3
        for j in range(0,le,1):
            try:
                datachar=chr(eval('0x'+(dump[0+i:2+i])))
                WxTbl.terminal.WriteText(datachar)
            except:
                
                WxTbl.terminal.WriteText('?')
                
            i=i+3
    return 