class FigureGenerator:
    """
    A class for generating the 2D isometric projection of a 3D parallelepiped using matplotlib.

    This class uses numpy arrays to define the projection vectors for the 3D axes and matplotlib
    to draw and color the parallelepiped.

    Attributes:
        x_axes_default_coefficient (float): Default coefficient for the x-axis in the isometric projection.
        y_axes_default_coefficient (float): Default coefficient for the y-axis in the isometric projection.
        x_vector (numpy.ndarray): The isometric projection vector for the x-axis.
        y_vector (numpy.ndarray): The isometric projection vector for the y-axis.
        z_vector (numpy.ndarray): The isometric projection vector for the z-axis.

    Methods:
        draw_parallelepiped(self, width, length, height, color='lightblue'): Draws a parallelepiped with the given dimensions and color.
    """

    x_axes_default_coefficient = 0.5
    y_axes_default_coefficient = 0.5

    def __init__(self, x_axes_coefficient=x_axes_default_coefficient, y_axes_coefficient=y_axes_default_coefficient):
        """
        Initializes the FigureGenerator with specific coefficients for the axes.

        Args:
            x_axes_coefficient (float, optional): Coefficient for the x-axis in the isometric projection. Defaults to x_axes_default_coefficient.
            y_axes_coefficient (float, optional): Coefficient for the y-axis in the isometric projection. Defaults to y_axes_default_coefficient.
        """
        import numpy as np
        # Defining the 2D isometric projection vectors for 3D axes
        # The value of "1" on the first axis means it moves 1 unit to the right for every unit of width
        self.x_vector = np.array([1, x_axes_coefficient])
        # The value of "-1" on the first axis means it moves 1 unit to the left for every unit of length
        self.y_vector = np.array([-1, y_axes_coefficient])
        # The value of "0" on the first axis means it doesn't move left or right; it remains vertically aligned
        self.z_vector = np.array([0, -1])

    def __calculate_parallelepiped_vertices(self, width, length, height):
        import numpy as np
        return [
            np.zeros(2),
            self.x_vector * width,
            self.y_vector * length,
            self.x_vector * width + self.y_vector * length,
            self.z_vector * height,
            self.x_vector * width + self.z_vector * height,
            self.y_vector * length + self.z_vector * height,
            self.x_vector * width + self.y_vector * length + self.z_vector * height
        ]

    @staticmethod
    def __name_points(axes, vertices):
        for i, v in enumerate(vertices):
            axes.plot(v[0], v[1], 'o')
            axes.text(v[0], v[1], f'P{i}', fontsize=12, verticalalignment='bottom')

    @staticmethod
    def __color_parallelepiped_projection(axes, vertices, color):
        # Coloring the sides (quadrilaterals)
        # Bottom
        axes.fill(*zip(*[vertices[0], vertices[1], vertices[3], vertices[2]]), color)
        # Top
        axes.fill(*zip(*[vertices[4], vertices[5], vertices[7], vertices[6]]), color)
        # Front
        axes.fill(*zip(*[vertices[0], vertices[1], vertices[5], vertices[4]]), color)
        # Back
        axes.fill(*zip(*[vertices[2], vertices[3], vertices[7], vertices[6]]), color)
        # Left
        axes.fill(*zip(*[vertices[0], vertices[2], vertices[6], vertices[4]]), color)
        # Right
        axes.fill(*zip(*[vertices[1], vertices[3], vertices[7], vertices[5]]), color)

    @staticmethod
    def __connect_parallelepiped_points(axes, vertices):
        # Connect vertices to draw the edges of the parallelepiped
        connections = [
            (0, 1), (0, 2), (1, 3), (2, 3),
            (0, 4), (1, 5), (2, 6), (3, 7),
            (4, 5), (4, 6), (5, 7), (6, 7)
        ]

        for start, end in connections:
            axes.plot([vertices[start][0], vertices[end][0]],
                      [vertices[start][1], vertices[end][1]], 'k-')

    def draw_parallelepiped(self, width, length, height, color='lightblue'):
        """
        Draws a parallelepiped with the given dimensions and color. It calculates the 2D projections 
        of the parallelepiped's vertices and uses matplotlib to draw and color it.

        Args:
            width (float): The width of the parallelepiped.
            length (float): The length of the parallelepiped.
            height (float): The height of the parallelepiped.
            color (str, optional): The color to fill the parallelepiped. Defaults to 'lightblue'.
        """
        import matplotlib.pyplot as plt
        # Calculate the 2D projections of the 8 vertices of the parallelepiped
        vertices = self.__calculate_parallelepiped_vertices(width, length, height)

        # Plot the vertices and edges
        _, axes = plt.subplots()

        # Name points of parallelepiped
        self.__name_points(axes, vertices)

        # Color sides of parallelepiped
        self.__color_parallelepiped_projection(axes, vertices, color)

        # Connect points of parallelepiped
        self.__connect_parallelepiped_points(axes, vertices)

        axes.set_aspect('equal', 'box')
        axes.axis('off')
        plt.show()
