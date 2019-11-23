import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def ros_to_matplotlib(coord, map_resolution, map_size):
    return (coord[0]/map_resolution + map_size, -1*coord[1]/map_resolution + map_size)


def add_points_to_map(image_path, map_resolution, map_size, positions):
    dpi = 120

    # Read our image
    im_data = mpimg.imread(image_path)

    # Get image dimensions so resulting image is the same
    height, width, nbands = im_data.shape
    figsize = width / float(dpi), height / float(dpi)
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')

    # Show image
    ax.imshow(im_data, interpolation='nearest')

    # Add all markers
    for coord in positions:
        x, y = ros_to_matplotlib(
            (coord['x'], coord['y']), map_resolution, map_size)
        plt.scatter(x, y, s=50, c='red', marker='o', picker=5)

    # Save figure with the original but as png
    fig.savefig(image_path.replace("pgm", "png"), dpi=dpi, transparent=True)

    plt.show()
