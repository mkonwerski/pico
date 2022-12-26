import gc
from micropython import const
import struct
from machine import Pin
from motor import Motor, motor2040
from encoder import Encoder, MMME_CPR
from pimoroni import Analog, AnalogMux

# https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/modules/motor
# https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/modules/encoder
# https://learn.adafruit.com/improve-brushed-dc-motor-performance

CHANEL_A = 0
CHANEL_B = 1
CHANEL_C = 2
CHANEL_D = 3
VOLTAGE_CHANEL_A1 = 0
VOLTAGE_CHANEL_A2 = 1

ENCODER_CHANEL_A_COMMON_PIN = 10
ENCODER_CHANEL_B_COMMON_PIN = 11
ENCODER_CHANEL_C_COMMON_PIN = 12
ENCODER_CHANEL_D_COMMON_PIN = 13
ENCODER_CHANEL_A_COUNT = 14
ENCODER_CHANEL_B_COUNT = 15
ENCODER_CHANEL_C_COUNT = 16
ENCODER_CHANEL_D_COUNT = 17
ENCODER_CHANEL_A_DELTA = 18
ENCODER_CHANEL_B_DELTA = 19
ENCODER_CHANEL_C_DELTA = 20
ENCODER_CHANEL_D_DELTA = 21
ENCODER_CHANEL_A_STEP = 22
ENCODER_CHANEL_B_STEP = 23
ENCODER_CHANEL_C_STEP = 24
ENCODER_CHANEL_D_STEP = 25
ENCODER_CHANEL_A_TURN = 26
ENCODER_CHANEL_B_TURN = 27
ENCODER_CHANEL_C_TURN = 28
ENCODER_CHANEL_D_TURN = 29
ENCODER_CHANEL_A_REVOLUTIONS = 30
ENCODER_CHANEL_B_REVOLUTIONS = 31
ENCODER_CHANEL_C_REVOLUTIONS = 32
ENCODER_CHANEL_D_REVOLUTIONS = 33
ENCODER_CHANEL_A_DEGREES = 34
ENCODER_CHANEL_B_DEGREES = 35
ENCODER_CHANEL_C_DEGREES = 36
ENCODER_CHANEL_D_DEGREES = 37
ENCODER_CHANEL_A_RADIANS = 38
ENCODER_CHANEL_B_RADIANS = 39
ENCODER_CHANEL_C_RADIANS = 40
ENCODER_CHANEL_D_RADIANS = 41
ENCODER_CHANEL_A_DIRECTION = 42
ENCODER_CHANEL_B_DIRECTION = 43
ENCODER_CHANEL_C_DIRECTION = 44
ENCODER_CHANEL_D_DIRECTION = 45
ENCODER_CHANEL_A_COUNT_PER_PRE = 46
ENCODER_CHANEL_B_COUNT_PER_PRE = 47
ENCODER_CHANEL_C_COUNT_PER_PRE = 48
ENCODER_CHANEL_D_COUNT_PER_PRE = 49
VOLTAGE = 50
AMPERE_CHANEL_A = 51
AMPERE_CHANEL_B = 52
AMPERE_CHANEL_C = 53
AMPERE_CHANEL_D = 54
IS_FAULT = 55

# Get Moto
MOTOR_SPEED_CHANEL_A = 56
MOTOR_SPEED_CHANEL_B = 56
MOTOR_SPEED_CHANEL_C = 57
MOTOR_SPEED_CHANEL_D = 58
MOTOR_DEADZONE_CHANEL_A = 59
MOTOR_DEADZONE_CHANEL_B = 60
MOTOR_DEADZONE_CHANEL_C = 61
MOTOR_DEADZONE_CHANEL_D = 62
MOTOR_FREQUENCY_CHANEL_A = 63
MOTOR_FREQUENCY_CHANEL_B = 64
MOTOR_FREQUENCY_CHANEL_C = 65
MOTOR_FREQUENCY_CHANEL_D = 66
MOTOR_DIRECION_CHANEL_A = 67
MOTOR_DIRECION_CHANEL_B = 68
MOTOR_DIRECION_CHANEL_C = 69
MOTOR_DIRECION_CHANEL_D = 70
MOTOR_ZEROPOINT_CHANEL_A = 71
MOTOR_ZEROPOINT_CHANEL_B = 72
MOTOR_ZEROPOINT_CHANEL_C = 73
MOTOR_ZEROPOINT_CHANEL_D = 74
MOTOR_SPEED_SCALE_CHANEL_A = 75
MOTOR_SPEED_SCALE_CHANEL_B = 76
MOTOR_SPEED_SCALE_CHANEL_C = 77
MOTOR_SPEED_SCALE_CHANEL_D = 78

