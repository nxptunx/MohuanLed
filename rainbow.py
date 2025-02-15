from bluelights import BJLEDInstance
import asyncio
ADDRESS = 'FF:10:10:9D:EC:AC'
UUID = '0000ee01-0000-1000-8000-00805f9b34fb'
async def main():
    led = BJLEDInstance(address=ADDRESS, uuid=UUID)                       
    try:
        await led.rainbow_cycle(duration_per_color=10.0)                    
    except Exception as e:
      print(e)                
     
asyncio.run(main())
print("Turned Led Rainbow")