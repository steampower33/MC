import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

with open("sixth.cwnd", "rt") as f:
    data = f.read()

cwnd = []
time = []

for line in data.split("\n"):
    t, s, _ = map(float, line.split("\t"))
    time.append(t)
    cwnd.append(s)

plt.title("sixth.cc Tracing Result")
plt.xlabel("Time(s)")
plt.ylabel("CWND size(Byte)")
plt.grid(True)

plt.plot(time, cwnd, label="CWND size")
plt.legend(loc="upper right", frameon=True)
plt.savefig("sixth-cc-result")
plt.close()