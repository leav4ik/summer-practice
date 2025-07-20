import json
import matplotlib.pyplot as plt
import sys

name = sys.argv[1]
if len(sys.argv) == 2:
    tol = 2
else:
    tol = sys.argv[2]


def graphic(filename):

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    x = [point['x'] for point in data['data']]
    y = [point['y'] for point in data['data']]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, linewidth=int(tol), label='f(x)')
    plt.title('График функции')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()


graphic(str(name))
