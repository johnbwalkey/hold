# load code to Uno wi same filename
import serial
import time

# Establish a connection to the Arduino
arduino = serial.Serial('COM3', 9600) # Replace 'COM3' with your Arduino's serial port
time.sleep(2) # Wait for the connection to establish

def blink_led(duration, interval):
    """
    Blinks the LED connected to pin 13 of the Arduino.
    
    :param duration: Total duration to blink the LED in seconds
    :param interval: Interval between blinks in seconds
    """
    end_time = time.time() + duration
    while time.time() < end_time:
        arduino.write(b'H') # Turn LED on
        time.sleep(interval)
        arduino.write(b'L') # Turn LED off
        time.sleep(interval)

# Blink the LED for 10 seconds with a 3-second interval
blink_led(10, 3)

# Close the serial connection
arduino.close()
