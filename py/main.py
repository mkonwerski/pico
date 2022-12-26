import driver
from i2cSlave import i2c_slave


i2c = i2c_slave(0, sda_gpio=20, scl_gpio=21, responder_address=0x41)

try:
    while True:

        if i2c.write_data_is_available():
            request = i2c.get_write_data(3)
            print(request)
            if len(request) == 1:
                print('reading')
                msg = driver.sensor_reading(request[0])
                print(msg)
                i2c.send(msg)
            elif len(request) == 3:
                print('write')
                driver.writing(request[0], request[1], request[2])


except KeyboardInterrupt:
    pass