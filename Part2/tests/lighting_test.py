import unittest
from Part2 import lighting

TESTFILE = "Part2/tests/test_input.txt"


class LightingTest(unittest.TestCase):
    def test_turn_light_on(self):
        light = lighting.Light()
        light.turn_on()
        self.assertTrue(light.return_state())

    def test_turn_light_on_brightness(self):
        light = lighting.Light()
        light.turn_on()
        self.assertEqual(1, light.return_brightness())

    def test_turn_light_off(self):
        light = lighting.Light()
        light.turn_on()
        light.turn_off()
        self.assertFalse(light.return_state())

    def test_turn_light_off_brightness(self):
        light = lighting.Light()
        light.turn_on()
        light.turn_off()
        self.assertEqual(0, light.return_brightness())

    def test_toggle_light_on(self):
        light = lighting.Light()
        light.toggle()
        self.assertTrue(light.return_state())

    def test_toggle_light_on_brightness(self):
        light = lighting.Light()
        light.toggle()
        self.assertEqual(2, light.return_brightness())

    def test_toggle_light_off(self):
        light = lighting.Light()
        light.turn_on()
        light.toggle()
        self.assertTrue(light.return_state())

    def test_toggle_light_off_brightness(self):
        light = lighting.Light()
        light.turn_on()
        light.toggle()
        self.assertEqual(3, light.return_brightness())

    def test_display(self):
        display = lighting.Display(5, 5)
        self.assertEqual(0, display.number_of_lights_on())

    def test_turn_display_on(self):
        display = lighting.Display(5, 5)
        display.turn_on(0, 4, 0, 4)
        self.assertEqual(25, display.number_of_lights_on())

    def test_turn_one_on(self):
        display = lighting.Display(5, 5)
        display.turn_on(0, 0, 0, 0)
        self.assertEqual(1, display.number_of_lights_on())

    def test_turn_display_off(self):
        display = lighting.Display(5, 5)
        display.turn_on(0, 4, 0, 4)
        display.turn_off(0, 4, 0, 4)
        self.assertEqual(0, display.number_of_lights_on())

    def test_display_one_row(self):
        display = lighting.Display(5, 5)
        display.turn_on(0, 0, 0, 4)
        self.assertEqual(5, display.number_of_lights_on())

    def test_display_toggle(self):
        display = lighting.Display(5, 5)
        # Turn all of the lights on
        display.turn_on(0, 4, 0, 4)
        # Toggle one row
        display.toggle(1, 1, 0, 4)
        self.assertEqual(25, display.number_of_lights_on())

    def test_sequence_part_one(self):
        display = lighting.Display(1000, 1000)
        display.turn_on(0, 999, 0, 999)
        self.assertEqual(1000000, display.number_of_lights_on())

    def test_sequence_part_two(self):
        display = lighting.Display(1000, 1000)
        display.turn_on(0, 999, 0, 999)
        display.turn_off(499, 500, 499, 500)
        self.assertEqual(999996, display.number_of_lights_on())

    def test_sequence_part_three(self):
        display = lighting.Display(1000, 1000)
        display.turn_on(0, 999, 0, 999)
        display.turn_off(499, 500, 499, 500)
        display.toggle(0, 999, 499, 500)
        self.assertEqual(1003996, display.number_of_lights_on())

    def test_read_file(self):
        output = lighting.number_lights_on_from_file(TESTFILE, 1000, 1000)
        self.assertEqual(1003996, output)

    def test_sequence_part_three_brightness(self):
        display = lighting.Display(1000, 1000)
        display.turn_on(0, 999, 0, 999)
        display.turn_off(499, 500, 499, 500)
        display.toggle(0, 999, 499, 500)
        self.assertEqual(1003996, display.return_total_brightness())

    def test_read_file_brightness(self):
        output = lighting.brightness_from_file(TESTFILE, 1000, 1000)
        self.assertEqual(1003996, output)
