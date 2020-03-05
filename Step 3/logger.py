##################
# FILL IN HEADER
#################

import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=10, length=100)

print('Program Started')
mb.display.show(mb.Image.HAPPY)

while not mb.button_a.is_pressed():  # wait for button A to be pressed to begin logging
    mb.sleep(10)

radio.send('start') # Send the word 'start' to start the receiver
mb.sleep(1000)
mb.display.show(mb.Image.HEART)  # Display Heart while logging


# Read and send accelerometer data repeatedly until button A is pressed again
time0=mb.running_time()
while not mb.button_a.is_pressed():
    x=mb.accelerometer.get_x()
    y=mb.accelerometer.get_y()
    z=mb.accelerometer.get_z()
    elapsed_time=mb.running_time()-time0
    elapsed_time=elapsed_time/1000
    message=x, y, z, elapsed_time
    message=str(message)
    ######################################################
    # FILL In HERE
    # Need to collect accelerometer and time measurements
    # Need to format into a single string
    # Send the string over the radio
    ######################################################
    radio.send(message)
    mb.sleep(500)



mb.display.show(mb.Image.SQUARE)  # Display Square when program ends