#!/usr/bin/env python

import sys
import os
import lcm
import numpy as np
import matplotlib.pyplot as plt

from exlcm import flowdrone_t

if len(sys.argv) < 2:
    sys.stderr.write("usage: read-log <logfile>\n")
    sys.exit(1)

log = lcm.EventLog("../../" + sys.argv[1], "r")

timestamp_list = []

x_list = []
y_list = []

z_list = []

roll_list = []
yaw_list = []

pitch_list = []

rollrate_list = []
yawrate_list = []

pitchrate_list = []

rollrate_residual_list = []
yawrate_residual_list = []

pitchrate_residual_list = []

thrust_sp_list = []
thrust_residual_list = []

wind_magnitude_estimate_list = []
wind_angle_estimate_list = []

start_time = -1.0

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, "plots/" + sys.argv[1])
print("final_directory: ",final_directory)
if not os.path.exists(final_directory):
   os.makedirs(final_directory)

writeCSV = True # flag TRUE if you want to write to csv
csv_filename = final_directory + "/" + sys.argv[1] + ".csv" # filename for csv

if writeCSV:
    with open(csv_filename, "a") as f:   # use 'a' instead of 'ab'
        f.write("timestamp,x,y,z,roll,pitch,yaw,vx,vy,vz,p,q,r,psp,qsp,rsp,pres,qres,rres,thrust_sp, thrust_res")
        f.write("\n")

for event in log:
    if event.channel == "FLOWDRONE":
        if start_time == -1:
            start_time = event.timestamp
        msg = flowdrone_t.decode(event.data)
        print("Message:")
        print("   timestamp   = %s" % str(event.timestamp))
        timestamp_list.append((event.timestamp-start_time)/1E6)
        print("   drone_state    = %s" % str(msg.drone_state))
        x_list.append(msg.drone_state[0])
        y_list.append(msg.drone_state[1])
        z_list.append(msg.drone_state[2])
        roll_list.append(msg.drone_state[7])
        yaw_list.append(msg.drone_state[9])
        pitch_list.append(msg.drone_state[8])
        print("   thrust_sp = %s" % str(msg.thrust_sp))
        thrust_sp_list.append(msg.thrust_sp)
        print("   thrust_residual = %s" % str(msg.thrust_residual))
        thrust_residual_list.append(msg.thrust_residual)
        print("   body_rate_sp =%s" % str(msg.body_rate_sp))
        rollrate_list.append(msg.body_rate_sp[0])
        yawrate_list.append(msg.body_rate_sp[2])
        pitchrate_list.append(msg.body_rate_sp[1])
        print("   body_rate_residual =%s" % str(msg.body_rate_residual))
        rollrate_residual_list.append(msg.body_rate_residual[0])
        yawrate_residual_list.append(msg.body_rate_residual[2])
        pitchrate_residual_list.append(msg.body_rate_residual[1])
        print("   wind_magnitude_estimate        = %s" % str(msg.wind_magnitude_estimate))
        wind_magnitude_estimate_list.append(msg.wind_magnitude_estimate)
        print("   wind_angle_estimate     = %s" % str(msg.wind_angle_estimate))
        wind_angle_estimate_list.append(msg.wind_angle_estimate)
        print("")

        if writeCSV:
            with open(csv_filename, "a") as f:   # use 'a' instead of 'ab'
                np.savetxt(f, np.array([(event.timestamp-start_time)/1E6,msg.drone_state[0],msg.drone_state[1],msg.drone_state[2], # time s, x,y,z position
                                        msg.drone_state[7], msg.drone_state[8], msg.drone_state[9], # roll pitch yaw
                                        msg.drone_state[10], msg.drone_state[11], msg.drone_state[12], # vx, vy, vz
                                        msg.drone_state[13], msg.drone_state[14], msg.drone_state[15], # p, q, r (body rates)
                                        msg.body_rate_sp[0], msg.body_rate_sp[1], msg.body_rate_sp[2], # body rate setpoints
                                        msg.body_rate_residual[0], msg.body_rate_residual[1], msg.body_rate_residual[2], # body rate residual
                                        msg.thrust_sp, msg.thrust_residual]).reshape(1,21),delimiter=",") # thrust setpoint, thrust residual

print("final_directory: ",final_directory)

buffer = 5 

fig = plt.figure()
#plt.axis([min(timestamp_list) - buffer, max(timestamp_list) + buffer, min(min(x_list), min(y_list)) - buffer, max(max(x_list), max(y_list)) + buffer])
plt.scatter(timestamp_list, x_list, s=2, c='b', marker="s", label='x')
plt.scatter(timestamp_list, y_list, s=2, c='r', marker="o", label='y')
plt.legend(loc='upper left')
plt.title("XY v Time")
plt.xlabel("Time (s)")
plt.ylabel("Position (UNITS)")
plt.savefig(final_directory + "/xy_plot.png")

fig = plt.figure()
#plt.axis([min(timestamp_list) - buffer, max(timestamp_list) + buffer, min(z_list) - buffer, max(z_list) + buffer])
plt.scatter(timestamp_list, z_list, s=2, c='b', marker="s", label='z')
plt.legend(loc='upper left')
plt.title("Z v Time")
plt.xlabel("Time (s)")
plt.ylabel("Position (UNITS)")
plt.savefig(final_directory + "/z_plot.png")

