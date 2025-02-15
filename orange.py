from bluelights import BJLEDInstance
import asyncio
ADDRESS = 'FF:10:10:9D:EC:AC'
UUID = '0000ee01-0000-1000-8000-00805f9b34fb'
async def main():
    led = BJLEDInstance(address=ADDRESS, uuid=UUID)                       
    try:
        await led.set_color_to_rgb(255, 30, 0)                   
    except Exception as e:
      print(e)                
     
asyncio.run(main())
print("Turned Led Orange")