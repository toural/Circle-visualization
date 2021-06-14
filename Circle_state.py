from qiskit import *
from qiskit_textbook.tools import array_to_latex
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cmath 
import colorsys

def print_circles(state):
    sfigure, axes = plt.subplots(figsize=(60, 60))
    x_pos = 0.1
    y_pos = 0.9
    x_next = 0.1
    y_next = 0.1
    r = 0.03
    arrow_size = 0.007
    i=0
    for j in range(len(state)):
        axes.add_artist( plt.Circle( (x_pos+x_next*i, y_pos),r ,fill = False ) )
        axes.text(x_pos+x_next*i-0.004,y_pos-r-0.02,str(j),fontsize=40)
        magnitude = abs(state[j])
        angles = (np.angle(state[j]) + (np.pi * 4)) % (np.pi * 2)
        phase_color = colorsys.hls_to_rgb(angles / (np.pi * 2), 0.5, 0.5)
        axes.add_artist( plt.Circle( (x_pos+x_next*i, y_pos),r*magnitude,fill = True, color= phase_color,alpha = 0.9 ))
        if magnitude > 0.0001:
            axes.add_patch(patches.Arrow(x_pos+x_next*i, y_pos, np.cos(cmath.phase(state[j]))*r, np.sin(cmath.phase(state[j]))*r, arrow_size))
        i = i+1
        if i == 8:
            i = 0
            y_pos = y_pos - y_next
    plt.show()

q = QuantumRegister(4)
circ = QuantumCircuit(q)

circ.h(q)
circ.t(q[0])
circ.s(q[1])
circ.z(q[2])

circ.draw()

stvBackend = Aer.get_backend('statevector_simulator')

job = execute (circ, stvBackend)
state = job.result().get_statevector()
array_to_latex(state, pretext = "\\text{Statevector} = ", precision=1)

print_circles(state)
