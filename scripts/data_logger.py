
import serial
import csv
import time

def log_data():
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    with open("sensor_data.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Temperature", "Humidity"])
        
        while True:
            line = ser.readline().decode().strip()
            if line:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                data = line.split(", ")
                writer.writerow([timestamp, data[0], data[1]])
                print(f"{timestamp} - {data[0]}, {data[1]}")
            time.sleep(1)

if __name__ == "__main__":
    log_data()
