import serial

def write_mem(PORT,BAUDRATE,pic_pos,mem_block,family):
            
    s=serial.Serial(PORT,BAUDRATE,timeout=0.1)
   
##    try:   
##        s.flushInput()
##    except:
##        s.open()
##        s.flushInput()
    
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

    if family=="18F":
        # Calculate checksum
        chs=hm+lm+rl
        # the pic receives 3 byte memory address
        # TBLPTRU TBLPTRH TBLPTRL
        # Todo: Check if TBLPTRU can be different to 0
        #           U TBLPTRH TBLPTRL
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
        s.close()
    s.close()
    return ret

def write_config(config_block,family):
   print 'TODO'
        
def write_eeprom(config_block,family):
    print 'TODO'
    
