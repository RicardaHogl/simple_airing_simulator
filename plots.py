import matplotlib.pyplot as plt


def plot(states):

    minutes = list(range(len(states)))

    dry = [s.dry_bulb for s in states]
    wet = [s.wet_bulb for s in states]
    rh = [s.relative_humidity for s in states]

    fig, ax = plt.subplots(3, 1, figsize=(9, 9))

    ax[0].plot(minutes, dry)
    ax[0].set_ylabel("Dry Bulb (°C)")
    ax[0].grid()

    ax[1].plot(minutes, wet)
    ax[1].set_ylabel("Wet Bulb (°C)")
    ax[1].grid()

    ax[2].plot(minutes, rh)
    ax[2].set_ylabel("RH (%)")
    ax[2].set_xlabel("Minutes")
    ax[2].grid()

    plt.tight_layout()
    plt.show()