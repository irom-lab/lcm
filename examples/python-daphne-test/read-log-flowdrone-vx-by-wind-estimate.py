#!/usr/bin/env python

import sys
import os
import lcm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from exlcm import flowdrone_daphne_t

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

vy_list = []
vz_list = []

vx_list = []

rollrate_actual_list = []
yawrate_actual_list = []

pitchrate_actual_list = []

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

wind_obs_latest_list = []

start_time = -1.0

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, "velocity_by_wind_estimate_plots/" + sys.argv[1])
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
        msg = flowdrone_daphne_t.decode(event.data)
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
        vx_list.append(msg.drone_state[10])
        vy_list.append(msg.drone_state[11])
        vz_list.append(msg.drone_state[12])
        rollrate_actual_list.append(msg.drone_state[13])
        pitchrate_actual_list.append(msg.drone_state[14])
        yawrate_actual_list.append(msg.drone_state[15])
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
        print("   wind_obs_latest        = %s" % str(msg.wind_obs_current[4])) #TODO: update to latest wind obs index
        wind_obs_latest_list.append(msg.wind_obs_current)
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
                                        msg.thrust_sp, msg.thrust_residual,
                                        msg.wind_magnitude_estimate, msg.wind_angle_estimate, msg.wind_obs_current[4]]).reshape(1,24),delimiter=",") # thrust setpoint, thrust residual

print("final_directory: ",final_directory)

buffer = 5 

# fig = plt.figure()
# plt.scatter(wind_magnitude_estimate_list, vx_list, c='b', label='velocity in the x-axis over wind magnitude estimate')
# plt.legend(loc='upper left')
# plt.title("X Velocity in the Forrestal ENU Frame (Gym) [m/s] over Wind Magnitude Estimate")
# plt.xlabel("Wind Magnitude Estimate (m/s)")
# plt.ylabel("Velocity (m/s)")
# plt.savefig(final_directory + "/vx_by_wind_estimate_plot.png")

# fig = plt.figure()
# plt.scatter(wind_magnitude_estimate_list, vy_list, c='b', label='velocity in the y-axis over wind magnitude estimate')
# plt.legend(loc='upper left')
# plt.title("Y Velocity in the Forrestal ENU Frame (Gym) [m/s] over Wind Magnitude Estimate")
# plt.xlabel("Wind Magnitude Estimate (m/s)")
# plt.ylabel("Velocity (m/s)")
# plt.savefig(final_directory + "/vy_by_wind_estimate_plot.png")

# fig = plt.figure()
# plt.scatter(wind_magnitude_estimate_list, vz_list, c='b', label='velocity in the z-axis over wind magnitude estimate')
# plt.legend(loc='upper left')
# plt.title("Z Velocity in the Forrestal ENU Frame (Gym) [m/s] over Wind Magnitude Estimate")
# plt.xlabel("Wind Magnitude Estimate (m/s)")
# plt.ylabel("Velocity (m/s)")
# plt.savefig(final_directory + "/vz_by_wind_estimate_plot.png")

# fig = plt.figure()
# plt.scatter(wind_angle_estimate_list, vx_list, c='b', label='velocity in the x-axis over wind angle estimate')
# plt.legend(loc='upper left')
# plt.title("X Velocity in the Forrestal ENU Frame (Gym) [m/s] over Wind Angle Estimate")
# plt.xlabel("Wind Angle Estimate (m/s)")
# plt.ylabel("Velocity (m/s)")
# plt.savefig(final_directory + "/vx_by_wind_angle_estimate_plot.png")

# fig = plt.figure()
# plt.scatter(wind_angle_estimate_list, vy_list, c='b', label='velocity in the y-axis over wind angle estimate')
# plt.legend(loc='upper left')
# plt.title("Y Velocity in the Forrestal ENU Frame (Gym) [m/s] over Wind Angle Estimate")
# plt.xlabel("Wind Angle Estimate (m/s)")
# plt.ylabel("Velocity (m/s)")
# plt.savefig(final_directory + "/vy_by_wind_angle_estimate_plot.png")

# fig = plt.figure()
# plt.scatter(wind_angle_estimate_list, vz_list, c='b', label='velocity in the z-axis over wind angle estimate')
# plt.legend(loc='upper left')
# plt.title("Z Velocity in the Forrestal ENU Frame (Gym) [m/s] over Wind Angle Estimate")
# plt.xlabel("Wind Angle Estimate (m/s)")
# plt.ylabel("Velocity (m/s)")
# plt.savefig(final_directory + "/vz_by_wind_angle_estimate_plot.png")

# fig = plt.figure()
# plt.plot(timestamp_list, vx_list, c='b', label='velocity in the x-axis')
# plt.scatter(timestamp_list, [item - 1 for item in wind_magnitude_estimate_list], c='r', s=2, label='wind magnitude estimate')
# plt.legend(loc='upper left')
# plt.title("X Velocity in the Forrestal ENU Frame (Gym) [m/s] and Wind Magnitude Estimate with Offset [m/s] over Time")
# plt.xlabel("Time (s)")
# plt.ylabel("Velocity (m/s)")
# plt.savefig(final_directory + "/TODO.png")

