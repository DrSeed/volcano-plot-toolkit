import os, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True); os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(0); n=4000
lfc=rng.normal(0,1,n); base=rng.uniform(0,1,n)
# plant real DE genes
idx=rng.choice(n,200,replace=False); lfc[idx]+=rng.choice([-1,1],200)*rng.uniform(2,5,200)
p=np.clip(np.abs(rng.normal(0,1,n))*0.05,1e-12,1); p[idx]*=1e-6
y=-np.log10(p); sig=(np.abs(lfc)>1)&(y>2)
plt.figure(figsize=(6,5))
plt.scatter(lfc[~sig],y[~sig],s=4,c="grey",alpha=0.4)
plt.scatter(lfc[sig&(lfc>0)],y[sig&(lfc>0)],s=6,c="firebrick",label="up")
plt.scatter(lfc[sig&(lfc<0)],y[sig&(lfc<0)],s=6,c="royalblue",label="down")
plt.axhline(2,ls="--",c="k",lw=.7); plt.axvline(1,ls="--",c="k",lw=.7); plt.axvline(-1,ls="--",c="k",lw=.7)
plt.xlabel("log2 fold change"); plt.ylabel("-log10(p)"); plt.title("Volcano plot (demo data)"); plt.legend()
plt.tight_layout(); plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write(f"significant genes: {int(sig.sum())}\n")
print("ok")