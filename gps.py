from machine import UART
import uasyncio as asyncio
from machine import Pin



# pin tx and rx
uart= UART(0,baudrate=9600,tx=Pin(0),rx=Pin(1),bits=8,parity=None,stop=1)

async def sender():
    swriter = asyncio.StreamWriter(uart, {})
    while True:
        print('Wrote')
        await asyncio.sleep(1)

async def receiver():
    sreader = asyncio.StreamReader(uart)
    while True:
        nmea = await sreader.readline()
        #print('Recieved', nmea.rstrip().decode("utf-8"))
        if nmea.startswith( '$GPRMC' ) :
            dic={nmea[:7]:nmea.rstrip().decode('utf-8')}
            print(dic)

            
 

loop = asyncio.get_event_loop()
loop.create_task(sender())
loop.create_task(receiver())
loop.run_forever()
