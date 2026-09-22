from microcontroller import Pin

from neopixel import NeoPixel
from config.pins import LED_RING_DATA, NUM_PIXELS, RED, GREEN, YELLOW, BLUE

from time import sleep



class RgbRing():
  
  def __init__(self):
    self.neopixel = NeoPixel(Pin(LED_RING_DATA), NUM_PIXELS,
                             brightness=0.3, auto_write=False)
    
  def _wheel(self, pos):
    """Return the RGB colour at a position in the colour wheel."""
    pos %= 256

    if pos < 85:
      return (pos * 3, 255 - pos * 3, 0)
    if pos < 170:
      pos -= 85
      return (255 - pos * 3, 0, pos * 3)

    pos -= 170
    return (0, pos * 3, 255 - pos * 3)
    
  def rainbow_cycle(self):
    for j in range(255):
        for i in range(NUM_PIXELS):
            pixel_index = (i * 256 // NUM_PIXELS) + j
            self.neopixel[i] = self._wheel(pixel_index & 255)
        self.neopixel.show()
        
  def loading(self, cycles=3, tail=5, delay=0.04):
    """Spin a fading rainbow comet around the ring, once per cycle."""
    for step in range(cycles * NUM_PIXELS):
      self.neopixel.fill(0)
      for t in range(tail):
        r, g, b = self._wheel((step + t) * 256 // NUM_PIXELS)
        fade = (tail - t) / tail
        self.neopixel[(step - t) % NUM_PIXELS] = (
          int(r * fade), int(g * fade), int(b * fade))
      self.neopixel.show()
      sleep(delay)
    self.neopixel.fill(0)
    self.neopixel.show()

  def fill_color(self, color: int):
    self.neopixel.fill(color)
    self.neopixel.show()
  
  def deinit(self):
    self.neopixel.deinit()