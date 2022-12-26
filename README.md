Na wstępie muszę powiedzieć, nie znam ani Pythona, ani C++.
Sterownik chyba działa, po wydaniu komendy w Pythonie, sterownik odpowiada, uruchamia silnik.


>>> import smbus
>>> import struct
>>> i2c=smbus.SMBus(1)
>>> struct.unpack('f',bytearray(i2c.read_i2c_block_data(0x41,14,4)))

(-51.0,)


pico loguje:
[14]
reading
-51


Niestety nie wiem jak przechwycić wiadomość w C++, kod zwraca 0, Gdzieś czytałem, że trzeba przesunąć bity, ale nie wiem jak to zrobić, co gorsza nie wiem gdzie to czytałem.

lolo@lolo:~/i2c$ ./i2c
0000 >> RAW
0

pico loguje:
[14]
reading
-51