fig = plt.figure()
#plt.axis([min(timestamp_list) - buffer, max(timestamp_list) + buffer, min(min(roll_list), min(yaw_list)) - buffer, max(max(roll_list), max(yaw_list)) + buffer])
plt.scatter(timestamp_list, roll_list, s=2, c='b', marker="s", label='roll')
plt.scatter(timestamp_list, yaw_list, s=2, c='r', marker="o", label='yaw')
plt.legend(loc='upper left')
plt.title("Roll, Yaw v Time")
plt.xlabel("Time (s)")
plt.ylabel("Angle (UNITS)")
plt.savefig(final_directory + "/roll_yaw_plot.png")

fig = plt.figure()
#plt.axis([min(timestamp_list) - buffer, max(timestamp_list) + buffer, min(pitch_list) - buffer, max(pitch_list) + buffer])
plt.scatter(timestamp_list, pitch_list, s=2, c='b', marker="s", label='pitch')
plt.legend(loc='upper left')
plt.title("Pitch v Time")
plt.xlabel("Time (s)")
plt.ylabel("Angle (UNITS)")
plt.savefig(final_directory + "/pitch_plot.png")

fig = plt.figure()
#plt.axis([min(timestamp_list) - buffer, max(timestamp_list) + buffer, min(min(rollrate_list), min(yawrate_list)) - buffer, max(max(rollrate_list), max(yawrate_list)) + buffer])
plt.scatter(timestamp_list, rollrate_list, s=2, c='b', marker="s", label='rollrate')
plt.scatter(timestamp_list, yawrate_list, s=2, c='r', marker="o", label='yawrate')
plt.legend(loc='upper left')
plt.title("Net Rollrate, Yawrate setpoint v Time")
plt.xlabel("Time (s)")
plt.ylabel("Angle Rate (UNITS)")
plt.savefig(final_directory + "/rollrate_yawrate_plot.png")

fig = plt.figure()
#plt.axis([min(timestamp_list) - buffer, max(timestamp_list) + buffer, min(pitchrate_list) - buffer, max(pitchrate_list) + buffer])
plt.scatter(timestamp_list, pitchrate_list, s=2, c='b', marker="s", label='pitchrate')
plt.legend(loc='upper left')
plt.title("Net Pitch setpoint v Time")
plt.xlabel("Time (s)")
plt.ylabel("Angle Rate (UNITS)")
plt.savefig(final_directory + "/pitchrate_plot.png")

fig = plt.figure()
#plt.axis([min(timestamp_list) - buffer, max(timestamp_list) + buffer, min(min(rollrate_residual_list), min(yawrate_residual_list)) - buffer, max(max(rollrate_residual_list), max(yawrate_residual_list)) + buffer])
plt.scatter(timestamp_list, rollrate_residual_list, s=2, c='b', marker="s", label='rollrate_residual')
plt.scatter(timestamp_list, yawrate_residual_list, s=2, c='r', marker="o", label='yawrate_residual')
plt.legend(loc='upper left')
plt.title("Rollrate_residual, Yawrate_residual v Time")
plt.xlabel("Time (s)")
plt.ylabel("Angle Rate Residual (UNITS)")
plt.savefig(final_directory + "/rollrate_residual_yawrate_residual_plot.png")

fig = plt.figure()
#plt.axis([min(timestamp_list) - buffer, max(timestamp_list) + buffer, min(pitchrate_residual_list) - buffer, max(pitchrate_residual_list) + buffer])
plt.scatter(timestamp_list, pitchrate_residual_list, s=2, c='b', marker="s", label='pitchrate_residual')
plt.legend(loc='upper left')
plt.title("Pitch_residual v Time")
plt.xlabel("Time (s)")
plt.ylabel("Angle Rate Residual (UNITS)")
plt.savefig(final_directory + "/pitchrate_residual_plot.png")

fig = plt.figure()
#plt.axis([min(timestamp_list) - buffer, max(timestamp_list) + buffer, min(min(thrust_sp_list), min(thrust_residual_list)) - buffer, max(max(thrust_sp_list), max(thrust_residual_list)) + buffer])
plt.scatter(timestamp_list, thrust_sp_list, s=2, c='b', marker="s", label='thrust_sp')
plt.scatter(timestamp_list, thrust_residual_list, s=2, c='r', marker="o", label='thrust_residual_list')
plt.legend(loc='upper left')
plt.title("Thrust Set Point, Thrust Residual v Time")
plt.xlabel("Time (s)")
plt.ylabel("Thrust Set Point (UNITS), Thrust Residual (UNITS)")
plt.savefig(final_directory + "/thurst_sp_thrust_residual_plot.png")

fig = plt.figure()
#plt.axis([min(timestamp_list) - buffer, max(timestamp_list) + buffer, min(wind_magnitude_estimate_list) - buffer, max(wind_magnitude_estimate_list), max(wind_angle_estimate_list) + buffer])
plt.scatter(timestamp_list, wind_magnitude_estimate_list, s=2, c='b', marker="s", label='wind_magnitude_estimate_list')
plt.legend(loc='upper left')
plt.title("Wind Magnitude Estimate")
plt.xlabel("Time (s)")
plt.ylabel("Wind Magnitude Estimate (UNITS)")
plt.savefig(final_directory + "/wind_magnitude_estimate_plot.png")

fig = plt.figure()
#plt.axis([min(timestamp_list) - buffer, max(timestamp_list) + buffer, min(wind_angle_estimate_list) - buffer, max(wind_angle_estimate_list), max(wind_angle_estimate_list) + buffer])
plt.scatter(timestamp_list, wind_angle_estimate_list, s=2, c='b', marker="s", label='wind_angle_estimate_list')
plt.legend(loc='upper left')
plt.title("Wind Angle Estimate")
plt.xlabel("Time (s)")
plt.ylabel("Wind Angle Estimate (UNITS)")
plt.savefig(final_directory + "/wind_angle_estimate_plot.png")
