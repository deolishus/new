from gpiozero import LED
from signal import pause

red = LED(17)

def redlight():

    while True:
        print("\n")
        number = int(input("Type a number:> "))
        print("\n")

        if 1 <= number < 5:
            red.on()
            print("Light on!")
        elif number == 0:
            red.blink()
            print("Light blinks!")
        else:
            red.off()
            print("Light off!")

redlight()
