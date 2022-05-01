import re

FILENAME = "coding_challenge_input.txt"


class Light:
    """Creates a light object, initially turned off"""

    def __init__(self):
        self.on = False

    def turn_on(self):
        """Turns on the light"""
        self.on = True

    def turn_off(self):
        """Turns off the light"""
        self.on = False

    def return_state(self):
        """Returns the state of the light"""
        return self.on

    def toggle(self):
        """Toggles the light on/off"""
        if self.on:
            self.on = False
        else:
            self.on = True


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


def run_instructions_from_file(file_path, width, height):
    """
    Reads a file and returns the number of lights on at the end of the set of instructions
    Parameters:
    file_path : string
    width : int width of display
    height : int height of display
    """
    display = Display(width, height)
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
    return display.number_of_lights_on()


def main():
    print(run_instructions_from_file(FILENAME, 1000, 1000))
    # Gives the answer 385705

if __name__ == "__main__":
    main()
