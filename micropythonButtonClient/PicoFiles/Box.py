from machine import Pin

class Box:
    light: Pin = None
    button: Pin = None

    def __init__(self, light_pin, button_pin):
        self.light = Pin(light_pin, Pin.OUT)
        self.button = Pin(button_pin, Pin.IN, Pin.PULL_UP)

    def light_on(self) -> None:
        self.light.on()

    def light_off(self) -> None:
        self.light.off()

    def toggle(self) -> None:
        self.light.value(not self.light.value())

    def is_pressed(self):
        return self.button.value() == 0
