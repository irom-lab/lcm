import lcm
import time
import numpy as np

from exlcm import voltages_t

lc = lcm.LCM()

msg = voltages_t()
msg.timestamp = int(time.time() * 1000000)
msg.voltages = (0, 0, 0, 0, 0, 0)

lc.publish("VOLTAGES", msg.encode())
