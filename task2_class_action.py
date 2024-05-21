import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy


def read_coordinates_from_file(filename):
    points = []
    with open(filename, 'r') as file:
        # Skip the header line
        next(file)
        for line in file:
            x, y = map(float, line.strip().split(','))  # Split by comma
            points.append(Point(x, y))
    return points



def plot_points(points, color='blue'):
    x_values = [point.x for point in points]
    y_values = [point.y for point in points]
    plt.scatter(x_values, y_values, color=color)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot of Points')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    filename = "data.csv"
    points = read_coordinates_from_file(filename)
    plot_points(points)

    # Move the points
    dx = -19.2347
    dy = 28.9872
    for point in points:
        point.translate(dx, dy)

    # Plot the moved points in a different color
    plot_points(points, color='black')


