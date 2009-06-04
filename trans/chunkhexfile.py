
def chunkhexfile(filename):
    
    pic_mem={}
    pic_first_8_mem=[]
    address_extended=''
    config_mem=[]
    message='OK'
    f8f=0
          
    try:
        f=open(filename, 'r')
    except IOError:
        message="Can't open file:"+filename+"\n\n"
        return None
    
    hexfile=f.readlines()
    f.close()
    le=len(hexfile)
    
    for rec in hexfile:  
       
        # Check Hex file Start code
        if rec[0]!=":":
            
            if rec[0]==";":
                message=str(rec)
                print message
                break
            else:
                message="Hex file not recognized:\nLine: "+str(act)+ " File: "+filename+"\n\n"
                return message
        
        # Read Byte count
        byte_count=eval("0x"+rec[1:3])
            
        # Read register address 
        address=eval("0x"+rec[3:7])
            
        # Read record type
        record_type=eval("0x"+rec[7:9])

                  
        # Get all data register
        if record_type==0 : 
            
            if address==0:
                f8f=f8f+1
                 
            for i in range(9,9+2*byte_count,2):
                
                data=rec[i:i+2] 
                
                # store first 8 memory data in pic_first_8_mem
   
                if address < 0x08 and f8f==1:
                    
                    pic_first_8_mem.append(eval("0x"+data))
                       
                if address>0x03 and f8f==1:
                    
                    pic_mem[address]=eval("0x"+data) 
                    
                address=address+1   
                
                
    return message,pic_first_8_mem,pic_mem


def chunkhexfile_config(filename):
    
    pic_config_mem={}
    pic_eeprom_mem={}
    mem=0;

    try:
        f=open(filename, 'r')
    except IOError:
        message="Can't open file:"+filename+"\n\n"
        return None
    
    hexfile=f.readlines()
    f.close()
    le=len(hexfile)
    
    for rec in hexfile:  
       
        # Check Hex file Start code
        if rec[0]!=":":
            
            if rec[0]==";":
                message=str(rec)
                print message
                break
            else:
                message="Hex file not recognized:\nLine: "+str(act)+ " File: "+filename+"\n\n"
                return message
        
        # Read Byte count
        byte_count=eval("0x"+rec[1:3])
            
        # Read register address 
        address=eval("0x"+rec[3:7])
            
        # Read record type
        record_type=eval("0x"+rec[7:9])

        if mem==2:
            
            
            for i in range(9,9+2*byte_count,2):
                
                data=rec[i:i+2] 
                pic_config_mem[address]=eval("0x"+data)     
                address=address+1   
                
                
                
            mem=mem+1
            
            
        # Get all config register
        if record_type==4 : 
            mem=mem+1
                 
    return pic_config_mem


