import serial
import csv
import time

# 1. Initialize Peripheral
ser = serial.Serial('COM5', 9600, timeout=1)
ser.flushInput()

# 2. Open File (Write mode)
f = open('energy_data.csv', 'w', newline='')
writer = csv.writer(f) # Create a CSV writer object for clean formatting
# Write the header row
writer.writerow(['Timestamp', 'Current_Amps', 'Power_Watts'])
try:
    while True:
        line = ser.readline() # Grab the raw bytes
    
        if line and b',' in line: # Only process if we actually received data
            decoded_line = line.decode('utf-8').strip()
            data = decoded_line.split(',')
            
            # 4. Rigorous Testing: Add a Timestamp
            timestamp = time.strftime('%H:%M:%S')
            data.insert(0, timestamp) # Put the time at the start of the list
            
            # 5. Data Persistence
            writer.writerow(data)
            f.flush() # Forces Windows to save the file immediately so you don't lose data if it crashes
            
            print(f"Logged: {data}") # Visual feedback for the engineer
except KeyboardInterrupt:
    print("Logging stopped by user.")
finally:
    f.close()
    ser.close()

