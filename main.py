
from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

def sample_numpy (e): 
    document.getElementById('output').innerHTML = ""

    cookies= np.array (['Mon', 'Tues', 'Web', 'Thurs', 'Fri', 'Sat', 'Sun'])
    sold_cookies = np.array([20, 20, 15, 30, 42, 20, 25])

    fig, ax = plt.subplots()
    ax.plot(cookies, sold_cookies, marker='o', linestyle='-', color='b')
    ax.set_title("Dubai Chewy Cookies Sold Per Day!")

    display(fig, target='output')