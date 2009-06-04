from hexage import gethexage

def chunkhexfile(WxTbl,filename):
    
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
        message="Can't open file:"+filename+"\n\n"
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
            WxTbl.messages.AppendText('\n Warning! CRC failed on line '+str(row_counter))
            
        row_counter=row_counter+1
                
    WxTbl.messages.AppendText('\n HEX:  '+ age+' old,'+ INHX +' ,'+Fcode+cfg+ ', total='+str(total)+ ' bytes.') 
    return pic_mem, eeprom_mem, config_mem
