#include <wiringPi.h>
#include <wiringPiI2C.h>
#include <iostream>

#include <typeinfo>
#include <string>

int main()

{
int fd = wiringPiI2CSetup(0x41);
        uint8_t tmp;

        uint16_t  value = wiringPiI2CReadReg8(fd, 14);

        printf("%.4X >> RAW\n", value);
        value = (value >> 8)  & 0xff | (tmp << 8)  & 0xE;

        printf("%u\n", (unsigned int)value);

   return 1;
}