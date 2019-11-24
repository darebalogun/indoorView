import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def ros_to_matplotlib(coord, map_resolution, map_size):
    """
    ROS map coordinates have the origin in the centre, while matplolib origin is upper left corner
    This method converts between the two

    Parameters
    ----------
    coord : tuple
        x y coordinates according to ros map (origin in the centre)
    map_resolution : float
        map resolution, set in rviz slam launch file
    map_size : int
        dimensions of map, set in rviz slam launch file, note: map is square
    """
    return (coord[0]/map_resolution + map_size/2, -1*coord[1]/map_resolution + map_size/2)


def add_points_to_map(image_path, map_resolution, map_size, positions):
    """
    Open the pgm file, plot the points of interest as a scatter then save as png

    Parameters
    ----------
    image_path : str
        path to image file (pgm)
    map_resolution : float
        map resolution, set in rviz slam launch file
    map_size : int
        dimensions of map, set in rviz slam launch file, note: map is square
    positions : list
        list of positions to be plotted
    """
    dpi = 300

    # Read our image
    im_data = mpimg.imread(image_path)

    # Get image dimensions so resulting image is the same
    height, width = im_data.shape
    figsize = width / float(dpi), height / float(dpi)
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')

    # Show image
    ax.imshow(im_data,
              cmap='gray', origin='upper', aspect='auto')
    plt.subplots_adjust(left=0, bottom=0, top=1.0, right=1.0)

    # Add all markers

    for coord in positions:
        x, y = ros_to_matplotlib(
            (coord['x'], coord['y']), map_resolution, map_size)
        plt.scatter(x, y, s=2, c='red', marker='o', picker=5)

    # Save figure with the original but as png
    fig.savefig(image_path.replace("pgm", "png"), dpi=dpi, transparent=True)
