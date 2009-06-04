import wx


def ChangeTaskBarIcon(WxTbl,color):
    
    
    if color=='blue':

        icon = wx.Icon('/usr/share/tinybldLin/_tinybldLin/images/blue.ico', wx.BITMAP_TYPE_ICO)
        WxTbl.tbicon.SetIcon(icon, 'blue')
        return
        
    elif color=='red':

        icon = wx.Icon('/usr/share/tinybldLin/_tinybldLin/images/red.ico', wx.BITMAP_TYPE_ICO)
        WxTbl.tbicon.SetIcon(icon, 'blue')
        return
        
    elif color=='yellow':

        icon = wx.Icon('/usr/share/tinybldLin/_tinybldLin/images/yellow.ico', wx.BITMAP_TYPE_ICO)
        WxTbl.tbicon.SetIcon(icon, 'blue')
        return
    
    elif color=='green':

        icon = wx.Icon('/usr/share/tinybldLin/_tinybldLin/images/green.ico', wx.BITMAP_TYPE_ICO)
        WxTbl.tbicon.SetIcon(icon, 'blue')
        return
    
    elif color=='yg':

        icon = wx.Icon('/usr/share/tinybldLin/_tinybldLin/images/working.ico', wx.BITMAP_TYPE_ICO)
        WxTbl.tbicon.SetIcon(icon, 'blue')
        return
    
    return