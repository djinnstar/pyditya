import matplotlib.pyplot as plt
x = []
y = []
samples = 1000


def rect(h):
    if abs(h) < 1:
        return 1
    return 0


def add_hills(x, shifts):
    list_of_ys = []

    for shift in shifts:
        list_of_ys.append(0.234 * hill(x, shift))

    return sum(list_of_ys)


def hill(x, s):
    if -1000 * (x - s)**2 + 1 > 0:
        return -1000 * (x - s)**2 + 1

    else:
        return 0


shifts = []

for shift in range(-100, 100):
    shifts.append(shift/100)


for item in range(-3 * samples, 3 * samples):
    x.append(item/samples)
    y.append(add_hills(item/samples, shifts))

plt.plot(x, y)


for num in range(-3 * samples, 3 * samples):
    x.append(num/samples)
    y.append(rect(x[-1]))

plt.plot(x, y)
plt.show()
