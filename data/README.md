# Data used in 02456_scVAE project

* 10x-68k-PMBC **raw** data set \*

	- *subset1300_counts.tsv.gz*: single-cell transcript counts - subset 1300 samples

	- *subset1300_celltypes.tsv*: cell classes - subset 1300 samples

	- *fullset_celltypes.tsv*: cell classes - full data set


* Latent representations, generated with **scVAE** tool, of 10x-68k-PMBC data \*\* \*\*\*

	 - *subset1300_lv10_H250.tsv*: latent values of scVAE Model 2 - 10 latent dimensions - subset 1300 samples
	 
	 - *subset1300_lv25_H500.tsv*: latent values of scVAE Model 7 - 25 latent dimensions - subset 1300 samples

  - *subset1300_lv50_H250.tsv*: latent values of scVAE Model 10 - 50 latent dimensions - subset 1300 samples
  
  - *subset15000_lv100_H500.tsv*: latent values of scVAE Model 15 - 100 latent dimensions - subset 1300 samples

 	 - *subset15000_lv10_H250.tsv*: latent values of scVAE Model 17 - 10 latent dimensions - subset 15000 samples
	 
	 - *subset15000_lv25_H500.tsv*: latent values of scVAE Model 18 - 25 latent dimensions - subset 15000 samples

  - *subset15000_lv50_H250.tsv*: latent values of scVAE Model 19 - 50 latent dimensions - subset 15000 samples
  
  - *subset15000_lv100_H500.tsv*: latent values of scVAE Model 20 - 100 latent dimensions - subset 15000 samples
  

* **PCA** on 10x-68k-PMBC data \*\*\*\*

  - *subset1300_pca10.tsv*: 10 principal components - subset 1300 samples
  
  - *subset1300_pca25.tsv*: 25 principal components - subset 1300 samples
    
  - *subset1300_pca50.tsv*: 50 principal components - subset 1300 samples
      
  - *subset1300_pca100.tsv*: 100 principal components - subset 1300 samples


\* we were not able to obtain the transcript counts neither for the full 10x-68k-PMBC data set nor for the subset of 15000 samples

\*\* more scVAE models were run, but only latent representations of the top performing models (subsets 1300 and 15000 samples) were used for classification with FFNN

\*\*\* models are enumerated following structure described in [this file](https://github.com/laurasansc/02456_scVAE/blob/main/code/scvae_commands.md)

\*\*\*\* PCA was not run on the subset of 15000 samples due to unavailability of the raw transcript counts subset of 15000 samples