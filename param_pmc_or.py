#!/usr/bin/env python

# parameters to initialize the system
num_clust = 100        # num of Ptn clusters with n > 1
num_single_atom = 0  # num of single atom Pt
largest_cluster = 2  # largest initial cluster size in the system 

# total number of steps, write step, and temperature
# For quick tests, reduce MMAX. Restore to original for production runs.
MMAX   = 20000
wstep  =  1 
T      = 700

# unit cell parameters in A
unitcell_a = 13.216 
unitcell_b = 12.243
unitcell_c = 26.362

# primitive cell parameters in A (used for PES)
primcell_a = 6.607835831
primcell_b = 3.060749557
N_mesh = 11*11
xstep_max  =  primcell_a / 10.0
ystep_max  =  primcell_b / 10.0
numprimecellFactor = 2.0

# x and y boundaries of simulation
maxx   =  primcell_a * 17
minx   =  0.0
maxy   =  primcell_b * 17
miny   =  0.0

# constants
hartree_to_ev = 27.2114
k_J           = 1.38064852e-23
k_ev          = 8.6173303e-5
k_hartree     = k_ev/hartree_to_ev
kT            = k_hartree*T
beta          = 1.0/kT

# VDW radius of Pt in A
Ratom  =  1.75

# Control
CounterLimit = 50000
SinteringResultPlot = True # plot the result of sintering
LimitForOverlap = 1  # limit of total number of overlap process in one step. 


# --- PMC (particle migration + coalescence) controls ---
enable_pmc = False       # set False to run the original OR-only model
p_pmc = 0.005            # probability of attempting a PMC translation move each MC step (only if chosen cluster has n>=pmc_min_atoms)
pmc_min_atoms = 2       # only clusters with n >= this can undergo PMC translation
pmc_step_scale = 1.0    # PMC translation step ~ pmc_step_scale * (2*R_cluster)
# merging behavior: whether to merge with all overlapping neighbors (True) or only first neighbor found (False, safer)
pmc_merge_all = False
# maximum merges allowed in one PMC translation (safety cap). Only used if pmc_merge_all is True
pmc_merge_cap = 1
# if True, stop the simulation (raise) when all atoms coalesce into a single cluster (useful for debugging)
pmc_stop_on_full_coalesce = False  # don't abort by default; set True for debugging stops

# --- cluster-PES surrogate (gives ΔE for cluster translation in Metropolis) ---
use_cluster_pes = True
s0 = 0.30               # strength of cluster corrugation term (scaled from monomer PES)
gamma = 0.50            # size dependence: s(n) = s0 * n^{-gamma}
cluster_pes_avg_points = 1  # 1=center only; >1 averages a few nearby points (slower)

# --- extra PMC safety / split / sweep parameters ---
# maximum number of overlapping neighbors allowed for a single PMC translation without a strong negative ΔE
pmc_max_neighbors_allowed = 1
# require dE_total <= -pmc_merge_deltaE_threshold (eV) to allow merges with many neighbors
pmc_merge_deltaE_threshold = 0.10  # stricter: require larger energy gain to allow merge with > pmc_max_neighbors_allowed
# optional kinetic barrier for PMC merges (adds to ΔE before Metropolis)
pmc_barrier_scale = 0.02   # small per-atom barrier to slow merges
pmc_barrier_exponent = 0.5  # some size-dependence (sqrt)

# split move controls (reverse of merger, helps reversibility)
enable_split_moves = True
split_move_prob = 0.01      # per-step probability to attempt an explicit split move
split_move_min_atoms = 2    # minimal cluster size to consider splitting
# how many recent merges to remember for potential split reversals
pmc_merge_history_len = 2000
# if True, use deterministic choices from cluster_min_lookup (improves q_fwd/q_rev -> 1)
enable_detailed_balance_splits = False

# parameter sweep defaults (short calibration runs)
# Enable a quick PMC-only calibration sweep. Set back to False for production runs.
sweep_enabled = False  # turned off after running a short sweep
sweep_p_pmc_list = [0.005, 0.01, 0.02, 0.05]
sweep_s0_list = [0.1, 0.2, 0.3]
sweep_gamma_list = [0.5, 1.0]
sweep_steps_short = 2000

# --- mechanism logging ---
print_mechanism_every = wstep