# Set motor
ENABLE = 80
DISABLE = 81
SPEED = 82
FULL_NEGATIVE = 83
FULL_POSITIVE = 84
STOP_CHANEL = 85
STOP = 86
COAST = 87
COAST_CHANEL = 88
BRAKE = 89
BRAKE_CHANEL = 90
SPEED_SCALE = 91
ZEROPOINT = 92
TO_PERCENT = 93
TO_percent = 94
DUT = 95
DEDZONE = 96
FREQUENCY = 97
DIRECTION = 98

# --------- Encoder --------
GEAR_RATIO = 50
COUNTS_PER_REV = MMME_CPR * GEAR_RATIO
# gc.collect()

NUM_ENCODERS = 4
ENCODER_PINS = [motor2040.ENCODER_A, motor2040.ENCODER_B, motor2040.ENCODER_C, motor2040.ENCODER_D]
encoders = [Encoder(0, i, ENCODER_PINS[i], counts_per_rev=COUNTS_PER_REV, count_microsteps=True) for i in
            range(NUM_ENCODERS)]


def get_encoder_pins(pin):
    return encoders[pin].pins()


def get_encoder_common_pin(pin):
    return encoders[pin].common_pin()


def get_encoder_state(pin):
    return encoders[pin].state()


def get_encoder_count(pin):
    return encoders[pin].count()


def get_encoder_delta(pin):
    return encoders[pin].delta()


def get_encoder_zero(pin):
    return encoders[pin].zero()


def get_encoder_step(pin):
    return encoders[pin].step()


def get_encoder_turn(pin):
    return encoders[pin].turn()


def get_encoder_revolutions(pin):
    return encoders[pin].revolutions()


def get_encoder_degrees(pin):
    return encoders[pin].degrees()


def get_encoder_radians(pin):
    return encoders[pin].radians()


def get_encoder_direction(pin):
    return encoders[pin].direction()


def get_encoder_counts_per_rev(pin):
    return encoders[pin].counts_per_rev()


def get_encoder_capture(pin):
    return encoders[pin].capture()


# -------- Voltage --------
sensor_adc = Analog(motor2040.SHARED_ADC)
voltage_adc = Analog(motor2040.SHARED_ADC, motor2040.VOLTAGE_GAIN)
current_adc = Analog(motor2040.SHARED_ADC, motor2040.CURRENT_GAIN, motor2040.SHUNT_RESISTOR, motor2040.CURRENT_OFFSET)

mux = AnalogMux(motor2040.ADC_ADDR_0, motor2040.ADC_ADDR_1, motor2040.ADC_ADDR_2, muxed_pin=Pin(motor2040.SHARED_ADC))

sensor_addrs = list(range(motor2040.SENSOR_1_ADDR, motor2040.SENSOR_2_ADDR + 1))
for addr in sensor_addrs:
    mux.configure_pull(addr, Pin.PULL_DOWN)

mux.configure_pull(motor2040.FAULT_SENSE_ADDR, Pin.PULL_UP)


# -------- Voltage --------
def get_voltage_sensor(chanel):
    mux.select(chanel + motor2040.SENSOR_1_ADDR)
    return round(sensor_adc.read_voltage(), 3)


def get_voltage():
    mux.select(motor2040.VOLTAGE_SENSE_ADDR)
    return round(voltage_adc.read_voltage(), 3)


def get_ampere_sensor(chanel):
    mux.select(chanel + motor2040.CURRENT_SENSE_A_ADDR)
    return round(current_adc.read_current(), 3)


def is_fault():
    mux.select(motor2040.FAULT_SENSE_ADDR)
    return not mux.read()


