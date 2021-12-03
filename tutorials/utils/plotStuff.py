import numpy as np
import matplotlib.pyplot as plt
from IPython import display
from ai_economist.foundation.utils import load_episode_log
import plotting
import os

base = "../rllib/phase1/dense_logs/"
file_loc = "../rllib/phase1/ckpts/"
log_path = os.path.join(base, "logs_0000000000486000/env000.lz4")
dense_log = load_episode_log(log_path)
(fig0, fig1, fig2), incomes, endows, c_trades, all_builds = plotting.breakdown(dense_log)
fig = plotting.vis_world_range(dense_log, t0=0, tN=200, N=5)
fig.savefig('vis_world_range_p2_3.png') 
fig0.savefig('p_2_breakdown6.png')
fig1.savefig('p_2_breakdown7.png')
fig2.savefig('p_2_breakdown8.png')
plotting.get_all_taxes_from_all_logs(base)
plotting.get_all_rwds_from_all_logs(base)