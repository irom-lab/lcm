from pandas import *
import matplotlib.pyplot as plt
 
# ----------------------------------------------------------------------------------------------------------------

def plot_individual_pics():

    # Plot wind-aware tests

    wind_aware_files = ["./lcmlog-2022-09-14.65.csv", "./lcmlog-2022-09-14.66.csv", 
                        "./lcmlog-2022-09-14.67.csv", "./lcmlog-2022-09-14.68.csv",
                        "./lcmlog-2022-09-14.69.csv", "./lcmlog-2022-09-15.21.csv",
                        "./lcmlog-2022-09-15.22.csv", "./lcmlog-2022-09-15.23.csv",
                        "./lcmlog-2022-09-15.24.csv", "./lcmlog-2022-09-15.25.csv"]

    fig = plt.figure()
    for index, wind_aware_file in enumerate(wind_aware_files):
        data = read_csv(wind_aware_file)
        x_list = data['x'].tolist()
        y_list = data['y'].tolist()
        # plt.plot(x_list, y_list, c='C'+str(index))
        plt.plot(x_list, y_list, c=(1,0,0))
    plt.xlabel("X Position (m)")
    plt.ylabel("Y Position (m)")
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig("." + "/wind-aware.png", dpi=300, bbox_inches='tight')

    # Plot wind-unaware tests

    wind_unaware_files =   ["./lcmlog-2022-09-15.00.csv", "./lcmlog-2022-09-15.01.csv", 
                            "./lcmlog-2022-09-15.02.csv", "./lcmlog-2022-09-15.03.csv",
                            "./lcmlog-2022-09-15.04.csv", "./lcmlog-2022-09-15.16.csv",
                            "./lcmlog-2022-09-15.17.csv", "./lcmlog-2022-09-15.18.csv",
                            "./lcmlog-2022-09-15.19.csv", "./lcmlog-2022-09-15.20.csv"]

    fig = plt.figure()
    for index, wind_unaware_file in enumerate(wind_unaware_files):
        data = read_csv(wind_unaware_file)
        x_list = data['x'].tolist()
        y_list = data['y'].tolist()
        plt.plot(x_list, y_list, c='C'+str(index))
    plt.xlabel("X Position (m)")
    plt.ylabel("Y Position (m)")
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig("." + "/wind-unaware.png", dpi=300, bbox_inches='tight')

    # Plot baseline tests

    baseline_files =   ["./lcmlog-2022-09-15.05.csv", "./lcmlog-2022-09-15.06.csv", 
                        "./lcmlog-2022-09-15.07.csv", "./lcmlog-2022-09-15.08.csv",
                        "./lcmlog-2022-09-15.09.csv", "./lcmlog-2022-09-15.11.csv",
                        "./lcmlog-2022-09-15.12.csv", "./lcmlog-2022-09-15.13.csv",
                        "./lcmlog-2022-09-15.14.csv", "./lcmlog-2022-09-15.15.csv"]

    fig = plt.figure()
    for index, baseline_file in enumerate(baseline_files):
        data = read_csv(baseline_file)
        x_list = data['x'].tolist()
        y_list = data['y'].tolist()
        plt.plot(x_list, y_list, c='C'+str(index))
    plt.xlabel("X Position (m)")
    plt.ylabel("Y Position (m)")
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig("." + "/baseline.png", dpi=300, bbox_inches='tight')

# ----------------------------------------------------------------------------------------------------------------

