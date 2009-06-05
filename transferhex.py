import serial,wx
import chunkhexfile,detectpic,time
from taskbaricon import ChangeTaskBarIcon


def TransferHex(WxTbl):
    
    wx.YieldIfNeeded()
    
    if detectpic.CheckConection(WxTbl)==0:
        return 
    
    hexfile = WxTbl.combo_box_hex.GetValue()
       
    pic_mem, eeprom_mem, config_mem = chunkhexfile.chunkhexfile(WxTbl,hexfile)
    
    type,max_flash,family=detectpic.CheckPic(WxTbl)
    
    if max_flash==None:
        WxTbl.timer.Start(2000)
        ChangeTaskBarIcon(WxTbl,'red')
        return
    
    #Ading firt 8 pic mem data to the begining of bootloader
    
    
    
    
    
    
    if family=="16F8XX":
        hblock=8 #Hex Block 8 bytes
        block=4  #PIC Block 4 instructions (8 memory positions)
        maxpos=max_flash-100+4
        minpos=4
        
        interval=8*((len(pic_mem))/8+1)
        for i in range (0,8,1):
           
            try:
                pic_mem[i+2*max_flash-200]=pic_mem[i]
                    
                
            except:
                pic_mem[i+2*max_flash-200]=0xff

    if family=="16F8X":
        #The pic 16F87 and 16F88 do erase the program memory in blocks
        #of 32 word blocks (64 bytes)
        
        hblock=64 #Hex Block 64 bytes
        block=32  #PIC Block 32 instructions (64 memory positions)
        
        maxpos=max_flash-100+4
        minpos=0

        ###############################
        for i in range(8):
            adr = 2*(max_flash-100)+i
            pic_mem[adr] = pic_mem.get(i,0xFF)
        ###############################
        
        pic_mem[0]=0x8A
        pic_mem[1]=0x15
        pic_mem[2]=0xA0
        pic_mem[3]=0x2F

        interval=64*((len(pic_mem))/64+1)
        
                  
    if family=="18F" or family=="18FXX2":
        
        for i in range (0,8,1):
            try:
                pic_mem[i+max_flash-200]=pic_mem[i]
        
            except:
                pic_mem[i+max_flash-200]=0xff
               
            
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

        block=64
        hblock=64
        maxpos=max_flash-200+8
        minpos=0
        interval=64*((len(pic_mem))/64+1)
        
        
    #Beginung Hex data tranfer
    
    ChangeTaskBarIcon(WxTbl,'yg')
    PORT= WxTbl.port.GetValue()
    BAUDRATE=int(WxTbl.combo_box_speed.GetValue())
      
    start = time.time()
    Write_default_config(WxTbl,family)
    begin=time.strftime("%H:%M", time.localtime())
    
    try:
        s=serial.Serial(PORT,BAUDRATE,timeout=0.5)
        

    except:
        print ' No port detected'
        return
    
      
    for pic_pos in range(minpos,maxpos,block):
        
        wx.YieldIfNeeded()
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
                WxTbl.messages.AppendText("Error, family not suported:",family)
                WxTbl.timer.Start(2000)
                WxTbl.ChangeTaskBarIcon(WxTbl,'red')
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
                ret=s.read(1)

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
                s.close()
                
                print "Error writing to the memory position: "+ hex(pic_pos)+"\n\n"
                WxTbl.messages.AppendText('\n ERROR')
                
                WxTbl.timer.Start(2000)
                ChangeTaskBarIcon(WxTbl,'red')
                return        
       
    #write_config(config_mem,family)
    print "blarg"
    WxTbl.timer.Start(2000)
    ChangeTaskBarIcon(WxTbl,'green')
    
    WxTbl.main_gauge.SetValue(0)  
    WxTbl.gaugecounter=0
    end = time.time() 
    WxTbl.messages.AppendText("\n WRITE OK at "+str(begin)+' time: '+str(end-start)[0:5]+' sec')
     
    s.close()
    return 

def Write_default_config(WxTbl,family):
    
    pic_config_mem={}
    PORT= WxTbl.port.GetValue()
    BAUDRATE=int(WxTbl.combo_box_speed.GetValue())
    
    try:
        s=serial.Serial(PORT,BAUDRATE)
        s.flushInput()
        s.flushOutput()
        s.timeout=0.2
        
    except:
        print ' No port detected'
        return

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
        
        config_len=len(pic_config_mem)
        
        #print pic_config_mem
        
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

        