# -------- Sensor reading --------
def sensor_reading(request):
    if request == ENCODER_CHANEL_A_COMMON_PIN:
        msg = get_encoder_common_pin(CHANEL_A)
    elif request == ENCODER_CHANEL_B_COMMON_PIN:
        msg = get_encoder_common_pin(CHANEL_B)
    elif request == ENCODER_CHANEL_C_COMMON_PIN:
        msg = get_encoder_common_pin(CHANEL_C)
    elif request == ENCODER_CHANEL_D_COMMON_PIN:
        msg = get_encoder_common_pin(CHANEL_D)
    elif request == ENCODER_CHANEL_A_COUNT:
        msg = get_encoder_count(CHANEL_A)
    elif request == ENCODER_CHANEL_B_COUNT:
        msg = get_encoder_count(CHANEL_B)
    elif request == ENCODER_CHANEL_C_COUNT:
        msg = get_encoder_count(CHANEL_C)
    elif request == ENCODER_CHANEL_D_COUNT:
        msg = get_encoder_count(CHANEL_D)
    elif request == ENCODER_CHANEL_A_DELTA:
        msg = get_encoder_delta(CHANEL_A)
    elif request == ENCODER_CHANEL_B_DELTA:
        msg = get_encoder_delta(CHANEL_B)
    elif request == ENCODER_CHANEL_C_DELTA:
        msg = get_encoder_delta(CHANEL_C)
    elif request == ENCODER_CHANEL_D_DELTA:
        msg = get_encoder_delta(CHANEL_D)
    elif request == ENCODER_CHANEL_A_STEP:
        msg = get_encoder_step(CHANEL_A)
    elif request == ENCODER_CHANEL_B_STEP:
        msg = get_encoder_step(CHANEL_B)
    elif request == ENCODER_CHANEL_C_STEP:
        msg = get_encoder_step(CHANEL_C)
    elif request == ENCODER_CHANEL_D_STEP:
        msg = get_encoder_step(CHANEL_D)
    elif request == ENCODER_CHANEL_A_TURN:
        msg = get_encoder_turn(CHANEL_A)
    elif request == ENCODER_CHANEL_B_TURN:
        msg = get_encoder_turn(CHANEL_B)
    elif request == ENCODER_CHANEL_C_TURN:
        msg = get_encoder_turn(CHANEL_C)
    elif request == ENCODER_CHANEL_D_TURN:
        msg = get_encoder_turn(CHANEL_D)
    elif request == ENCODER_CHANEL_A_DIRECTION:
        msg = get_encoder_direction(CHANEL_A)
    elif request == ENCODER_CHANEL_B_DIRECTION:
        msg = get_encoder_direction(CHANEL_B)
    elif request == ENCODER_CHANEL_C_DIRECTION:
        msg = get_encoder_direction(CHANEL_C)
    elif request == ENCODER_CHANEL_D_DIRECTION:
        msg = get_encoder_direction(CHANEL_D)
    elif request == ENCODER_CHANEL_A_REVOLUTIONS:
        msg = get_encoder_revolutions(CHANEL_A)
    elif request == ENCODER_CHANEL_B_REVOLUTIONS:
        msg = get_encoder_revolutions(CHANEL_B)
    elif request == ENCODER_CHANEL_C_REVOLUTIONS:
        msg = get_encoder_revolutions(CHANEL_C)
    elif request == ENCODER_CHANEL_D_REVOLUTIONS:
        msg = get_encoder_revolutions(CHANEL_D)
    elif request == ENCODER_CHANEL_A_DEGREES:
        msg = get_encoder_degrees(CHANEL_A)
    elif request == ENCODER_CHANEL_B_DEGREES:
        msg = get_encoder_degrees(CHANEL_B)
    elif request == ENCODER_CHANEL_C_DEGREES:
        msg = get_encoder_degrees(CHANEL_C)
    elif request == ENCODER_CHANEL_D_DEGREES:
        msg = get_encoder_degrees(CHANEL_D)
    elif request == ENCODER_CHANEL_A_RADIANS:
        msg = get_encoder_radians(CHANEL_A)
    elif request == ENCODER_CHANEL_B_RADIANS:
        msg = get_encoder_radians(CHANEL_B)
    elif request == ENCODER_CHANEL_C_RADIANS:
        msg = get_encoder_radians(CHANEL_C)
    elif request == ENCODER_CHANEL_D_RADIANS:
        msg = get_encoder_radians(CHANEL_D)
    elif request == ENCODER_CHANEL_A_COUNT_PER_PRE:
        msg = get_encoder_counts_per_rev(CHANEL_A)
    elif request == ENCODER_CHANEL_B_COUNT_PER_PRE:
        msg = get_encoder_counts_per_rev(CHANEL_B)
    elif request == ENCODER_CHANEL_C_COUNT_PER_PRE:
        msg = get_encoder_counts_per_rev(CHANEL_C)
    elif request == ENCODER_CHANEL_D_COUNT_PER_PRE:
        msg = get_encoder_counts_per_rev(CHANEL_D)
    elif request == VOLTAGE:
        msg = get_voltage()
    elif request == VOLTAGE_CHANEL_A1:
        msg = get_voltage_sensor(VOLTAGE_CHANEL_A1)
    elif request == VOLTAGE_CHANEL_A2:
        msg = get_voltage_sensor(VOLTAGE_CHANEL_A2)
    elif request == AMPERE_CHANEL_A:
        msg = get_ampere_sensor(CHANEL_A)
    elif request == AMPERE_CHANEL_B:
        msg = get_ampere_sensor(CHANEL_B)
    elif request == AMPERE_CHANEL_C:
        msg = get_ampere_sensor(CHANEL_C)
    elif request == AMPERE_CHANEL_D:
        msg = get_ampere_sensor(CHANEL_D)
    elif request == IS_FAULT:
        msg = is_fault()
    elif request == MOTOR_SPEED_CHANEL_A:
        msg = get_motor_speed(CHANEL_A)
    elif request == MOTOR_SPEED_CHANEL_B:
        msg = get_motor_speed(CHANEL_B)
    elif request == MOTOR_SPEED_CHANEL_C:
        msg = get_motor_speed(CHANEL_C)
    elif request == MOTOR_SPEED_CHANEL_D:
        msg = get_motor_speed(CHANEL_D)
    elif request == MOTOR_DEADZONE_CHANEL_A:
        msg = get_motor_deadzone(CHANEL_A)
    elif request == MOTOR_DEADZONE_CHANEL_B:
        msg = get_motor_deadzone(CHANEL_B)
    elif request == MOTOR_DEADZONE_CHANEL_C:
        msg = get_motor_deadzone(CHANEL_C)
    elif request == MOTOR_DEADZONE_CHANEL_D:
        msg = get_motor_deadzone(CHANEL_D)
    elif request == MOTOR_FREQUENCY_CHANEL_A:
        msg = get_motor_frequency(CHANEL_A)
    elif request == MOTOR_FREQUENCY_CHANEL_B:
        msg = get_motor_frequency(CHANEL_B)
    elif request == MOTOR_FREQUENCY_CHANEL_C:
        msg = get_motor_frequency(CHANEL_C)
    elif request == MOTOR_FREQUENCY_CHANEL_D:
        msg = get_motor_frequency(CHANEL_D)
    elif request == MOTOR_DIRECION_CHANEL_A:
        msg = get_motor_direction(CHANEL_A)
    elif request == MOTOR_DIRECION_CHANEL_B:
        msg = get_motor_direction(CHANEL_B)
    elif request == MOTOR_DIRECION_CHANEL_C:
        msg = get_motor_direction(CHANEL_C)
    elif request == MOTOR_DIRECION_CHANEL_D:
        msg = get_motor_direction(CHANEL_D)
    elif request == MOTOR_ZEROPOINT_CHANEL_A:
        msg = get_motor_zeropoint(CHANEL_A)
    elif request == MOTOR_ZEROPOINT_CHANEL_B:
        msg = get_motor_zeropoint(CHANEL_B)
    elif request == MOTOR_ZEROPOINT_CHANEL_C:
        msg = get_motor_zeropoint(CHANEL_C)
    elif request == MOTOR_ZEROPOINT_CHANEL_D:
        msg = get_motor_zeropoint(CHANEL_D)
    elif request == MOTOR_SPEED_SCALE_CHANEL_A:
        msg = get_motor_speed_scale(CHANEL_A)
    elif request == MOTOR_SPEED_SCALE_CHANEL_B:
        msg = get_motor_speed_scale(CHANEL_B)
    elif request == MOTOR_SPEED_SCALE_CHANEL_C:
        msg = get_motor_speed_scale(CHANEL_C)
    elif request == MOTOR_SPEED_SCALE_CHANEL_D:
        msg = get_motor_speed_scale(CHANEL_D)
    else:
        msg = 9999
    return msg


