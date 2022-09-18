from bokeh.plotting import figure, output_file, show
import numpy as np
import random
from scipy import signal


# The point of this is to try wavelet
# analysis on something that looks like the real data


class signal:
    def __init__(self):
        self.time_series = np.arange(start=0, stop=1, step=0.001)

    def spike_signal(self):
        # spikes soar to 40v within a few ms
        # they rarely last longer than 10ms
        # assumes half wave rectification
        # value range depends on the time step

        # floor is sinusoidal with time, going to high with the max
        # max is sinusoidal with time, going to high with the max

        total_range = np.arange(0, 40, 0.1)
        sinusoid = np.sin(np.arange(0, np.pi, np.pi / len(self.time_series)))
        sinc = np.sinc(np.arange(0, np.pi, np.pi / len(self.time_series)))
        floor = sinc * 20
        ciel = sinusoid * 40
        output = np.zeros(shape=len(self.time_series))

        for n, t in enumerate(self.time_series):
            point_voltage_range = np.linspace(start=floor[n], stop=ciel[n], num=100)
            output[n] = random.choice(list(point_voltage_range))

        return [self.time_series, output]

    def cwt_spike(self):
        # Apply continous wavelet transform to the spike signal
        pass

    def plot_cwt_histogram(self):
        # show data from contionus wavelet transform on waterfall diagram
        pass

    def plot_spike(self):
        p = figure(title="tribo-electric voltage", x_axis_label='x', y_axis_label='y')
        x, y = self.spike_signal()
        # add a line renderer with legend and line thickness
        p.line(x, y, legend="voltage.", line_width=2)

        # show the results
        show(p)