def plot_subplots():

    # fig, axs = plt.subplots(1, 3, figsize=(18,3))
    #fig, axs = plt.subplots(1, 3, figsize=(18,5), sharey=True)
    fig, axs = plt.subplots(3, 1, figsize=(5,18), sharex=True)

    wind_aware_files = ["./lcmlog-2022-09-14.65.csv", "./lcmlog-2022-09-14.66.csv", 
                        "./lcmlog-2022-09-14.67.csv", "./lcmlog-2022-09-14.68.csv",
                        "./lcmlog-2022-09-14.69.csv", "./lcmlog-2022-09-15.21.csv",
                        "./lcmlog-2022-09-15.22.csv", "./lcmlog-2022-09-15.23.csv",
                        "./lcmlog-2022-09-15.24.csv", "./lcmlog-2022-09-15.25.csv"]

    wind_unaware_files =   ["./lcmlog-2022-09-15.00.csv", "./lcmlog-2022-09-15.01.csv", 
                            "./lcmlog-2022-09-15.02.csv", "./lcmlog-2022-09-15.03.csv",
                            "./lcmlog-2022-09-15.04.csv", "./lcmlog-2022-09-15.16.csv",
                            "./lcmlog-2022-09-15.17.csv", "./lcmlog-2022-09-15.18.csv",
                            "./lcmlog-2022-09-15.19.csv", "./lcmlog-2022-09-15.20.csv"]

    baseline_files =   ["./lcmlog-2022-09-15.05.csv", "./lcmlog-2022-09-15.06.csv", 
                        "./lcmlog-2022-09-15.07.csv", "./lcmlog-2022-09-15.08.csv",
                        "./lcmlog-2022-09-15.09.csv", "./lcmlog-2022-09-15.11.csv",
                        "./lcmlog-2022-09-15.12.csv", "./lcmlog-2022-09-15.13.csv",
                        "./lcmlog-2022-09-15.14.csv", "./lcmlog-2022-09-15.15.csv"]

    all_files = [wind_aware_files,
                 wind_unaware_files,
                 baseline_files]

    # TODO: Remove
    # wind_aware_files = ["./lcmlog-2022-09-14.65.csv", "./lcmlog-2022-09-14.66.csv",
    #                     "./lcmlog-2022-09-14.67.csv", "./lcmlog-2022-09-14.68.csv",]
    # wind_aware_files = ["./lcmlog-2022-09-14.65.csv", "./lcmlog-2022-09-14.66.csv"]
    # all_files = [wind_aware_files]

    all_test_types = ["Wind-aware", "Wind-unaware", "Baseline"]

    for test_type_index in range(len(all_files)):
        for file in all_files[test_type_index]:
            data = read_csv(file)
            x_list = data['x'].tolist()
            y_list = data['y'].tolist()
            # point_index = 1
            # print(file)
            # for x, y in zip(x_list, y_list):
            #     axs[test_type_index].scatter(x, y, color=(point_index/(1.0*len(x_list)), 0, 0, 0.5), s=5)
            #     point_index += 1
            axs[test_type_index].plot(x_list, y_list, c='C'+str(test_type_index))
        axs[test_type_index].set_title(all_test_types[test_type_index])
        #axs[test_type_index].set_xlabel("X Position (m)")
        axs[test_type_index].set_ylabel("Y Position (m)")
        axs[test_type_index].spines['top'].set_visible(False)
        axs[test_type_index].spines['right'].set_visible(False)

        # axs[test_type_index].spines['bottom'].set_bounds(-0.5, 1.2)
        # axs[test_type_index].spines['left'].set_bounds(-0.5, 0.5)
        axs[test_type_index].set_xlim([-0.5, 1.2])
        axs[test_type_index].set_ylim([-0.5, 0.4])

        # axs[test_type_index].axis('equal')
        axs[test_type_index].set_aspect('equal')

    # axs[0].set_ylabel("Y Position (m)")
    axs[2].set_xlabel("X Position (m)")

    # axs[0].set_xlim([-0.2, 0.6])
    # axs[0].set_ylim([-0.2, 0.6])
    # axs[1].set_xlim([-0.3, 0.9])
    # axs[1].set_ylim([-0.3, 0.9])
    # axs[2].set_xlim([-0.5, 1.2])
    # axs[2].set_ylim([-0.5, 1.2])

    # fig.gca().set_aspect('equal')
    # fig.axis('scaled')

    #plt.subplots_adjust(wspace=0.05, hspace=0)
    plt.tight_layout()
    fig.savefig("." + "/subplots_gradient.png", dpi=300, bbox_inches='tight')

# ----------------------------------------------------------------------------------------------------------------

# Set plot formatting

SMALL_SIZE = 10
MEDIUM_SIZE = 13
BIGGER_SIZE = 16

plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=BIGGER_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

plt.rcParams['font.family'] = 'serif'
plt.rcParams['mathtext.fontset'] = 'cm'

plot_subplots()
# plot_individual_pics()

# fig = plt.figure()
# # plt.plot(x_list, y_list, c='C0', label='$wind$')
# plt.plot(x_list, y_list, c='C0')
# # plt.legend(loc='upper right',frameon=False, prop={'size': 16})
# plt.legend(bbox_to_anchor=(1.0, 1.0), loc='upper right',frameon=False)
# plt.title("X Velocity Magnitude in the Forrestal ENU Frame (Gym) [m/s] and Rolling Average Wind Magnitude Estimate with Offset [m/s] over Time")
# plt.xlabel("X Position (m)")
# # plt.xlim((-1, 40))
# plt.ylabel("Y Position (m)")
# # plt.ylim((-0.6, 3.0))
# plt.gca().spines['top'].set_visible(False)
# plt.gca().spines['right'].set_visible(False)
# plt.savefig("." + "/wind-aware.png", dpi=300, bbox_inches='tight')