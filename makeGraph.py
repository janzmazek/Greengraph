from matplotlib import pyplot as plt
from greengraph import Greengraph

def MakeGraph(start, end, steps, out=False):
    '''
    Generate a plot of green pixels intensity between two locations.
    Parameters
    ---------
    start: str
        Start location name (e.g. Ljubljana)
    end: str
        End location name (e.g. London)
    steps: int
        Number of points between start location and end location
    out: str
        Save as
    Returns
    ---------
    image
        A plot of green pixels intensity between two locations.
    '''


    mygraph = Greengraph(start, end)
    data = mygraph.green_between(steps+1)
    plt.plot(data)
    plt.xlabel("Steps")
    plt.ylabel("Green Pixel")

    if out:
        plt.savefig(out)
    else:
        plt.show()