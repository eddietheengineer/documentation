import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Arrow
plt.clf()

samplecount = 360
microsteplist = [1, 2, 4, 8, 16]


def definemicrostepamplitude(microstep):
    anglesegment = 90/(microstep)
    center = []
    steps = []
    for i in range(microstep*2):
        if (i % 2 == 0):
            steps.append(anglesegment/2 * i)
        else:
            # center.append(anglesegment/2 * i)
            center.append(np.sin(np.radians(anglesegment/2 * i)))
    return steps, center


def generatecurrenttrace(x_val, microstep):
    steps, center = definemicrostepamplitude(microstep)
    norm_current = []
    for _, index in enumerate(x_val):
        output_index, _ = findFirstInstanceGreaterOrEqualThan(steps, index)
        norm_current.append(round(center[output_index], 3))
    return norm_current


def findFirstInstanceGreaterOrEqualThan(array, value):
    output_index = 0
    output_val = 0
    for x, arrayvalue in reversed(list(enumerate(array))):
        if value >= arrayvalue:
            output_index = x
            output_val = arrayvalue
            break
    return output_index, output_val


def generatefullcycle(samplecount, microstep):
    quartersamplecount = int(samplecount/4)
    quarterdegreeframes = np.linspace(0, 90, quartersamplecount)
    full_x = []
    phase_a = []
    phase_b = []
    reference = generatecurrenttrace(quarterdegreeframes, microstep)
    rev_ref = tuple(reversed(list(reference)))
    for i in range(4):
        for index, value in enumerate(quarterdegreeframes):
            full_x.append(value + i*90)
            if i == 0:
                phase_a.append(reference[index])
                phase_b.append(rev_ref[index])
            elif i == 1:
                phase_a.append(rev_ref[index])
                phase_b.append(reference[index]*-1)
            elif i == 2:
                phase_a.append(reference[index]*-1)
                phase_b.append(rev_ref[index]*-1)
            elif i == 3:
                phase_a.append(rev_ref[index]*-1)
                phase_b.append(reference[index])

    return full_x, phase_a, phase_b


def staticplot():
    plt.xlim(0, 360)
    plt.ylim(bottom=-1)
    for _, ms in enumerate(microsteplist):
        x, y, _ = generatefullcycle(samplecount, ms)
        plt.plot(x, y, label=f'{ms}ms')
    plt.legend()
    plt.show()

################ animated code ################


fig, axs = plt.subplots(2, 2)

time, phase1, phase2, magnitude, vector = [], [], [], [], []
origin = [0, 0]
ln0, = axs[0, 0].plot([], [], color="C2")
ln1, = axs[0, 1].plot([], [], color='C1')
ln2, = axs[1, 1].plot([], [], color='C3')
ln3, = axs[1, 1].plot([], [], color='C0')
ln4, = axs[1, 1].plot([], [], color='C1')
ln5, = axs[1, 1].plot([], [], color='C2')
ln6, = axs[1, 0].plot([], [], color='C0')

def init():
    axs[0, 0].set_title('Phase A Current')
    axs[0, 0].set(xlim=(0, 360), ylim=(-1.1, 1.1))

    axs[0, 1].set_title('Phase B Current')
    axs[0, 1].set(xlim=(0, 360), ylim=(-1.1, 1.1))

    axs[1, 0].set_title('Torque Magnitude')
    axs[1, 0].set(xlim=(0, 360), ylim=(0.9, 1.1))

    axs[1, 1].axis('equal')
    axs[1, 1].set_title('Vector')
    axs[1, 1].set(xlim=(-2, 2), ylim=(-1.1, 1.1))

    fig.tight_layout()

    return ln0, ln1, ln2, ln3, ln4, ln5, ln6

testmicrostep = 128
fig.suptitle(f'Stepper Simulator: {testmicrostep} Microsteps', fontsize=16)

giftime = 5
x, a, b = generatefullcycle(360, testmicrostep)
framecount = range(len(x))
fpsset = int(len(x)/10)

def update(frame):
    time.append(x[frame])
    phase1.append(a[frame])
    phase2.append(b[frame])
    amplitude = np.sqrt(a[frame]**2+b[frame]**2)
    magnitude.append(amplitude)
    ln0.set_data(time, phase1)
    ln1.set_data(time, phase2)
    ln2.set_data(phase1, phase2)
    ln3.set_data([0, a[frame]], [0, b[frame]])
    ln4.set_data([a[frame], a[frame]], [0, b[frame]])
    ln5.set_data([0, a[frame]], [0, 0])
    ln6.set_data(time, magnitude)

    return ln0, ln1, ln2, ln3, ln4, ln5, ln6


#def animate():
ani = FuncAnimation(fig, update, framecount,
                        init_func=init, blit=True, repeat=False)
ani.save(f'Animation_{testmicrostep}ms.gif', fps=fpsset)
#plt.show()
