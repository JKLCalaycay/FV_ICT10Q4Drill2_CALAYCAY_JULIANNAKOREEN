
from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

def sample_numpy (e): 
    document.getElementById('output').innerHTML = ""

    boxes= np.array (['Mon', 'Tues', 'Web', 'Thurs', 'Fri', 'Sat', 'Sun'])
    sold_boxes = np.array([20, 20, 15, 30, 42, 20, 25])

    fig, ax = plt.subplots()
    ax.plot(boxes, sold_boxes, marker='o', linestyle='-', color='b')
    ax.set_title("Dubai Chewy Cookies Sold Per Day!")

    display(fig, target='output')