# -------- Motor --------
MOTOR_PINS = [motor2040.MOTOR_A, motor2040.MOTOR_B, motor2040.MOTOR_C, motor2040.MOTOR_D]
motors = [Motor(pins) for pins in MOTOR_PINS]


def enable_motors():
    for m in motors:
        m.enable()


def disable_motors():
    for m in motors:
        m.disable()


def set_motor_speed(pin, speed):
    motors[pin].speed(speed/100)


# ------
def get_motor_speed(pin):
    return motors[pin].speed()


def set_motor_full_negative(pin):
    motors[pin].full_negative()


def set_motor_full_positive(pin):
    motors[pin].full_positive()


# ------
def get_motor_speed_scale(pin):
    return motors[pin].speed_scale()


def set_motor_stop(pin):
    motors[pin].stop()


def set_motors_stop():
    for m in motors:
        m.stop()


def set_motor_coast(pin):
    motors[pin].coast()


def set_motors_coast():
    for m in motors:
        m.coast()


def set_motor_brake(pin):
    motors[pin].brake()


def set_motors_brake():
    for m in motors:
        m.brake()


def set_motor_speed_scale(pin, speed_scale):
    motors[pin].speed_scale(speed_scale/100)


# ------
def get_motor_speed_scale(pin):
    return motors[pin].speed_scale()


