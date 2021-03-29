import time
import board
import usb_hid
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kb = Keyboard(usb_hid.devices)

button_1 = digitalio.DigitalInOut(board.GP17)
button_1.direction = digitalio.Direction.INPUT
button_1.pull = digitalio.Pull.DOWN

button_2 = digitalio.DigitalInOut(board.GP16)
button_2.direction = digitalio.Direction.INPUT
button_2.pull = digitalio.Pull.DOWN

onboard_led = digitalio.DigitalInOut(board.GP25)
onboard_led.direction = digitalio.Direction.OUTPUT

led_rgb_1 = digitalio.DigitalInOut(board.GP22)
led_rgb_2 = digitalio.DigitalInOut(board.GP21)
led_rgb_3 = digitalio.DigitalInOut(board.GP20)

led_rgb_1.direction = digitalio.Direction.OUTPUT
led_rgb_2.direction = digitalio.Direction.OUTPUT
led_rgb_3.direction = digitalio.Direction.OUTPUT  

def keyboard_handle():
    
    while True:
        
        onboard_led.value = True
        led_rgb_3.value = True
        
        if button_1.value:
            
            kb.press(Keycode.CONTROL, Keycode.S)
            led_rgb_2.value = True
            time.sleep(0.1)
            kb.release(Keycode.CONTROL, Keycode.S)
            led_rgb_2.value = False
            time.sleep(0.1)
            
        if button_2.value:
            
            kb.press(Keycode.ALT, Keycode.TAB)
            led_rgb_2.value = True
            time.sleep(0.1)
            kb.release(Keycode.ALT, Keycode.TAB)
            led_rgb_2.value = False
            time.sleep(0.1)
            
def main():
    
    keyboard_handle()
    
main()