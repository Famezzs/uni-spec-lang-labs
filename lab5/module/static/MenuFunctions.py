from module.InputScanner import InputScanner
from module.ArtGenerator import ArtGenerator
from module.ArtPrinter import ArtPrinter
from module.ArtScaler import ArtScaler
from module.static.ArtGeneratorConfiguration import ArtGeneratorConfiguration

class MenuFunctions:
    @staticmethod
    def draw_figure():
        width = float(InputScanner.scan('Width: '))
        length = float(InputScanner.scan('Length: '))
        height = float(InputScanner.scan('Height: '))
        color = InputScanner.scan('Color: ')
        x_axes_angle_coefficient = InputScanner.scan('X Axes Angle Coefficient (defaults to 0.5): ', allow_empty=True)
        y_axes_angle_coefficient = InputScanner.scan('Y Axes Angle Coefficient (defaults to 0.5): ', allow_empty=True)

        if InputScanner.input_empty(x_axes_angle_coefficient):
            x_axes_angle_coefficient = ArtGenerator.x_axes_default_coefficient
        else:
            x_axes_angle_coefficient = float(x_axes_angle_coefficient)

        if InputScanner.input_empty(y_axes_angle_coefficient):
            y_axes_angle_coefficient = ArtGenerator.y_axes_default_coefficient
        else:
            y_axes_angle_coefficient = float(y_axes_angle_coefficient)

        art_generator = ArtGenerator(x_axes_angle_coefficient, y_axes_angle_coefficient)

        art_generator.draw_parallelepiped(width, length, height, color)

    @staticmethod
    def exit_programme():
        exit(0)
