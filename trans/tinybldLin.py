#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

# generated by wxGlade 0.6.3 on Sun Jan  4 01:18:48 2009 from "/home/fjv/Python/TinyBldLin/src/TinyBldLin.wxg"

try: 
    import wx 
except ImportError:
    raise ImportError,"Se requiere el modulo wxPython"

# begin wxGlade: extracode
# end wxGlade

import os,serial,time



from loadsavesettings import GetRestoreSettings
from loadsavesettings import SaveSettings
from checkpic import checkserial
from checkpic import detectpic
from searchserial import searchserial
from chunkhexfile import chunkhexfile
from chunkhexfile import chunkhexfile_config


from hexage import gethexage

from nonascii import nonascii

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.Tabs = wx.Notebook(self, -1, style=0)
        self.terminal_tab = wx.Panel(self.Tabs, -1)
        self.messages_tab = wx.Panel(self.Tabs, -1)
        self.sizer_3_staticbox = wx.StaticBox(self, -1, "Comm")
        self.sizer_8_staticbox = wx.StaticBox(self.terminal_tab, -1, "")
        self.sizer_4_staticbox = wx.StaticBox(self.terminal_tab, -1, "")
        self.sizer_5_staticbox = wx.StaticBox(self.terminal_tab, -1, "")
        self.sizer_6_staticbox = wx.StaticBox(self.terminal_tab, -1, "")
        self.sizer_2_staticbox = wx.StaticBox(self, -1, "")
        self.combo_box_hex = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.browsebutton = wx.Button(self, -1, "&Browse")
        self.writeflashbutton = wx.Button(self, -1, "&Write Flash")
        self.checkpicbutton = wx.Button(self, -1, "&CheckPic")
        self.abortsearchbutton = wx.Button(self, -1, "Abort Search")
        self.main_gauge = wx.Gauge(self, -1, 100, style=wx.GA_HORIZONTAL|wx.GA_SMOOTH)
        self.combo_box_speed = wx.ComboBox(self, -1, choices=["115200", "57600", "38400", "19200", "9600"], style=wx.CB_DROPDOWN)
        self.searchportbutton = wx.Button(self, -1, "Search")
        self.port = wx.TextCtrl(self, -1, "")
        self.list_ports = wx.ListBox(self, -1, choices=[], style=wx.LB_SINGLE)
        self.messages = wx.TextCtrl(self.messages_tab, -1, "Interface to TinyBootLoader\ncontact: claudiu.chiculita@ugal.ro\nhttp://www.etc.ugal.ro/cchiculita/software/picbootloader.htm\nfor GNU/Linux version:\ncontact:ferezvi@gmail.com\nhttp://fjv.awardspace.com\n--------------------------------------------------------------------------------------------------\n", style=wx.TE_MULTILINE)
        self.openterminalbutton = wx.Button(self.terminal_tab, -1, "&Open")
        self.closeterminalbutton = wx.Button(self.terminal_tab, -1, "&Close")
        self.combo_box_speed_terminal = wx.ComboBox(self.terminal_tab, -1, choices=["115200", "57600", "38400", "19200", "9600"], style=wx.CB_DROPDOWN)
        self.clearterminalbutton = wx.Button(self.terminal_tab, -1, "&Clear")
        self.label_1_copy = wx.StaticText(self.terminal_tab, -1, "Tx ")
        self.combo_box_tx_type = wx.ComboBox(self.terminal_tab, -1, choices=["Char", "Char\\", "Type", "TypEcho"], style=wx.CB_DROPDOWN)
        self.combo_box_tx_data = wx.ComboBox(self.terminal_tab, -1, choices=[], style=wx.CB_DROPDOWN)
        self.sendataterminalbutton = wx.Button(self.terminal_tab, -1, "Send")
        self.button_12 = wx.Button(self.terminal_tab, -1, "&1")
        self.button_13 = wx.Button(self.terminal_tab, -1, "&2")
        self.button_14 = wx.Button(self.terminal_tab, -1, "&3")
        self.label_1 = wx.StaticText(self.terminal_tab, -1, "Rx ")
        self.combo_box_rx_type = wx.ComboBox(self.terminal_tab, -1, choices=["Char", "Hex"], style=wx.CB_DROPDOWN)
        self.combo_box_terminal_log = wx.ComboBox(self.terminal_tab, -1, choices=["dump.bin"], style=wx.CB_DROPDOWN)
        self.button_15 = wx.Button(self.terminal_tab, -1, "&B")
        self.button_16 = wx.Button(self.terminal_tab, -1, "&H")
        self.button_17 = wx.Button(self.terminal_tab, -1, "&R")
        self.terminal = wx.TextCtrl(self.terminal_tab, -1, "", style=wx.TE_PROCESS_ENTER|wx.TE_MULTILINE|wx.TE_RICH|wx.TE_RICH2|wx.TE_LINEWRAP|wx.TE_WORDWRAP)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.browsefile, self.browsebutton)
        self.Bind(wx.EVT_BUTTON, self.writeflash, self.writeflashbutton)
        self.Bind(wx.EVT_BUTTON, self.checkpic, self.checkpicbutton)
        self.Bind(wx.EVT_BUTTON, self.abortsearch, self.abortsearchbutton)
        self.Bind(wx.EVT_BUTTON, self.searchport, self.searchportbutton)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.listboxdclick, self.list_ports)
        self.Bind(wx.EVT_BUTTON, self.openterminal, self.openterminalbutton)
        self.Bind(wx.EVT_BUTTON, self.closeterminal, self.closeterminalbutton)
        self.Bind(wx.EVT_BUTTON, self.clearterminal, self.clearterminalbutton)
        self.Bind(wx.EVT_COMBOBOX, self.TxType, self.combo_box_tx_type)
        self.Bind(wx.EVT_BUTTON, self.sendataterminal, self.sendataterminalbutton)
        self.Bind(wx.EVT_BUTTON, self.ononebutton, self.button_12)
        self.Bind(wx.EVT_BUTTON, self.ontwobutton, self.button_13)
        self.Bind(wx.EVT_BUTTON, self.onthreebutton, self.button_14)
        self.Bind(wx.EVT_COMBOBOX, self.TerminalDisplay, self.combo_box_rx_type)
        self.Bind(wx.EVT_BUTTON, self.onbbutton, self.button_15)
        self.Bind(wx.EVT_BUTTON, self.onhbutton, self.button_16)
        self.Bind(wx.EVT_BUTTON, self.onrbutton, self.button_17)
        self.Bind(wx.EVT_TEXT_ENTER, self.ontextenterterminal, self.terminal)
        # end wxGlade
        self.Bind(wx.EVT_CLOSE, self.onclosebutton) 
        self.terminal.Bind(wx.EVT_CHAR, self.EvtChar)
        self.timer = wx.Timer(self)

        self.Bind(wx.EVT_TIMER, self.OnTimer,self.timer)


    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("WxPython Tiny Pic Bootloader")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("/usr/share/tinybldLin/_tinybldLin/images/blue.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((728, 411))
        self.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.abortsearchbutton.SetMinSize((90, 30))
        self.abortsearchbutton.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.abortsearchbutton.Hide()
        self.main_gauge.SetMinSize(wx.DLG_SZE(self.main_gauge, (45, 8)))
        self.combo_box_speed.SetMinSize(wx.DLG_SZE(self.combo_box_speed, (45, 13)))
        self.combo_box_speed.SetSelection(0)
        self.port.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.list_ports.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.list_ports.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.messages.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.openterminalbutton.SetMinSize(wx.DLG_SZE(self.openterminalbutton, (41, 16)))
        self.closeterminalbutton.SetMinSize(wx.DLG_SZE(self.closeterminalbutton, (35, 16)))
        self.closeterminalbutton.Enable(False)
        self.combo_box_speed_terminal.SetMinSize(wx.DLG_SZE(self.combo_box_speed_terminal, (44, 16)))
        self.combo_box_speed_terminal.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.combo_box_speed_terminal.SetSelection(0)
        self.clearterminalbutton.SetMinSize(wx.DLG_SZE(self.clearterminalbutton, (35, 16)))
        self.label_1_copy.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.combo_box_tx_type.SetMinSize(wx.DLG_SZE(self.combo_box_tx_type, (38, 13)))
        self.combo_box_tx_type.SetSelection(1)
        self.combo_box_tx_data.SetMinSize(wx.DLG_SZE(self.combo_box_tx_data, (60, 13)))
        self.sendataterminalbutton.SetMinSize(wx.DLG_SZE(self.sendataterminalbutton, (30, 13)))
        self.button_12.SetMinSize(wx.DLG_SZE(self.button_12, (10, 16)))
        self.button_12.Enable(False)
        self.button_13.SetMinSize(wx.DLG_SZE(self.button_13, (10, 16)))
        self.button_13.Enable(False)
        self.button_14.SetMinSize(wx.DLG_SZE(self.button_14, (10, 16)))
        self.button_14.Enable(False)
        self.label_1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.combo_box_rx_type.SetMinSize(wx.DLG_SZE(self.combo_box_rx_type, (38, 13)))
        self.combo_box_rx_type.SetSelection(0)
        self.combo_box_terminal_log.SetMinSize(wx.DLG_SZE(self.combo_box_terminal_log, (45, 13)))
        self.combo_box_terminal_log.Enable(False)
        self.combo_box_terminal_log.SetSelection(0)
        self.button_15.SetMinSize(wx.DLG_SZE(self.button_15, (11, 16)))
        self.button_15.Enable(False)
        self.button_16.SetMinSize(wx.DLG_SZE(self.button_16, (11, 16)))
        self.button_16.Enable(False)
        self.button_17.SetMinSize(wx.DLG_SZE(self.button_17, (11, 16)))
        self.button_17.Enable(False)
        self.terminal.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer_3 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_8 = wx.FlexGridSizer(2, 1, 0, 0)
        sizer_6 = wx.StaticBoxSizer(self.sizer_6_staticbox, wx.HORIZONTAL)
        grid_sizer_14 = wx.FlexGridSizer(1, 1, 0, 0)
        grid_sizer_9 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_11 = wx.FlexGridSizer(2, 1, 0, 0)
        sizer_5 = wx.StaticBoxSizer(self.sizer_5_staticbox, wx.HORIZONTAL)
        grid_sizer_13 = wx.FlexGridSizer(1, 8, 0, 0)
        sizer_4 = wx.StaticBoxSizer(self.sizer_4_staticbox, wx.HORIZONTAL)
        grid_sizer_12 = wx.FlexGridSizer(1, 8, 0, 0)
        grid_sizer_17 = wx.FlexGridSizer(1, 1, 0, 0)
        sizer_8 = wx.StaticBoxSizer(self.sizer_8_staticbox, wx.HORIZONTAL)
        grid_sizer_18 = wx.FlexGridSizer(2, 4, 5, 5)
        grid_sizer_4 = wx.FlexGridSizer(1, 1, 0, 0)
        grid_sizer_5 = wx.FlexGridSizer(2, 1, 0, 0)
        sizer_3 = wx.StaticBoxSizer(self.sizer_3_staticbox, wx.HORIZONTAL)
        grid_sizer_7 = wx.FlexGridSizer(4, 1, 0, 0)
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.HORIZONTAL)
        grid_sizer_6 = wx.FlexGridSizer(4, 1, 0, 0)
        grid_sizer_2 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_2.Add(self.combo_box_hex, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.browsebutton, 0, 0, 0)
        grid_sizer_2.AddGrowableCol(0)
        grid_sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        grid_sizer_6.Add(self.writeflashbutton, 0, 0, 0)
        grid_sizer_6.Add(self.checkpicbutton, 0, 0, 0)
        grid_sizer_6.Add(self.abortsearchbutton, 0, wx.SHAPED, 0)
        grid_sizer_6.Add((90, 30), 0, 0, 0)
        grid_sizer_6.Add(self.main_gauge, 0, 0, 0)
        sizer_2.Add(grid_sizer_6, 1, wx.EXPAND, 0)
        grid_sizer_5.Add(sizer_2, 1, wx.EXPAND, 0)
        grid_sizer_7.Add(self.combo_box_speed, 0, 0, 0)
        grid_sizer_7.Add(self.searchportbutton, 0, wx.SHAPED, 0)
        grid_sizer_7.Add(self.port, 0, wx.EXPAND, 0)
        grid_sizer_7.Add(self.list_ports, 0, wx.EXPAND, 0)
        grid_sizer_7.AddGrowableRow(3)
        sizer_3.Add(grid_sizer_7, 1, wx.EXPAND, 0)
        grid_sizer_5.Add(sizer_3, 1, wx.EXPAND, 0)
        grid_sizer_5.AddGrowableRow(1)
        grid_sizer_3.Add(grid_sizer_5, 1, wx.EXPAND, 0)
        grid_sizer_4.Add(self.messages, 0, wx.EXPAND, 0)
        self.messages_tab.SetSizer(grid_sizer_4)
        grid_sizer_4.AddGrowableRow(0)
        grid_sizer_4.AddGrowableCol(0)
        grid_sizer_18.Add((5, 20), 0, wx.EXPAND, 0)
        grid_sizer_18.Add(self.openterminalbutton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_18.Add(self.closeterminalbutton, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_18.Add((5, 20), 0, wx.EXPAND, 0)
        grid_sizer_18.Add((5, 20), 0, wx.EXPAND, 0)
        grid_sizer_18.Add(self.combo_box_speed_terminal, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_18.Add(self.clearterminalbutton, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_18.Add((5, 20), 0, wx.EXPAND, 0)
        grid_sizer_18.AddGrowableRow(0)
        grid_sizer_18.AddGrowableRow(1)
        sizer_8.Add(grid_sizer_18, 1, wx.EXPAND, 0)
        grid_sizer_17.Add(sizer_8, 1, wx.EXPAND, 0)
        grid_sizer_17.AddGrowableRow(0)
        grid_sizer_17.AddGrowableCol(0)
        grid_sizer_9.Add(grid_sizer_17, 1, wx.EXPAND, 0)
        grid_sizer_12.Add(self.label_1_copy, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_12.Add(self.combo_box_tx_type, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_12.Add(self.combo_box_tx_data, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_12.Add(self.sendataterminalbutton, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_12.Add(self.button_12, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_12.Add(self.button_13, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_12.Add(self.button_14, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_12.AddGrowableCol(2)
        sizer_4.Add(grid_sizer_12, 1, wx.EXPAND, 0)
        grid_sizer_11.Add(sizer_4, 1, wx.EXPAND, 0)
        grid_sizer_13.Add(self.label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_13.Add(self.combo_box_rx_type, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_13.Add(self.combo_box_terminal_log, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_13.Add(self.button_15, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_13.Add(self.button_16, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_13.Add((20, 14), 0, wx.EXPAND, 0)
        grid_sizer_13.Add(self.button_17, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_13.Add((20, 14), 0, wx.EXPAND, 0)
        grid_sizer_13.AddGrowableCol(7)
        sizer_5.Add(grid_sizer_13, 1, wx.EXPAND, 0)
        grid_sizer_11.Add(sizer_5, 1, wx.EXPAND, 0)
        grid_sizer_11.AddGrowableRow(0)
        grid_sizer_11.AddGrowableRow(1)
        grid_sizer_11.AddGrowableCol(0)
        grid_sizer_9.Add(grid_sizer_11, 1, wx.EXPAND, 0)
        grid_sizer_9.AddGrowableRow(0)
        grid_sizer_9.AddGrowableCol(1)
        grid_sizer_8.Add(grid_sizer_9, 1, wx.EXPAND, 0)
        grid_sizer_14.Add(self.terminal, 0, wx.EXPAND, 0)
        grid_sizer_14.AddGrowableRow(0)
        grid_sizer_14.AddGrowableCol(0)
        sizer_6.Add(grid_sizer_14, 1, wx.EXPAND, 0)
        grid_sizer_8.Add(sizer_6, 1, wx.EXPAND, 0)
        self.terminal_tab.SetSizer(grid_sizer_8)
        grid_sizer_8.AddGrowableRow(1)
        grid_sizer_8.AddGrowableCol(0)
        self.Tabs.AddPage(self.messages_tab, "Messages")
        self.Tabs.AddPage(self.terminal_tab, "Terminal")
        grid_sizer_3.Add(self.Tabs, 1, wx.EXPAND, 0)
        grid_sizer_3.AddGrowableRow(0)
        grid_sizer_3.AddGrowableCol(1)
        grid_sizer_1.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        grid_sizer_1.AddGrowableRow(1)
        grid_sizer_1.AddGrowableCol(0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade
        self.want_abort=0
        self.start = 0
        self.end = 0 
        self.fin=0
        self.write_ok=1
        self.echo=1
        self.read=0
        self.terminal_back=' '
        self.tbicon = wx.TaskBarIcon() 
        
        self.ChangeTaskBarIcon('blue')
        

    def browsefile(self, event): # wxGlade: MainFrame.<event_handler>
        #Get the Saved path
        try:      
            dirname=GetRestoreSettings('FILES','hexfilepath')
        except:
            dirname=os.getcwd()
        
        #Setting File dialog
        filechooser = wx.FileDialog(self, "Select File:", dirname, "",
                               "Hex files (*.hex)|*.hex|Any (*.*)|*.*", wx.FD_CHANGE_DIR)         
        #Wait until user select a .hex file
        option = filechooser.ShowModal()
        #Acordig to the option
        if option == wx.ID_OK:
            #If OK has been pushed retrieve the path
            hexfile = filechooser.GetPath()
            #change combobox value to current Hex file
            self.combo_box_hex.SetValue(hexfile)
        else: 
          print "Cancel..."
        #get courrent directory to save it on config file
        global HexFilePath
        HexFilePath=filechooser.GetDirectory()
        
    def writeflash(self, event): # wxGlade: MainFrame.<event_handler>
        
        hexfile=self.combo_box_hex.GetValue()
        PORT=self.port.GetValue()
        BAUDRATE=int(self.combo_box_speed.GetValue())
        self.gaugecounter=0
        try:
            age=gethexage(hexfile)
            
        except:
            twrite('\n First select a valid Hex file')
            return
        message,pic_first_8_mem,pic_mem=chunkhexfile(hexfile)
        pic_config_mem=chunkhexfile_config(hexfile)
        twrite(checkserial(PORT,BAUDRATE))
        twrite('\n HEX: '+age+' old')
        message,PicType,max_flash,family=self.CheckPic(PORT,BAUDRATE)
        
        if message!='Not found, \n ERROR!':  
            
            Write_default_config(PORT,BAUDRATE,family)
            
            tranferdata(PORT,BAUDRATE,pic_first_8_mem,pic_mem,max_flash,family)
            
            write_config(PORT,BAUDRATE,pic_config_mem,family)

      
            return
        
        
        else:
            
            self.ChangeTaskBarIcon('red')
            self.timer.Start(2000)
            
                   

    def checkpic(self, event): # wxGlade: MainFrame.<event_handler>
        PORT=self.port.GetValue()
        BAUDRATE=int(self.combo_box_speed.GetValue())
        twrite(checkserial(PORT,BAUDRATE))
        twrite('\n Searching for PIC ...')
        try:
            
            message,PicType,max_flash,family=self.CheckPic(PORT,BAUDRATE)
            
            if max_flash!=None:
            
                self.timer.Start(2000)
                self.ChangeTaskBarIcon('green') 
                
            else:
                self.timer.Start(2000)
                self.ChangeTaskBarIcon('red') 
                
        except:
            pass
        return
    
    

    def abortsearch(self, event): # wxGlade: MainFrame.<event_handler>
        self.want_abort=1
        return

    def searchport(self, event): # wxGlade: MainFrame.<event_handler>
        self.list_ports.Clear()
        port_list=searchserial()
        self.port.SetValue(port_list[0])
        for disp in port_list:
            self.list_ports.Append(disp)   
        return

    def listboxdclick(self, event): # wxGlade: MainFrame.<event_handler>
        print "Event handler `listboxdclick' not implemented!"
        event.Skip()

    def openterminal(self, event): # wxGlade: MainFrame.<event_handler>
        self.fin=0
        PORT=self.port.GetValue()
        BAUD=self.combo_box_speed_terminal.GetValue()
        self.terminal.Enable(1)
        self.closeterminalbutton.Enable(1)
        self.openterminalbutton.Enable(0)
        self.combo_box_speed_terminal.Enable(0)
        try:
            global s
            s = serial.Serial(PORT, BAUD)
            s.timeout=0.1
        except:
            print 'somethig went wrong'
            return
        self.reader()
        s.close()
        
              
        if self.read==0:
            self.read=0
            self.Close()
        self.read=0
    

    def closeterminal(self, event): # wxGlade: MainFrame.<event_handler>
        
        self.fin=1
        self.terminal.Enable(0)
        self.closeterminalbutton.Enable(0)
        self.openterminalbutton.Enable(1)
        self.combo_box_speed_terminal.Enable(1)
        return

    def clearterminal(self, event): # wxGlade: MainFrame.<event_handler>
        self.terminal.Clear()
        return

    def sendataterminal(self, event): # wxGlade: MainFrame.<event_handler>
        dat=self.combo_box_tx_data.GetValue()
        WriteTerminal(dat)
        event.Skip()

    def ononebutton(self, event): # wxGlade: MainFrame.<event_handler>
        print "Event handler `ononebutton' not implemented!"
        event.Skip()

    def ontwobutton(self, event): # wxGlade: MainFrame.<event_handler>
        print "Event handler `ontwobutton' not implemented!"
        event.Skip()

    def onthreebutton(self, event): # wxGlade: MainFrame.<event_handler>
        print "Event handler `onthreebutton' not implemented!"
        event.Skip()

    def onbbutton(self, event): # wxGlade: MainFrame.<event_handler>
        print "Event handler `onbbutton' not implemented!"
        event.Skip()

    def onhbutton(self, event): # wxGlade: MainFrame.<event_handler>
        print "Event handler `onhbutton' not implemented!"
        event.Skip()

    def onrbutton(self, event): # wxGlade: MainFrame.<event_handler>
        print "Event handler `onrbutton' not implemented!"
        event.Skip()

    def ontextenterterminal(self, event): # wxGlade: MainFrame.<event_handler>
        print "Event handler `ontextenterterminal' not implemented!"
        event.Skip()

    def oncharterminal(self, event): # wxGlade: MainFrame.<event_handler>
        
        event.Skip()
            
       
        
        
    def oninit(self):
        
        
        try:
            #Getting Saved and restoring Values
            Top=int(GetRestoreSettings('WINDOW','top'))
            Left=int(GetRestoreSettings('WINDOW','left'))
            self.SetPosition((Top,Left))
            
            Height=int(GetRestoreSettings('WINDOW','height'))
            Width=int(GetRestoreSettings('WINDOW','width'))
            self.SetSize((Width,Height))
            
            HexFile=GetRestoreSettings('FILES','hexfile')
            self.combo_box_hex.SetValue(HexFile)
            
            COMspeed=GetRestoreSettings('PIC','comspeed')
            self.combo_box_speed.SetValue(COMspeed)
            
            TERMspeed=GetRestoreSettings('TERMINAL','termspeed')
            self.combo_box_speed_terminal.SetValue(TERMspeed)
            
            COMport=GetRestoreSettings('PIC','comport')
            self.port.SetValue(COMport)

        except:
            print 'no configfile'
        return
    
    
    
    def onclosebutton(self,event):
        
        self.Close()
        
    def Close(self):
        
        #finish firs terminal if it is open
        
        try:
            if self.read==1:
                self.fin=1
                self.read=0
                return
        except:
            pass
        

        #seving Settings
        try:        
            SaveSettings('FILES','HexFile',self.combo_box_hex.GetValue())
            SaveSettings('PIC','COMport',self.port.GetValue())
            SaveSettings('PIC',"COMspeed",self.combo_box_speed.GetValue())
            SaveSettings('TERMINAL',"TERMspeed",self.combo_box_speed_terminal.GetValue())
            Width,Height=self.GetSize()
            SaveSettings('WINDOW',"Width",Width)
            SaveSettings('WINDOW',"Height",Height)
            Top,Left=self.GetPosition()
            SaveSettings('WINDOW',"Top",Top)
            SaveSettings('WINDOW',"Left",Left)
            
            
            try:
                SaveSettings('FILES','HexFilePath',HexFilePath)
            except:
                pass

        except:
            print 'there was an error savig settings'
        self.Destroy()
        
    def CheckPic(self,PORT,BAUDRATE):
        self.abortsearchbutton.Show()
        gaugecounter=100
        self.ChangeTaskBarIcon('yellow')
        for i in range(0,33):
            wx.YieldIfNeeded()
            message,PicType,max_flash,family=detectpic(PORT,BAUDRATE)
            if self.want_abort==1:
                self.want_abort=0
                self.main_gauge.SetValue(0)
                break
            if max_flash!=None:
                
                break 
            self.main_gauge.SetValue(gaugecounter)
            gaugecounter=gaugecounter-3
            self.main_gauge.Update()   
        self.main_gauge.SetValue(0)
        self.abortsearchbutton.Hide()           
        twrite(message)
              
        return message,PicType,max_flash,family
    
    def reader(self):
        
        self.read=1
   
        while not(self.fin):
            wx.Yield()
            data = s.read(1)
            WriteTerminal(data)
        return
                   
    def EvtChar(self, event):
        
        self.combo_box_tx_type.SetSelection(4)
        try:
            code=chr(event.GetKeyCode())
            s.write(code)
                
        except:
            
            if event.GetKeyCode()==241:
                s.write('\xF1')
                
            elif event.GetKeyCode()==209:
                s.write('\xD1')
                       
        if self.combo_box_tx_type.GetValue() == 'TypEcho':
           
            if event.GetKeyCode()==8:
                pos=self.terminal.GetLastPosition()
                self.terminal.Remove(pos-1,pos)
                return
            
            else:
                
                try:
                
                    self.terminal.AppendText(code)
                
                except:
               
                    na=nonascii(chr(event.GetKeyCode()))
                    self.terminal.WriteText(na)
                    
                return
       
            
    def TerminalDisplay(self, event): # wxGlade: MainFrame.<event_handler>
        dump=self.terminal.GetValue()
        self.terminal.Clear()
        i=0
        type=self.combo_box_rx_type.GetValue()
  
        if type=='Hex':
            
            for disp in dump:
                hexa=hex(ord(disp))
                
                if hexa=='0xd':
                    self.terminal.WriteText('0d ')
                    
                elif hexa=='0xa':
                    self.terminal.WriteText('0a ')
                    
                elif hexa=='0xf':
                    self.terminal.WriteText('ff ')
                 
                else:   
                    self.terminal.WriteText(str(hexa)[2:4]+' ')
                
        if type=='Char':
            
            le=len(dump)/3
            for j in range(0,le,1):
                try:
                    datachar=chr(eval('0x'+(dump[0+i:2+i])))
                    self.terminal.WriteText(datachar)
                except:
                    
                    pass
                    
                i=i+3
            
    def TxType(self, event): # wxGlade: MainFrame.<event_handler>
        tx_type=self.combo_box_tx_type.GetValue()
        
        print tx_type
       
        if tx_type=='Type':
            self.combo_box_tx_data.Enable(0)
            return
            
        if tx_type=='TypEcho':
            self.combo_box_tx_data.Enable(0)
            return
            
        if tx_type=='Char':
            self.combo_box_tx_data.Enable(1)
            return
            
        if tx_type=='Char\\':
            self.combo_box_tx_data.Enable(1)
            return
        
    def ChangeTaskBarIcon(self,color):
        
          
        if color=='blue':

            icon = wx.Icon('/usr/share/tinybldLin/_tinybldLin/images/blue.ico', wx.BITMAP_TYPE_ICO)
            self.tbicon.SetIcon(icon, 'blue')
            return
            
        elif color=='red':

            icon = wx.Icon('/usr/share/tinybldLin/_tinybldLin/images/red.ico', wx.BITMAP_TYPE_ICO)
            self.tbicon.SetIcon(icon, 'blue')
            return
            
        elif color=='yellow':

            icon = wx.Icon('/usr/share/tinybldLin/_tinybldLin/images/yellow.ico', wx.BITMAP_TYPE_ICO)
            self.tbicon.SetIcon(icon, 'blue')
            return
        
        elif color=='green':

            icon = wx.Icon('/usr/share/tinybldLin/_tinybldLin/images/green.ico', wx.BITMAP_TYPE_ICO)
            self.tbicon.SetIcon(icon, 'blue')
            return
        
        elif color=='yg':

            icon = wx.Icon('/usr/share/tinybldLin/_tinybldLin/images/working.ico', wx.BITMAP_TYPE_ICO)
            self.tbicon.SetIcon(icon, 'blue')
            return
        
        return
    
    def OnTimer(self,event):
        self.ChangeTaskBarIcon('blue')
        self.timer.Stop()
        return

# end of class MainFrame

   

def tranferdata(PORT,BAUDRATE,pic_first_8_mem,pic_mem,max_flash,family):
    
    
    i=0

    if family=="16F8XX":
        hblock=8 #Hex Block 8 bytes
        block=4  #PIC Block 4 instructions (8 memory positions)
        maxpos=max_flash-100+4
        minpos=4
        
        for disp in pic_first_8_mem:
            pic_mem[i+2*max_flash-100]=disp
            i=i+1

    if family=="16F8X":
        #The pic 16F87 and 16F88 do erase the program memory in blocks
        #of 32 word blocks (64 bytes)
        
        hblock=64 #Hex Block 64 bytes
        block=32  #PIC Block 32 instructions (64 memory positions)
        
        maxpos=max_flash-100+4
        minpos=0
        
        pic_mem[0]=0x8A
        pic_mem[1]=0x15
        pic_mem[2]=0xA0
        pic_mem[3]=0x2F
        
        for disp in pic_first_8_mem:
            pic_mem[i+2*max_flash-100]=disp
            i=i+1
           
    if family=="18F" or family=="18FXX2":
            
        # The blocks have to be written using a 64 bytes boundary
        # so the first 8 bytes (reserved by TinyPic) will be re writen
        # So we have to include a goto max_flash-200+8
        goto_add=((max_flash-200+8)/2)
        hh_goto=(goto_add/0x10000)&0x0F
        h_goto=(goto_add/0x100)&0xFF
        l_goto=goto_add&0xFF
        
        pic_mem[0]=l_goto
        pic_mem[1]=0xEF
        pic_mem[2]=h_goto
        pic_mem[3]=0xF0+hh_goto
        
        for disp in pic_first_8_mem:
            pic_mem[i+max_flash-200]=disp
            i=i+1
        
        block=64
        hblock=64
        maxpos=max_flash-200+8
        minpos=0
        global max_pos
        max_pos=maxpos
           
    #Beginung Hex data tranfer
    WxTbl.ChangeTaskBarIcon('yg')
    try:
        s=serial.Serial(PORT,BAUDRATE)
        s.flushInput()
        s.flushOutput()
        s.timeout=0.1
        
    except:
        print ' No port detected'
        return
    interval=64*((len(pic_mem))/64+1)
    start = time.time()
    begin=time.strftime("%H:%M", time.localtime())
    
       
    for pic_pos in range(minpos,maxpos,block):
 
        wx.Yield()
        WxTbl.main_gauge.SetValue(100*(pic_pos)/interval)
            
        mem_block=[255]*hblock
        write_block=False
        for j in range(0,hblock):
                      
            #.hex file address is pic_address/2 for the 16F familly
            if (family=="16F8XX") or (family == "16F8X"):
                hex_pos=2*pic_pos+j
            elif family=="18F" or family=="18FXX2":
                hex_pos=pic_pos+j
            else :
                twrite("Error, family not suported:",family)
                WxTbl.timer.Start(2000)
                WxTbl.ChangeTaskBarIcon('red')
                return
            
            if pic_mem.has_key(hex_pos):
                mem_block[j]=pic_mem[hex_pos]
                write_block=True
                
        if write_block: 
            
            hm=(pic_pos/256)&255
            lm=(pic_pos&255)
            rl=len(mem_block)
            
            
            if (family=="16F8XX")or(family=="16F8X"):
                # Calculate checksum
                chs=hm+lm+rl
                s.write(chr(hm)+chr(lm)+chr(rl))
                for i in range(0,rl):
                
                    # Calculate checksum
                    chs=chs+mem_block[i]
                    
                    s.write(chr(mem_block[i]))
                    
                chs=((-chs)&255)
                s.write(chr(chs))

            if family=="18F" or family=="18FXX2":
                # Calculate checksum
                chs=hm+lm+rl
                # the pic receives 3 byte memory address
                # TBLPTRU TBLPTRH TBLPTRL
                # Todo: Check if TBLPTRU can be different to 0
                #           TBLPTRU TBLPTRH TBLPTRL
                s.write(chr(0)+chr(hm)+chr(lm)+chr(rl))
               
                for i in range(0,rl):
                    # Calculate checksum
                    chs=chs+mem_block[i]
                    s.write(chr(mem_block[i]))
                
                chs=((-chs)&255)
                s.write(chr(chs))
            
            ret=s.read(1)
            if ret!="K":
                print "Error writing to the memory position: "+ hex(pic_pos)+"\n\n"
                twrite('\nERROR')
                s.close()
                WxTbl.timer.Start(2000)
                WxTbl.ChangeTaskBarIcon('red')
                return        
       
    #write_config(config_mem,family)
    WxTbl.timer.Start(3000)
    WxTbl.ChangeTaskBarIcon('green')
    
    WxTbl.main_gauge.SetValue(0)  
    WxTbl.gaugecounter=0
    end = time.time() 
    twrite("\n WRITE OK at "+str(begin)+' time: '+str(end-start)[0:5]+' sec')
    
    s.flushInput()
    s.flushOutput()
    s.close()
    
    return
    
def twrite(data):   
    WxTbl.messages.AppendText(data)
    return


def WriteTerminal(rx):
    
    type=WxTbl.combo_box_rx_type.GetValue()
    
    if type=='Char':
       
        try:
            WxTbl.terminal.AppendText(str(rx))
            return
        except:
            non_ascii = nonascii(rx)
            
            if non_ascii!=None:
                WxTbl.terminal.AppendText(non_ascii)
            
        
        
    
    elif type=='Hex':
       
        try:
            h=ord(rx)
            k=hex(h)
            if h>15:
                
                WxTbl.terminal.AppendText(str(k)[2:4]+' ')
                return
            else:
                
                WxTbl.terminal.AppendText('0'+str(k)[2:4]+' ')
                return
                
        except:
            pass
        
               
        return

def write_config(PORT,BAUDRATE,pic_config_mem,family):
    
        
    if family=='18FXX2':

        #IF YOU MODIFY ANY OF THE CONFIG BYTES THE BOOTLOADER COULD STOP TO WORK
        #JUST MODIFY WHAT YOU NEED these are the config bytes for 18fXX2 check
        #yuors
        
        pic_config_mem[0X1]= 0x22
        
        #disable WDT
        #pic_config_mem[0X3]= pic_config_mem[0X3]&0xFE
        
                 
        config_len=len(pic_config_mem)
        s=serial.Serial(PORT,BAUDRATE)
        s.timeout=1

        TBLPTRU = (0x80 | 0x30)
        TBLPTRH = 0x00
        TBLPTRL = 0x00
       
        while TBLPTRL<config_len:
                
            s.write(chr(TBLPTRU)+chr(TBLPTRH)+chr(TBLPTRL)+chr(0x01))

            s.write(chr(pic_config_mem[TBLPTRL]))
                                    
            chs= TBLPTRU +TBLPTRH +TBLPTRL+1+pic_config_mem[TBLPTRL]
            
            
            chs=((-chs)&255)

            s.write(chr(chs))
            
            ret=s.read(1)
            
            if ret!="K":
                print "Error writing CONFIG memory position: "+ hex(TBLPTRL)+"\n\n"
                s.close()
                return  
             
            TBLPTRL=TBLPTRL+1
                  
            
        s.close()
        return
    
    else:
        return
    
def Write_default_config(PORT,BAUDRATE,family):
    
    pic_config_mem={}

    if family=='18FXX2':
        

        #IF YOU MODIFY ANY OF THE CONFIG BYTES THE BOOTLOADER COULD STOP TO WORK
        #JUST MODIFY WHAT YOU NEED these are the config bytes for 18fXX2 check
        #yuors
        
        pic_config_mem[0X00]= 0xFF
        pic_config_mem[0X01]= 0x22
        pic_config_mem[0X02]= 0x0E
        pic_config_mem[0X03]= 0x0E
        pic_config_mem[0X04]= 0xFF
        pic_config_mem[0X05]= 0x01
        pic_config_mem[0X06]= 0x81
        pic_config_mem[0X07]= 0xFF
        pic_config_mem[0X08]= 0x0F
        pic_config_mem[0X09]= 0xC0
        pic_config_mem[0X0a]= 0x0F
        pic_config_mem[0X0b]= 0xE0
        pic_config_mem[0X0c]= 0x0F
        pic_config_mem[0X0d]= 0x40
        
        #print pic_config_mem
         
        config_len=len(pic_config_mem)
        s=serial.Serial(PORT,BAUDRATE)
        s.timeout=1

        TBLPTRU = (0x80 | 0x30)
        TBLPTRH = 0x00
        TBLPTRL = 0x00
       
        while TBLPTRL<config_len:
                
            s.write(chr(TBLPTRU)+chr(TBLPTRH)+chr(TBLPTRL)+chr(0x01))

            s.write(chr(pic_config_mem[TBLPTRL]))
                                    
            chs= TBLPTRU +TBLPTRH +TBLPTRL+1+pic_config_mem[TBLPTRL]
            
            
            chs=((-chs)&255)

            s.write(chr(chs))
            
            ret=s.read(1)
            
            if ret!="K":
                print "Error writing CONFIG memory position: "+ hex(TBLPTRL)+"\n\n"
                s.close()
                return  0
             
            TBLPTRL=TBLPTRL+1
            
                 
            
        s.close()
        return 1
    
    else:
        return 1


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    WxTbl = MainFrame(None, -1, "")
    app.SetTopWindow(WxTbl)
    WxTbl.oninit()
    WxTbl.Show()
    app.MainLoop()