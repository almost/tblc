#!/usr/bin/python
# -*- coding: utf-8 -*-

def NonAscii(WxTbl,nac):
   
    try:
 
            if WxTbl.naf==1:
            
                if nac == 0xa1:
                    nonasciichar = unicode('\xc3\xa1', 'utf-8', 'replace')
                    return nonasciichar
                elif nac == 0xa9:
                    nonasciichar = unicode('\xc3\xa9', 'utf-8', 'replace')
                    return nonasciichar
                elif nac == 0xad:
                    nonasciichar = unicode('\xc3\xad', 'utf-8', 'replace')
                    return nonasciichar
                elif nac == 0xb3:
                    nonasciichar = unicode('\xc3\xb3', 'utf-8', 'replace')
                    return nonasciichar
                elif nac == 0xba:
                    nonasciichar = unicode('\xc3\xba', 'utf-8', 'replace')
                    return nonasciichar
                
                elif nac == 0x81:
                    nonasciichar = unicode('\xc3\x81', 'utf-8', 'replace')
                    return nonasciichar
                elif nac == 0x89:
                    nonasciichar = unicode('\xc3\x89', 'utf-8', 'replace')
                    return nonasciichar
                elif nac == 0x8d:
                    nonasciichar = unicode('\xc3\x8d', 'utf-8', 'replace')
                    return nonasciichar
                elif nac == 0x93:
                    nonasciichar = unicode('\xc3\x93', 'utf-8', 'replace')
                    return nonasciichar
                elif nac == 0x9a:
                    nonasciichar = unicode('\xc3\x9a', 'utf-8', 'replace')
                    return nonasciichar
                
                WxTbl.naf=0
            
            if nac == 0xc3:
                WxTbl.naf=1
                nonasciichar=''
                return nonasciichar
            
            if nac == 0x87:
                nonasciichar = unicode('\xc3\x87', 'utf-8', 'replace')
                return nonasciichar
            elif nac == 0xa7:
                nonasciichar = unicode('\xc3\xa7', 'utf-8', 'replace')
                return nonasciichar
            
            elif nac == 0x91:
                nonasciichar = unicode('\xc3\x91', 'utf-8', 'replace')
                return nonasciichar
            elif nac == 0xb1:
                nonasciichar = unicode('\xc3\xb1', 'utf-8', 'replace')
                return nonasciichar
            
            elif nac == 209:
                nonasciichar = unicode('\xc3\x91', 'utf-8', 'replace')
                return nonasciichar
            elif nac == 241:
                nonasciichar = unicode('\xc3\xb1', 'utf-8', 'replace')
                return nonasciichar

            else:
                nonasciichar=str(hex(nac))
                return nonasciichar
            
  
    except:
        pass
        
    return ''