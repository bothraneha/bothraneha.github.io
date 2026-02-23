This folder is a compact snapshot of a sintering model for metallic clusters on a surface, combining classic Ostwald Ripening (OR) with particle migration/coalescence (PMC) moves in a Metropolis NVT framework. The original MC code (which has successfully been used to study OR of Pt@TiO2(110)) is from https://github.com/alexandrova-lab-ucla/Sintering-Project/tree/main/testing/TiO2_testing, and I am extending it to include PMC alongside OR.

If you are new to it: think of it as a Monte Carlo simulator that evolves cluster sizes and positions on a 2D surface using a PES and size-dependent energetics.

## What’s inside

**Core simulation**
- `sintering_pmc_or.py` — main PMC + OR simulator (Metropolis MC)
- `sintering_ori.py` — OR-only baseline [Original sript from Alexandrova's GitHub]
- `param_pmc_or.py` — all runtime parameters (system size, temperature, PMC toggles)

**Initialization & data**
- `autoinit.py` — creates the starting `INIT` file from `PES` and `DATA`
- `PES` — 2D potential energy surface
- `DATA` — cluster radii/energies by size (used for energetics)
- `INIT` — initial cluster configuration (generated)

**Outputs & analysis**
- `LOG` — detailed run log (mechanism counters, merge details)
- `metropolis` — stepwise cluster list
- `analyze_LOG.py` — post-process `LOG` into diagnostic plots
- `plot_clusters_vs_steps.py` — number of clusters vs MC steps
- `plot_sweep.py` — visualize quick PMC parameter sweeps
- `sweep_results.csv` — sweep output (if sweep mode is enabled)

**Example plots in this snapshot**
- `clusters_vs_steps.png`
- `sweep_largest_gamma_0.5.png`
- `sweep_largest_gamma_1.0.png`
- `sweep_merges_vs_ppmc.png`

## Quick start

1. **Set parameters** in `param_pmc_or.py` (cluster counts, temperature, total steps, and PMC settings like `enable_pmc`, `p_pmc`, `s0`, `gamma`).
2. **Generate initial conditions**:
	- Run `autoinit.py` to create `INIT`.
3. **Run the simulation**:
	- Run `sintering_pmc_or.py` (PMC + OR) or `sintering_ori.py` (OR only).
4. **Analyze results**:
	- `analyze_LOG.py` for mechanism-level plots
	- `plot_clusters_vs_steps.py` for cluster-count evolution
	- `plot_sweep.py` if you have enabled sweep mode

## Notes & tips

- **Sweep mode**: Set `sweep_enabled = True` in `param_pmc_or.py` to run short calibration sweeps and write `sweep_results.csv`.
- **Units**: Geometry is in Å, energies are consistent with the PES and cluster data; temperatures follow the provided constants in `param_pmc_or.py`.
- **Reproducibility**: This code is intentionally parameter-first. When in doubt, check `param_pmc_or.py` first.

## Acknowledgment

Original sintering framework by Borna Zandkarimi (2020), extended here with PMC + OR diagnostics and sweep tooling.
