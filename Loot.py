from ReadWriteMemory import ReadWriteMemory
import Offset

rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog-GOG.exe") #change the process name to what version u use
process.open()

while True:
    process.write(Offset.Gas, 99999)
    process.write(Offset.Food, 99999)
    process.write(Offset.Dolt, 99999)
    process.write(Offset.Rifle, 99999)
    process.write(Offset.Shotgun, 99999)
    process.write(Offset.Medkit, 99999)