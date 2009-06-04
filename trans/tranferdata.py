import serial

def transferdata(PORT,BAUDRATE,pic_first_8_mem,pic_mem,config_mem,adress_extended,max_flash,family):
   
    if family=="16F8XX":
        hblock=8 #Hex Block 8 bytes
        block=4  #PIC Block 4 instructions (8 memory positions)
        maxpos=max_flash-100+4
        minpos=4
        for disp in pic_first_8_mem:
            pic_mem[i+2*max_flash-200]=disp
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
        i=0
        for disp in pic_first_8_mem:
            pic_mem[i+2*max_flash-200]=disp
            i=i+1
        
           
    if family=="18F":
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
       
        
##    s=serial.Serial(PORT,BAUDRATE,timeout=1)
##    #Beginung Hex data tranfer
##    
##    
##    global interval
##    interval=len(pic_mem)
##    for pic_pos in range(minpos,maxpos,block):
##               
##        mem_block=[255]*hblock
##        write_block=False
##        for j in range(0,hblock):
##                      
##            #.hex file address is pic_address/2 for the 16F familly
##            if (family=="16F8XX") or (family == "16F8X"):
##                hex_pos=2*pic_pos+j
##            elif family=="18F":
##                hex_pos=pic_pos+j
##            else :
##                twrite("Error, family not suported:",family)
##                return
##            
##            if pic_mem.has_key(hex_pos):
##                mem_block[j]=pic_mem[hex_pos]
##                write_block=True
##                
##        if write_block:
##            
##            ret=write_mem(pic_pos,mem_block,family)
##            
##            if ret!="K":
##                return 
##    
##    s.close()  
##    WxTbl.main_gauge.SetValue(0)  
##    WxTbl.gaugecounter=0
##    success=1
##    twrite("\n WRITE OK at"+' time:'+' sec')
##
##def write_mem(pic_pos,mem_block,family):
##    
##    try:   
##        s.flushInput()
##    except:
##        s.open()
##        s.flushInput()
##    
##    hm=(pic_pos/256)&255
##    lm=(pic_pos&255)
##    rl=len(mem_block)
##    
##    if (family=="16F8XX")or(family=="16F8X"):
##        # Calculate checksum
##        chs=hm+lm+rl
##        s.write(chr(hm)+chr(lm)+chr(rl))
##        for i in range(0,rl):
##        
##            # Calculate checksum
##            chs=chs+mem_block[i]
##            
##            s.write(chr(mem_block[i]))
##            
##        chs=((-chs)&255)
##        s.write(chr(chs))
##        
##    if family=="18F":
##        # Calculate checksum
##        chs=hm+lm+rl
##        # the pic receives 3 byte memory address
##        # U TBLPTRH TBLPTRL
##        # Todo: Check if U can be different to 0
##        #           U TBLPTRH TBLPTRL
##        s.write(chr(0)+chr(hm)+chr(lm)+chr(rl))
##       
##        for i in range(0,rl):
##            # Calculate checksum
##            chs=chs+mem_block[i]
##            s.write(chr(mem_block[i]))
##            wx.Yield()
##            WxTbl.main_gauge.SetValue(100*WxTbl.gaugecounter/interval)
##            WxTbl.gaugecounter=WxTbl.gaugecounter+1
##            
##
##        chs=((-chs)&255)
##        s.write(chr(chs))
##    
##    ret=s.read(1)
##    s.close()
##    if ret!="K":
##        twrite("Error writing to the memory position: "+
##                    hex(pic_pos)+"\n\n")
##    return ret
