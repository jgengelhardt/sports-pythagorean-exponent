import matplotlib.pyplot as plt
from matplotlib import pylab
import numpy
import numpy.polynomial.polynomial as poly
import pandas as pd

plt.figure(figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

def plot_NHL_exponents():
    col_names = ['year','team','exponent']
    color = '#8394a1'
    df = pd.read_csv(f'./results/NHL_exponents.csv', header=0, encoding='ISO-8859-1')
    x = df['year']
    y = df['exponent']
    plt.scatter(x, y, c=color, alpha=0.1, label='NHL')
    coefs = poly.polyfit(x, y, 5)
    ffit = poly.polyval(sorted(x), coefs)
    pylab.plot(sorted(x),ffit,color)

    # design
    plt.title('What exponent should be used for NHL ice hockey?')
    plt.ylabel('Exponent')
    plt.ylim(0, 5)
    plt.xlabel('Season')
    plt.legend(loc=0)
    plt.show()
    
plot_NHL_exponents()