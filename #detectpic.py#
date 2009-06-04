#!/usr/bin/env python
# -*- coding: utf-8 -*-

try: 
    import serial 
    
except ImportError:
    
    raise ImportError,"Se requiere el modulo python-serial"

import wx
from pictype import PicType
from taskbaricon import ChangeTaskBarIcon

def CheckConection(WxTbl):
    PORT= WxTbl.port.GetValue()
    BAUD=int(WxTbl.combo_box_speed.GetValue())
    
    try:
        ser = serial.Serial(PORT,BAUD,timeout=0.1)
        ser.close()
        WxTbl.messages.AppendText("\n\n Connected to " + PORT + " at " + str(BAUD))
        return 1
        
    except:
        WxTbl.messages.AppendText("\n Could not connect to " + PORT + " at " + str(BAUD))
        return 0


def CheckPic(WxTbl):
    
    WxTbl.abortsearchbutton.Show() 
        
    WxTbl.main_gauge.SetValue(0)
    
    PORT= WxTbl.port.GetValue()
        
    BAUD=int(WxTbl.combo_box_speed.GetValue())

    WxTbl.messages.AppendText('\n Searching for PIC ...')
    
    type=None
    max_flash=None
    family=None
    
    try:
        #OpenPort
        ser = serial.Serial(PORT,BAUD,timeout=0.03)
        ChangeTaskBarIcon(WxTbl,'yellow')
        
        #Since we are lazy there will be a lot of chance to press reset           
        #Ask for PIC IDE several times
        
        for i in range(0,99,1):
            #Give wxpython chance to update main gauge
            wx.Yield()
            #decrease gauge
            WxTbl.main_gauge.SetValue(100-i)
            
            #Ask IDE
            ser.write(chr(0xC1))
          
            #wait for PIC answer
            ret=ser.read(2)
            
            
            #If pic send 2 bytes lets check what sends
            if len(ret)==2:
                break
            
            if WxTbl.wantabort==1:
                WxTbl.wantabort=0
                WxTbl.abortsearchbutton.Hide() 
                break

    except:
       
        #If port cant be open
        WxTbl.abortsearchbutton.Hide() 
        WxTbl.messages.AppendText("\n Could not connect to " + PORT + " at " + str(BAUD) + '\n ERROR!')
        return type,max_flash,family
    
    WxTbl.abortsearchbutton.Hide() 
    
    #closing serial port
    
    ser.close()
    #clear main gauge
    WxTbl.main_gauge.SetValue(0)
    
    #In case there was no answer from pic
    if len(ret)!=2:
        WxTbl.messages.AppendText('Not found, \n ERROR!')
        return type,max_flash,family
   
        
    #In case of pic not recognized
    if ret[1]!= "K":
        WxTbl.messages.AppendText("\n Error, PIC not recognized (protocol error)\n")
        return type,max_flash,family 
        
    pt=ord(ret[0])
        
    type, max_flash, family=PicType(pt)
    WxTbl.messages.AppendText('\n Found:'+ type)
    return type,max_flash,family
    