offset = 0
offset_wind = 1

# fig = plt.figure()
# plt.plot(timestamp_list, [abs(item) + offset for item in vx_list], c='b', label='velocity in the x-axis')
# plt.scatter(timestamp_list, wind_angle_estimate_list, c='r', s=2, label='wind angle estimate')
# plt.legend(loc='upper left')
# plt.title("TODO")
# plt.xlabel("Time (s)")
# plt.ylabel("Angle (deg)")
# plt.savefig(final_directory + "/TODO2.png")

# df = pd.DataFrame({'B': wind_magnitude_estimate_list})
# roll_2 = df.rolling(2).mean()
# fig = plt.figure()
# plt.plot(timestamp_list, [abs(item) + offset for item in vx_list], c='b', label='velocity in the x-axis')
# plt.scatter(timestamp_list, roll_2, c='r', s=2, label='wind angle estimate')
# plt.legend(loc='upper left')
# plt.title("TODO")
# plt.xlabel("Time (s)")
# plt.ylabel("Angle (deg)")
# plt.savefig(final_directory + "/roll2.png")

# df = pd.DataFrame({'B': wind_magnitude_estimate_list})
# roll_3 = df.rolling(3).mean()
# fig = plt.figure()
# plt.plot(timestamp_list, [abs(item) + offset for item in vx_list], c='b', label='velocity in the x-axis')
# plt.scatter(timestamp_list, roll_3, c='r', s=2, label='wind angle estimate')
# plt.legend(loc='upper left')
# plt.title("TODO")
# plt.xlabel("Time (s)")
# plt.ylabel("Angle (deg)")
# plt.savefig(final_directory + "/roll3.png")

# df = pd.DataFrame({'B': wind_magnitude_estimate_list})
# roll_4 = df.rolling(4).mean()
# fig = plt.figure()
# plt.plot(timestamp_list, [abs(item) + offset for item in vx_list], c='b', label='velocity in the x-axis')
# plt.scatter(timestamp_list, roll_4, c='r', s=2, label='wind angle estimate')
# plt.legend(loc='upper left')
# plt.title("TODO")
# plt.xlabel("Time (s)")
# plt.ylabel("Angle (deg)")
# plt.savefig(final_directory + "/roll4.png")

# df = pd.DataFrame({'B': wind_magnitude_estimate_list})
# roll_5 = df.rolling(5).mean()
# fig = plt.figure()
# plt.plot(timestamp_list, [abs(item) + offset for item in vx_list], c='b', label='velocity in the x-axis')
# plt.scatter(timestamp_list, roll_5, c='r', s=2, label='wind angle estimate')
# plt.legend(loc='upper left')
# plt.title("TODO")
# plt.xlabel("Time (s)")
# plt.ylabel("Angle (deg)")
# plt.savefig(final_directory + "/roll5.png")

# df = pd.DataFrame({'B': wind_magnitude_estimate_list})
# roll_10 = df.rolling(10).mean()
# fig = plt.figure()
# plt.plot(timestamp_list, [abs(item) + offset for item in vx_list], c='b', label='velocity in the x-axis')
# plt.scatter(timestamp_list, roll_10, c='r', s=2, label='wind angle estimate')
# plt.legend(loc='upper left')
# plt.title("TODO")
# plt.xlabel("Time (s)")
# plt.ylabel("Angle (deg)")
# plt.savefig(final_directory + "/roll10.png")

# for i in range(50):
#     j = i + 1
#     df = pd.DataFrame({'B': [item - offset_wind for item in wind_magnitude_estimate_list]})
#     roll = df.rolling(j).mean()
#     fig = plt.figure()
#     plt.plot(timestamp_list, [abs(item) + offset for item in vx_list], c='b', label='velocity in the x-axis')
#     plt.scatter(timestamp_list, roll, c='r', s=2, label='wind magnitude estimate')
#     plt.legend(loc='upper left')
#     plt.title("X Velocity Magnitude in the Forrestal ENU Frame (Gym) [m/s] and Rolling Average Wind Magnitude Estimate with Offset [m/s] over Time")
#     plt.xlabel("Time (s)")
#     plt.ylabel("Velocity (m/s)")
#     plt.savefig(final_directory + "/roll" + str(j) + "_offset" + str(offset_wind) + ".png")

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

plt.rcParams['font.family'] = 'serif'

fig = plt.figure()
plt.plot(timestamp_list, z_list, c='b', label='position in the z-axis')
plt.legend(loc='upper left')
plt.title("Z Position in the Forrestal ENU Frame (Gym) [m] over Time")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.savefig(final_directory + "/z_plot.png")