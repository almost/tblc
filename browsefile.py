import os,wx
from loadsavesettings import GetRestoreSettings
from loadsavesettings import SaveSettings

def BrowseFile(WxTbl): 
        #Get the Saved path
    try:      
        dirname=GetRestoreSettings('FILES','hexfilepath')
    except:
        dirname=os.getcwd()
    
    #Setting File dialog
    filechooser = wx.FileDialog(WxTbl, "Select File:", dirname, "",
                           "Hex files (*.hex)|*.hex|Any (*.*)|*.*", wx.FD_CHANGE_DIR)         
    
    #Wait until user select a .hex file
    option = filechooser.ShowModal()
    
    #Acordig to the option
    if option == wx.ID_OK:
        #If OK has been pushed retrieve the path
        hexfile = filechooser.GetPath()
        #change combobox value to current Hex file
        WxTbl.combo_box_hex.SetValue(hexfile)
    else: 
      print "Cancel..."
    #get courrent directory to save it on config file
   
    HexFilePath=filechooser.GetDirectory()
    SaveSettings('FILES','HexFilePath',HexFilePath)
    