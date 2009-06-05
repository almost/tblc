import wx


def ChangeTaskBarIcon(WxTbl,color):
    
    
    if color=='blue':

        icon = wx.Icon('images/blue.ico', wx.BITMAP_TYPE_ICO)
        WxTbl.tbicon.SetIcon(icon, 'blue')
        return
        
    elif color=='red':

        icon = wx.Icon('images/red.ico', wx.BITMAP_TYPE_ICO)
        WxTbl.tbicon.SetIcon(icon, 'blue')
        return
        
    elif color=='yellow':

        icon = wx.Icon('images/yellow.ico', wx.BITMAP_TYPE_ICO)
        WxTbl.tbicon.SetIcon(icon, 'blue')
        return
    
    elif color=='green':

        icon = wx.Icon('images/green.ico', wx.BITMAP_TYPE_ICO)
        WxTbl.tbicon.SetIcon(icon, 'blue')
        return
    
    elif color=='yg':

        icon = wx.Icon('images/working.ico', wx.BITMAP_TYPE_ICO)
        WxTbl.tbicon.SetIcon(icon, 'blue')
        return
    
    return
