import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import math
import os
import seaborn as sns

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

fig, axs = plt.subplots(2, 1, figsize=(8,8), sharex=True)

df = pd.read_csv('fulldataplotting.csv', index_col=0)

df2 = pd.read_csv('wind_prof.csv', header=None)
df2.columns = ["t", "mag", "obs"]
df2["t"] = df2["t"].apply(lambda x: x/40.0)

df3 = pd.read_csv('lcmlog-2022-09-15.23.csv', index_col=0)
# t_list = df3["timestamp"]
wind_mag_list = df3["wind_mag"]

# axs[0] = sns.lineplot(data=data, x="t", y="x", hue='case', palette=['C0', 'C1', 'C2'], legend=False, ci='sd')
# axs[0].legend(['Baseline', 'Unaware', 'Aware'])
# axs[0].set_xlim([2.5, 27.5])
# axs[0].set_xlabel('Time (s)')
# axs[0].set_ylabel('X Position (m)')
# axs[0].set_title('X Position (m) vs. Time (s) with Square Gust')
# # plt.hold(True)
# # ax2 = plt.plot(df2["t"].to_numpy(), df2["obs"].to_numpy(), 'k--', [2.5, 27.5], [0,0], 'k--')
# # ax2 = sns.lineplot(data=df2[(df2.t >= 2.5) & (df2.t <= 27.5)], x="t", y="obs", palette=['#000000'], dashes=[(2, 2, 5, 2)], legend=False)

# axs[1].plot(df2["t"].to_numpy(), df2["obs"].to_numpy(), 'k--', [2.5, 27.5], [0,0], 'k--')

# plt.savefig('ResponseWithGust.png', dpi=300, bbox_inches='tight')

# plt.figure(figsize=(9, 6), dpi=300)
titleFont=20
axisFont=16
legendFont=16

axs[0] = sns.lineplot(data=df, x="t", y="x", hue='case', palette=['C2', 'C1', 'C0'], legend=False, errorbar='sd', ax=axs[0], label="_nolegend_")
axs[0].plot([2.5, 27.5], [0,0], 'k--')
axs[0].legend(['baseline', 'wind-unaware', 'wind-aware'], fontsize=BIGGER_SIZE, frameon=False, loc="upper left")
axs[0].set_xlim([2.5, 27.5])
axs[0].set_ylim([-0.25, 1])
axs[0].set_xlabel('Time (s)', fontsize=BIGGER_SIZE)
axs[0].set_ylabel('X Position (m)', fontsize=BIGGER_SIZE)
axs[0].spines['top'].set_visible(False)
axs[0].spines['right'].set_visible(False)

axs[0].tick_params(axis='both', which='major', labelsize=MEDIUM_SIZE)
axs[0].yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))
axs[0].set_xticks(np.arange(2.5, 30, 2.5))

# axs[0].rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
# plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
# ax.set_title('X Position (m) vs. Time (s) with Square Gust', fontsize=titleFont)
# plt.hold(True)
axs[1].plot(df2["t"].to_numpy(), df2["obs"].to_numpy()*5, 'k--', linewidth=2)
axs[1].plot(df2["t"].to_numpy(), wind_mag_list)
# ax2 = sns.lineplot(hue='case', data=df2[(df2.t >= 2.5) & (df2.t <= 27.5)], x="t", y="obs", palette=['C1'], dashes=[(2, 2, 5, 2)], legend=False, ax=axs[1])

axs[1].spines['top'].set_visible(False)
axs[1].spines['right'].set_visible(False)
axs[1].set_ylim([-1, 5])
axs[1].set_xlabel('Time (s)', fontsize=BIGGER_SIZE)
axs[1].set_ylabel('Wind Speed (m/s)', fontsize=BIGGER_SIZE)
axs[1].legend(['filtered', 'raw'], fontsize=BIGGER_SIZE, frameon=False, loc="upper left")
axs[1].yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))
axs[1].tick_params(axis='both', which='major', labelsize=MEDIUM_SIZE)
plt.subplots_adjust(wspace=0.05, hspace=0.05)

plt.savefig('ResponseWithGust.png', dpi=300, bbox_inches='tight')



fig = plt.figure()
# plt.plot(df2["t"].to_numpy(), df2["obs"].to_numpy()*5, 'k--', linewidth=2)
plt.plot(df2["t"].to_numpy(), wind_mag_list)
# ax2 = sns.lineplot(hue='case', data=df2[(df2.t >= 2.5) & (df2.t <= 27.5)], x="t", y="obs", palette=['C1'], dashes=[(2, 2, 5, 2)], legend=False, ax=axs[1])

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.ylim([-1, 5])
plt.xlim([12.5, 15])
plt.xlabel('Time (s)', fontsize=BIGGER_SIZE)
plt.ylabel('Wind Speed (m/s)', fontsize=BIGGER_SIZE)
# plt.legend(['raw', 'filtered'], fontsize=BIGGER_SIZE, frameon=False, loc="upper left")
plt.tick_params(axis='both', which='major', labelsize=MEDIUM_SIZE)

plt.savefig('thumbnail.png', dpi=300, bbox_inches='tight')