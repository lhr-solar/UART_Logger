import serial
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--port')
args = parser.parse_args()

with serial.Serial(port=args.port, baudrate=115200) as ser:
    while True:
        with open('uart_log.bin', 'ab') as log:
            log.write(ser.readline())
