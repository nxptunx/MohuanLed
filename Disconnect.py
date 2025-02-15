from bluelights import BJLEDInstance
import asyncio
async def main():
    led = BJLEDInstance()                       
    try:
        print("Disconnecting Led")
    finally:
        await led._disconnect()  
     
asyncio.run(main())
print("Disconnected From Led") 