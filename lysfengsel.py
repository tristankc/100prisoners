import time
import random as r
import math
import matplotlib.pyplot as plt


class Prisoner:

    captain = None
    visited = False

    def __init__(self, captain):
        self.captain = captain


# Utregning av
def math_expected(n):
    if n==1:
        return 1
    elif n<1:
        return -1
    tall = 0
    for i in range(1, n):
        tall += 1/i
    return n*(n-1) + n*tall


# Simulering med n fanger. Returnerer antall iterasjoner pakrevd for kaptein kan med sikkerhet si at alle har vaert innom rommet
def run_simulation(n):
    prisoners = [Prisoner(False) for i in range(n)]
    prisoners[r.randint(0, n-1)].captain = True
    confirmed_prisoners = 0
    lys = False
    iterations = 0
    while confirmed_prisoners <= n-2:
        iterations += 1
        ran = r.randint(0, n-1)
        prisoner = prisoners[ran]
        if prisoner.captain:
            if lys:
                lys = False
                prisoner.visited = True
                confirmed_prisoners += 1
        if not prisoner.visited and not prisoner.captain and not lys:
            lys = True
            prisoner.visited = True
    return iterations


# Simulering av statistikk. Samler n forsøk med m fanger hver gang
def run_statistic(n, m):
    av = 0
    xkord = []
    ykord = []
    for i in range(n):
        plottableNum = run_simulation(m)
        av += plottableNum
        ykord.append(av/(i+1))
        xkord.append(i)
        plot_values(xkord, ykord)
    show_plot(n)
    return av/n


# Plotting av verdier
def plot_values(xkord, ykord):
    plt.plot(xkord, ykord, 'ro')


# Visning av plot
def show_plot(n):
    plt.axis([0, n, 9500, 11500])
    plt.plot([0,n], [10418, 10418], color='k', linestyle='-', linewidth=2)
    plt.xlabel('Utførrelser')
    plt.ylabel('Dager')
    plt.show()


def main():
    prinumb = int(input("Antall fanger: "))
    s = int(input("Antall forsøk: "))
    statisticallyexpected = math_expected(prinumb).__round__()
    computedvalue = run_statistic(s, prinumb).__round__()
    print ("Statistisk forventet verdi: ", statisticallyexpected, "\nForventet verdi ut i fra forsøk: ", computedvalue, "\nDifferanse: ", abs(statisticallyexpected-computedvalue))

main()