 ##################
# FILL IN HEADER
#################

import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=10, length =100)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)


# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
print('start')


while True:
    incoming = radio.receive() # Read from radio

    if incoming is not None: # message was received
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)
        data_acc=incoming
        data_acc=data_acc.split()
        data_x=data_acc[0]
        data_x=float(data_x)
        data_y=data_acc[1]
        data_y=float(data_y)
        data_z=data_acc[2]
        data_z=float(data_z)
        data_t=data_acc[3]
        data_t=float(data_t)
        print((data_x, data_y, data_z, data_t))
        #############################################################
        # FILL IN HERE
        # Incoming is string sent from logger
        # Need to parse it and reformat as a tuple for the MU plotter
        #############################################################
        mb.sleep(50)