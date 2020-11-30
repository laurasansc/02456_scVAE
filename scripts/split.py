import pandas as pd

dat = pd.read_table("/Users/laurasansc/Desktop/BioinformaticsSystemsBiology/DeepLearning/data_project/matrices_mex/hg19/counts.tsv")

dat_01 = dat.sample(frac=0.1)
dat_02 = dat.sample(frac=0.2)
dat_005 = dat.sample(frac=0.05)
dat_001 = dat.sample(frac=0.01)

dat_01.to_csv('counts_01.tsv', sep='\t', axis=1)
dat_02.to_csv('counts_02.tsv', sep='\t', axis=1)
dat_005.to_csv('counts_005.tsv', sep='\t', axis=1)
dat_001.to_csv('counts_005.tsv', sep='\t', axis=1)

