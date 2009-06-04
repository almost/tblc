#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA  02110-1301, USA.


import wx, detectpic, loadsavesettings, searchserial, browsefile
import transferhex,taskbaricon,hyperterminal

# begin wxGlade: extracode
# end wxGlade



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
        self.messages = wx.TextCtrl(self.messages_tab, -1, "Interface to TinyBootLoader\ncontact: claudiu.chiculita@ugal.ro\nhttp://www.etc.ugal.ro/cchiculita/software/picbootloader.htm\nfor GNU/Linux version:\ncontact:ferezvi@gmail.com\nhttp://fjv.awardspace.com\n--------------------------------------------------------------------------------------------------", style=wx.TE_MULTILINE)
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
        self.Bind(wx.EVT_CLOSE, self.close)
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer,self.timer)
        self.terminal.Bind(wx.EVT_CHAR, self.EvtChar)

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
        self.combo_box_speed_terminal.SetMinSize(wx.DLG_SZE(self.combo_box_speed_terminal, (44, 14)))
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
        
        self.wantabort=0
        self.naf=0
        self.tf=0
        

    def browsefile(self, event): # wxGlade: MainFrame.<event_handler>
        browsefile.BrowseFile(WxTbl)
        return

    def writeflash(self, event): # wxGlade: MainFrame.<event_handler>
        
        if self.tf==1:
            self.fin=1
       
        transferhex.TransferHex(WxTbl)
        return

    def checkpic(self, event): # wxGlade: MainFrame.<event_handler>
        
        if detectpic.CheckConection(WxTbl)==0:
            return
        
        type,max_flash,family=detectpic.CheckPic(WxTbl) 
            
       
        if max_flash!=None:
            taskbaricon.ChangeTaskBarIcon(WxTbl,'green')
            self.timer.Start(2000)
        else:
            taskbaricon.ChangeTaskBarIcon(WxTbl,'red')
            self.timer.Start(2000)
        return

    def abortsearch(self, event): # wxGlade: MainFrame.<event_handler>
        self.wantabort=1
        return
    
    def searchport(self, event): # wxGlade: MainFrame.<event_handler>
        searchserial.SearchSerial(WxTbl)
        return

    def listboxdclick(self, event): # wxGlade: MainFrame.<event_handler>
        self.port.Clear()
        self.port.SetValue(self.list_ports.GetStringSelection())
        return
        

    def openterminal(self, event): # wxGlade: MainFrame.<event_handler>
        hyperterminal.OpenTerminal(WxTbl)
        return

    def closeterminal(self, event): # wxGlade: MainFrame.<event_handler>
        self.read=0
        self.fin=1
        return

    def clearterminal(self, event): # wxGlade: MainFrame.<event_handler>
        self.terminal.Clear()
        return

    def TxType(self, event): # wxGlade: MainFrame.<event_handler>
        type=self.combo_box_tx_type.GetValue()
        if type=='Type' or type=='TypEcho':
            self.combo_box_tx_data.Enable(0)
            self.sendataterminalbutton.Enable(0)
        if type=='Char' or type=='Char\\':
            self.combo_box_tx_data.Enable(1)
            self.sendataterminalbutton.Enable(1)
        return

    def sendataterminal(self, event): # wxGlade: MainFrame.<event_handler>
        #Check if terminal is open
        if self.tf!=1:
            print 'No open terminal'
            return
        else:
            
            try:
                tx_data=self.combo_box_tx_data.GetValue()
                hyperterminal.SendTxData(WxTbl,tx_data)
            except:
                print 'you are trying to send a nonascii char'
            
            
        
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

    def TerminalDisplay(self, event): # wxGlade: MainFrame.<event_handler>
        hyperterminal.ChangeDisplay(WxTbl)
        return

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
        
    def close(self, event):
        loadsavesettings.OnClose(WxTbl)
        
    def OnTimer(self,event):
        taskbaricon.ChangeTaskBarIcon(WxTbl,'blue')
        self.timer.Stop()
        return
    
    def EvtChar(self, event):
       
        
        type=self.combo_box_tx_type.GetValue()
        if type=='Char' or type=='Char\\':
            self.combo_box_tx_type.SetSelection(3)
            self.sendataterminalbutton.Enable(0)
            self.combo_box_tx_data.Enable(0)
                     
        
        code=event.GetKeyCode()
        hyperterminal.SendData(WxTbl,code)
        return
        
        

# end of class MainFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    WxTbl = MainFrame(None, -1, "")
    app.SetTopWindow(WxTbl)
    WxTbl.Show()
    loadsavesettings.OnInit(WxTbl)
    
    app.MainLoop()