def set_motor_zeropoint(pin, zeropoint):
    motors[pin].zeropoint(zeropoint/100)


# ------
def get_motor_zeropoint(pin):
    return motors[pin].zeropoint()


def set_motor_to_percent(pin, value):
    motors[pin].to_percent(value)


def set_motor_to_percent(pin, value, value_min=0, value_max=100):
    motors[pin].to_percent(value, value_min, value_max)


def set_motor_duty(pin, duty):
    motors[pin].duty(duty)


def set_motor_deadzone(pin, deadzone):
    motors[pin].deadzone(deadzone)


# ------
def get_motor_deadzone(pin):
    return motors[pin].deadzone()


def set_motor_frequency(pin, frequency):
    motors[pin].frequency(frequency)


# ------
def get_motor_frequency(pin):
    return motors[pin].frequency()


def set_motor_direction(pin):
    motors[pin].direction(motor2040.REVERSED_DIR)


# ------
def get_motor_direction(pin):
    return motors[pin].direction()


def writing(request, chanel, value):
    if request == ENABLE:
        enable_motors()
    elif request == DISABLE:
        disable_motors()
    elif request == SPEED:
        set_motor_speed(chanel, value)
    elif request == FULL_NEGATIVE:
        set_motor_full_negative(chanel)
    elif request == FULL_POSITIVE:
        set_motor_full_positive(chanel)
    elif request == STOP_CHANEL:
        set_motor_stop(chanel)
    elif request == STOP:
        set_motors_stop()
    elif request == COAST_CHANEL:
        set_motor_coast(chanel)
    elif request == COAST:
        set_motors_coast()
    elif request == BRAKE_CHANEL:
        set_motor_brake(chanel)
    elif request == BRAKE:
        set_motors_brake()
    elif request == SPEED_SCALE:
        set_motor_speed_scale(chanel, value)
    elif request == ZEROPOINT:
        set_motor_zeropoint(chanel, value)
    elif request == TO_PERCENT:
        set_motor_to_percent(chanel, value)
    elif request == TO_percent:
        set_motor_to_percent(chanel, value)
    elif request == DUT:
        set_motor_duty(chanel, value)
    elif request == DEDZONE:
        set_motor_deadzone(chanel, value)
    elif request == FREQUENCY:
        set_motor_frequency(chanel, value)
    elif request == DIRECTION:
        set_motor_direction(chanel)