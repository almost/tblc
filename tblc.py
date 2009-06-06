#!/usr/bin/python
"""
Tiny PIC Boot Loader Command Line Tool

Based (very heavily) on the code by ferezvi@gmail.com from
tinybldlin.sf.net

tom@almsotobsolete.net

For Felix's Machines http://felixsmachines.com/
"""

import serial,wx
import time,sys
from pictype import PicType
from hexage import gethexage



def CheckConection(port, baud):
    try:
        ser = serial.Serial(port,baud,timeout=0.1)
        ser.close()
        return True
    except:
        return False

def CheckPic(port, baud):
    type=None
    max_flash=None
    family=None
    
    try:
        #OpenPort
        ser = serial.Serial(port,baud,timeout=0.03)
        
        #Since we are lazy there will be a lot of chance to press reset           
        #Ask for PIC IDE several times

        #Ask IDE
        ser.write(chr(0xC1))
          
        #wait for PIC answer
        ret=ser.read(2)
            
        #If pic send 2 bytes lets check what sends
        if len(ret)!=2:
            return None,None,None
            
    except:
        return None,None,None
    
    #closing serial port
    ser.close()
    #clear main gauge
    
    #In case of pic not recognized
    if ret[1]!= "K":
        print "Error, PIC not recognized (protocol error)"
        return None,None,None
        
    pt=ord(ret[0])
    type, max_flash, family=PicType(pt)
    return type,max_flash,family

def chunkhexfile(filename):
    pic_mem={}
    eeprom_mem={}
    config_mem={}
    type='data'
    total=0
    INHX='INX8M'
    Fcode=''
    cfg=''
           
    try:
        f=open(filename, 'r')
    except IOError:
        print "Can't open file:"+filename+"\n\n"
        return None,None,None
    
    hexfile=f.readlines()
    f.close()
    row_counter=1
    
    age=gethexage(filename)
    
    for rec in hexfile: 
       
        # Check Hex file Start code
        if rec[0]!=":":
            
            
            if rec[0]==";":
                message=str(rec)
                print message
                break
            else:
                message="Hex file not recognized:\nLine: "+str(row_counter)+ " File: "+filename+"\n\n"
                print message
                return None,None,None
        
        # Read Byte count
        byte_count=eval("0x"+rec[1:3])
        
        #Calculate total bytes
        total=total+byte_count
            
        # Read register address 
        address=eval("0x"+rec[3:7])
            
        # Read record type
        record_type=eval("0x"+rec[7:9])
        
        #Read Crc
        crc=eval("0x"+rec[9+2*byte_count:11+2*byte_count])
             
        # Calculate checksum
        chs=byte_count+eval("0x"+rec[3:5])+eval("0x"+rec[5:7])+record_type
        
  
        if record_type==0x04:
            
            INHX='INHX32'
            
            extended_adress=eval("0x"+rec[9:13])
            # Calculate checksum
            chs=chs+eval("0x"+rec[9:11])+eval("0x"+rec[11:13])
            if extended_adress==0x0000:
                
                type='data'
                cfg='+cfg'
                
            elif extended_adress==0x0030:
                
                type='config'
                
            elif extended_adress==0x00F0:
                type='eeprom'
                
                  
        # Get all data register
        if record_type==0 and type=='data': 
                     
            for i in range(9,9+2*byte_count,2):
                
                data=rec[i:i+2]
                         
                pic_mem[address]=eval("0x"+data)
                
                # Calculate checksum
                chs=chs+pic_mem[address]
  
                if address%2:
                    
                    if pic_mem[address]<0x40 and Fcode=='':
                        Fcode='16Fcode'
                   
                    if pic_mem[address]>0x3F and Fcode=='16Fcode':
                        Fcode='18Fcode'
                                   
                address=address+1 
                  
   

        # Get all config register
        if record_type==0 and type=='config': 
           
            for i in range(9,9+2*byte_count,2):
                
                data=rec[i:i+2] 
                              
                config_mem[address]=eval("0x"+data)
                
                # Calculate checksum
                chs=chs+config_mem[address]
                    
                address=address+1  
                
        # Get all EEPROM register
        if record_type==0 and type=='eeprom': 
           
            for i in range(9,9+2*byte_count,2):
                
                data=rec[i:i+2] 
                              
                eeprom_mem[address]=eval("0x"+data)
                    
                address=address+1
         
        chs=(1+~chs)&0xff
        
        if chs!=crc:
            print 'Warning! CRC failed on line '+str(row_counter)
            
        row_counter=row_counter+1
                
    print 'HEX:  '+ age+' old,'+ INHX +' ,'+Fcode+cfg+ ', total='+str(total)+ ' bytes.'
    return pic_mem, eeprom_mem, config_mem


def TransferHex(hexfile, port="/dev/ttyUSB0", baud=19200):
    baud = int(baud)
    pic_mem, eeprom_mem, config_mem = chunkhexfile(hexfile)
    
    print "Trying to open port"
    while True:
        if CheckConection(port, baud):
            break
        else:
            print "Can't open port, retrying..."
            time.slee(2)
    print "Attempting to connect to PIC (press the reset button then release it)"
    while True:
        type,max_flash,family=CheckPic(port, baud)
        if max_flash is not None:
            break
        
    #Ading first 8 pic mem data to the begining of bootloader
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
    
    start = time.time()
    Write_default_config(port, baud, family)
    begin=time.strftime("%H:%M", time.localtime())

    print "Programming.."
    try:
        s=serial.Serial(port,baud,timeout=0.5)
    except:
        print 'No port detected'
        return
    
    for pic_pos in range(minpos,maxpos,block):
        mem_block=[255]*hblock
        write_block=False
        for j in range(0,hblock):
                      
            #.hex file address is pic_address/2 for the 16F familly
            if (family=="16F8XX") or (family == "16F8X"):
                hex_pos=2*pic_pos+j
                
            elif family=="18F" or family=="18FXX2":
                hex_pos=pic_pos+j
                
            else :
                print "Error, family not suported:",family
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
                return        
       
    #write_config(config_mem,family)
    end = time.time() 
    print "\n WRITE OK at "+str(begin)+' time: '+str(end-start)[0:5]+' sec'
     
    s.close()
    return 

def Write_default_config(port, baud, family):
    
    pic_config_mem={}
    
    try:
        s=serial.Serial(port,baud)
        s.flushInput()
        s.flushOutput()
        s.timeout=0.2
        
    except:
        print ' No port detected'
        return False

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
    return True

if (__name__ == '__main__'):
    try:
        TransferHex(*sys.argv[1:])
    except:
        print "tblc.py <hexfile> [port] [baud]"
