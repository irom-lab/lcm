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
final_directory = os.path.join(current_directory, "velocity_plots/" + sys.argv[1])
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

fig = plt.figure()
plt.plot(timestamp_list, x_list, c='b', label='position in the x-axis')
plt.plot(timestamp_list, y_list, c='r', label='position in the y-axis')
plt.legend(loc='upper left')
plt.title("X and Y Position in the Forrestal ENU Frame (Gym) [m] over Time")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.savefig(final_directory + "/xy_plot.png")

fig = plt.figure()
plt.plot(timestamp_list, z_list, c='b', label='position in the z-axis')
plt.legend(loc='upper left')
plt.title("Z Position in the Forrestal ENU Frame (Gym) [m] over Time")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.savefig(final_directory + "/z_plot.png")

fig = plt.figure()
plt.plot(timestamp_list, roll_list, c='b', label='roll')
plt.plot(timestamp_list, yaw_list, c='r', label='yaw')
plt.legend(loc='upper left')
plt.title("Roll and Yaw in the Forrestal ENU Frame (Gym) [rad] over Time")
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.savefig(final_directory + "/roll_yaw_plot.png")

fig = plt.figure()
plt.plot(timestamp_list, pitch_list, c='b', label='pitch')
plt.legend(loc='upper left')
plt.title("Pitch in the Forrestal ENU Frame (Gym) [rad] over Time")
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.savefig(final_directory + "/pitch_plot.png")

fig = plt.figure()
plt.plot(timestamp_list, vy_list, c='b', label='velocity in the y-axis')
plt.plot(timestamp_list, vz_list, c='r', label='velocity in the z-axis')
plt.legend(loc='upper left')
plt.title("Y and Z Velocity in the Forrestal ENU Frame (Gym) [m/s] over Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.savefig(final_directory + "/vy_vz_plot.png")

fig = plt.figure()
plt.plot(timestamp_list, vx_list, c='b', label='velocity in the x-axis')
plt.legend(loc='upper left')
plt.title("X Velocity in the Forrestal ENU Frame (Gym) [m/s] over Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.savefig(final_directory + "/vx_plot.png")

fig = plt.figure()
plt.plot(timestamp_list, rollrate_actual_list, c='b', label='roll angular velocity')
plt.plot(timestamp_list, yawrate_actual_list, c='r', label='yaw angular velocity')
plt.legend(loc='upper left')
plt.title("Roll and Yaw Angular Velocity in the Forrestal ENU Frame (Gym) [m/s] over Time")
plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (rad/s)")
plt.savefig(final_directory + "/rollrate_actual_yawrate_actual_plot.png")

fig = plt.figure()
plt.plot(timestamp_list, pitchrate_actual_list, c='b', label='pitch angular velocity')
plt.legend(loc='upper left')
plt.title("Pitch Angular Velocity in the Forrestal ENU Frame (Gym) [m/s] over Time")
plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (rad/s)")
plt.savefig(final_directory + "/pitchrate_actual_plot.png")

fig = plt.figure()
plt.plot(timestamp_list, rollrate_list, c='b', label='roll body rate setpoint')
plt.plot(timestamp_list, yawrate_list, c='r', label='yaw body rate setpoint')
plt.legend(loc='upper left')
plt.title("Net Roll and Yaw Body Rate Setpoint in FRD (PX4) [rad/s] over Time")
plt.xlabel("Time (s)")
plt.ylabel("Body Rate Setpoint (rad/s)")
plt.savefig(final_directory + "/rollrate_yawrate_plot.png")

fig = plt.figure()
plt.plot(timestamp_list, pitchrate_list, c='b', label='pitch body rate setpoint')
plt.legend(loc='upper left')
plt.title("Net Pitch Body Rate Setpoint in FRD (PX4) [rad/s] over Time")
plt.xlabel("Time (s)")
plt.ylabel("Body Rate Setpoint (rad/s)")
plt.savefig(final_directory + "/pitchrate_plot.png")

fig = plt.figure()
plt.plot(timestamp_list, rollrate_residual_list, c='b', label='roll body rate residual')
plt.plot(timestamp_list, yawrate_residual_list, c='r', label='yaw body rate residual')
plt.legend(loc='upper left')
plt.title("Roll and Yaw Body Rate Residual in FRD (PX4) [rad/s] over Time")
plt.xlabel("Time (s)")
plt.ylabel("Body Rate Residual (rad/s)")
plt.savefig(final_directory + "/rollrate_residual_yawrate_residual_plot.png")

fig = plt.figure()
plt.plot(timestamp_list, pitchrate_residual_list, c='b', label='pitch body rate residual')
plt.legend(loc='upper left')
plt.title("Pitch Body Rate Residual in FRD (PX4) [rad/s] over Time")
plt.xlabel("Time (s)")
plt.ylabel("Body Rate Residual (rad/s)")
plt.savefig(final_directory + "/pitchrate_residual_plot.png")

fig = plt.figure()
plt.plot(timestamp_list, thrust_sp_list, c='b', label='thrust setpoint')
plt.plot(timestamp_list, thrust_residual_list, c='r', label='thrust residual')
plt.legend(loc='upper left')
plt.title("Thrust Setpoint and Thrust Residual in FRD (PX4) [normalized] over Time")
plt.xlabel("Time (s)")
plt.ylabel("Thrust Setpoint (normalized) and Thrust Residual (normalized)")
plt.savefig(final_directory + "/thurst_sp_thrust_residual_plot.png")

fig = plt.figure()
plt.plot(timestamp_list, wind_magnitude_estimate_list, c='b', label='wind magnitidue estimate')
plt.legend(loc='upper left')
plt.title("Wind Magnitude Estimate [m/s] over Time")
plt.xlabel("Time (s)")
plt.ylabel("Wind Magnitude Estimate (m/s)")
plt.savefig(final_directory + "/wind_magnitude_estimate_plot.png")

fig = plt.figure()
plt.plot(timestamp_list, wind_angle_estimate_list, c='b', label='wind angle estimate')
plt.legend(loc='upper left')
plt.title("Wind Angle Estimate [deg] over Time")
plt.xlabel("Time (s)")
plt.ylabel("Wind Angle Estimate (deg)")
plt.savefig(final_directory + "/wind_angle_estimate_plot.png")
