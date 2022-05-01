import re

FILENAME = "coding_challenge_input.txt"


class Light:
    """Creates a light object, initially turned off"""

    def __init__(self):
        self.brightness = 0

    def turn_on(self):
        """Turns on the light"""
        self.brightness += 1

    def turn_off(self):
        """Turns off the light"""
        if self.brightness != 0:
            self.brightness -= 1

    def return_state(self):
        """Returns the state of the light"""
        if self.brightness > 0:
            return True
        else:
            return False

    def return_brightness(self):
        """Returns the brightness of the light"""
        return self.brightness

    def toggle(self):
        """Toggles the light on/off"""
        self.brightness += 2


class Display:
    """
    Creates a matrix of lights
    Parameters:
    width : int
        width of the matrix
    height : int
        height of the matrix
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.lighting_matrix = []
        for row in range(height):
            self.lighting_matrix.append([])
            for column in range(width):
                self.lighting_matrix[row].append(Light())

    def turn_on(self, row_start, row_end, column_start, column_end):
        """
        Turns on the lights between the given coordinates
        row_start : int
        row_end : int
        column_start : int
        column_end : int
        """
        for row in range(row_start, row_end + 1):
            for column in range(column_start, column_end + 1):
                self.lighting_matrix[row][column].turn_on()

    def turn_off(self, row_start, row_end, column_start, column_end):
        """
        Turns off the lights between the given coordinates
        row_start : int
        row_end : int
        column_start : int
        column_end : int
        """
        for row in range(row_start, row_end + 1):
            for column in range(column_start, column_end + 1):
                self.lighting_matrix[row][column].turn_off()

    def toggle(self, row_start, row_end, column_start, column_end):
        """
        Toggles the lights between the given coordinates
        row_start : int
        row_end : int
        column_start : int
        column_end : int
        """
        for row in range(row_start, row_end + 1):
            for column in range(column_start, column_end + 1):
                self.lighting_matrix[row][column].toggle()

    def number_of_lights_on(self):
        """Returns the number of lights turned on"""
        result = 0
        for row in range(self.height):
            for column in range(self.width):
                if (self.lighting_matrix[row][column].return_state()):
                    result += 1
        return result

    def return_total_brightness(self):
        """Returns the total brightness"""
        result = 0
        for row in range(self.height):
            for column in range(self.width):
                result += self.lighting_matrix[row][column].return_brightness()
        return result

def read_file(file_path, display):
    """
    Reads a file, runs the instructions from it and returns the display
    file_path : string
    display : a display object
    """
    with open(file_path, 'r') as file:
        for line in file:
            # get the coordinates first
            coords = re.findall(r'\d+', line)
            row_start = int(coords[0])
            row_end = int(coords[2])
            column_start = int(coords[1])
            column_end = int(coords[3])
            # parse out the instructions
            if (line.startswith("turn on")):
                display.turn_on(row_start, row_end, column_start, column_end)
            elif (line.startswith("turn off")):
                display.turn_off(row_start, row_end, column_start, column_end)
            elif (line.startswith("toggle")):
                display.toggle(row_start, row_end, column_start, column_end)
    return display


def number_lights_on_from_file(file_path, width, height):
    """
    Reads a file and returns the number of lights on at the end of the set of instructions
    Parameters:
    file_path : string
    width : int width of display
    height : int height of display
    """
    display = read_file(file_path, Display(width, height))
    return display.number_of_lights_on()


def brightness_from_file(file_path, width, height):
    """
    Reads a file and returns the total brightness of lights on at the end of the set of instructions
    Added as the instructions asked for total number of lights on but the example returned the total brightness
    Parameters:
    file_path : string
    width : int width of display
    height : int height of display
    """
    display = read_file(file_path, Display(width, height))
    return display.return_total_brightness()


def main():
    # if the total brightness is required:
    print(brightness_from_file(FILENAME, 1000, 1000))
    # gives an answer of 1716513
    # if the total number of lights on at the end is required:
    print(number_lights_on_from_file(FILENAME, 1000, 1000))
    # gives an answer of 658257

if __name__ == "__main__":
    main()
