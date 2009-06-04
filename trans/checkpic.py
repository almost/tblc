try: 
    import serial 
except ImportError:
    raise ImportError,"Se requiere el modulo python-serial"

def checkserial(PORT,BAUD):
    message=None
    try:
        ser = serial.Serial(PORT,BAUD,timeout=0.01)
        ser.write('k')
        ser.flushOutput() 
        ser.close()
        message='\n\nConnect to ' + PORT + ' at ' + str(BAUD)
        return message
    except:
        message="\n Could not connect to " + PORT + " at " + str(BAUD) + '\n ERROR!'
        return message
   
    
def detectpic(PORT,BAUD):
##    print 'detecting PIC'
    PicType=None
    max_flash=None
    family=None
    
    try:
        ser = serial.Serial(PORT,BAUD,timeout=0.01)
        ser.flushInput()

        #Ask for PIC IDE
        try:
            ser.write(chr(0xC1))
        except:
            message="\n Could not connect to " + PORT + " at " + str(BAUD) + '\n ERROR!'
            return message,PicType,max_flash,family
        
        #wait for PIC answer
        ret=ser.read(2)
        
        #close serial port
        ser.flushInput()
        ser.close()
        
        #In case there was no answer
        if len(ret)!=2:
            message='Not found, \n ERROR!'
            ser.close
            return message,PicType,max_flash,family
        
        #In case of pic not recognized
        if ret[1]!= "K":
            message="\n Error, PIC not recognized (protocol error)\n"
            return message,PicType,max_flash,family 
        
        pt=ord(ret[0])
        
        PicType, max_flash, family=pictype(pt)
        message='\n Found:'+ PicType
        return message,PicType,max_flash,family
    except:
        message='No PORT detected'
        return message,PicType,max_flash,family

def pictype(pt):
    
    
    if pt==0x31:
        PicType="16F 876A/877A";
        max_flash=0x2000;
    elif pt==0x32:
        PicType="16F 873A/874A";
        max_flash=0x1000;
    elif pt==0x33:
        PicType="16F 87/F88";
        max_flash=0x1000;
    elif pt==0x41:
        PicType="18F 252o/452o";
        max_flash=0x8000;
    elif pt==0x42:
        PicType="18F 242o/442o";
        max_flash=0x4000;
    elif pt==0x43:
        PicType="18F 258/458";
        max_flash=0x8000;
    elif pt==0x44:
        PicType="18F 248/448";
        max_flash=0x4000;
    elif pt==0x45:
        PicType="18F 1320/2320";
        max_flash=0x2000;
    elif pt==0x46:
        PicType="18F 1220/2220";
        max_flash=0x1000;
    elif pt==0x47:
        PicType="18F 4320";
        max_flash=0x2000;
    elif pt==0x48:
        PicType="18F 4220";
        max_flash=0x1000;
    elif pt==0x4A:
        PicType="18F 6720/8720";
        max_flash=0x20000;
    elif pt == 0x4B:
        PicType="18F 6620/8620"
        max_flash=0x10000
    elif pt ==0x4C:
        PicType="18F 6520/8520"
        max_flash=0x8000
    elif pt==0x4D:
        PicType="18F 8680";
        max_flash=0x10000;
    elif pt==0x4E:
        PicType="18F 2525/4525";
        max_flash=0xC000;
    elif pt==0x4F:
        PicType="18F 2620/4620";
        max_flash=0x10000;
    elif pt==0x55:
        PicType="18F 2550/4550";
        max_flash=0x8000;
    elif pt==0x56:
        PicType="18F 2455/4455";
        max_flash=0x6000;
    else:
        PicType="Microcontroller not supported or not detected";
        max_flash=None;

    family=None

    if (pt==0x31) or (pt==0x32):
        family="16F8XX"
    
    elif (pt==0x33):
        family="16F8X"
   
    elif (pt==0x41) or (pt==0x42):
        family="18FXX2"
    
    elif (pt>0x42) and (pt<0x60):
        family="18F"
           
    return PicType, max_flash, family
    