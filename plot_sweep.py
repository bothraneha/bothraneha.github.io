#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('sweep_results.csv')

# unique parameters
pp = sorted(df['p_pmc'].unique())
s0s = sorted(df['s0'].unique())
gammas = sorted(df['gamma'].unique())

for g in gammas:
    sub = df[df['gamma']==g]
    # pivot table: rows s0, cols p_pmc -> largest_cluster
    pivot = sub.pivot(index='s0', columns='p_pmc', values='largest_cluster')
    plt.figure(figsize=(6,4))
    plt.title(f'Largest cluster after sweep (gamma={g})')
    im = plt.imshow(pivot.values, origin='lower', aspect='auto', cmap='Reds')
    plt.colorbar(im, label='largest cluster size')
    plt.xticks(range(len(pp)), [str(x) for x in pp])
    plt.yticks(range(len(s0s)), [str(x) for x in s0s])
    plt.xlabel('p_pmc')
    plt.ylabel('s0')
    plt.tight_layout()
    outname = f'sweep_largest_gamma_{g}.png'
    plt.savefig(outname, dpi=200)
    print('Wrote', outname)

# Also generate a scatter map of merges vs p_pmc
plt.figure(figsize=(6,4))
for g in gammas:
    sub = df[df['gamma']==g]
    plt.plot(sub['p_pmc'], sub['merges'], marker='o', label=f'gamma={g}')
plt.xlabel('p_pmc')
plt.ylabel('merges (short sweep)')
plt.title('Merges vs p_pmc (each s0 shown as symbol)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('sweep_merges_vs_ppmc.png', dpi=200)
print('Wrote sweep_merges_vs_ppmc.png')
