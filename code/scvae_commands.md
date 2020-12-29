# Commands used in scVAE tool


*Z: latent dimensions*

*H: hidden layers*

*more information in [scVAE repository](https://github.com/scvae/scvae)*

## Models 1 - 16: 10x-PBMC-68k subset 1300 samples (~2%)

**Model 1**: Z = 10, H = 100

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 10 -H 100 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 10 -H 100 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 2**: Z = 10, H = 250

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 10 -H 250 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 10 -H 250 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 3**: Z = 10, H = 500

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 10 -H 500 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 10 -H 500 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 4**: Z = 10, H = 1000

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 10 -H 1000 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 10 -H 1000 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 5**: Z = 25, H = 100

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 25 -H 100 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 25 -H 100 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 6**: Z = 25, H = 250

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 25 -H 250 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 25 -H 250 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 7**: Z = 25, H = 500

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 25 -H 500 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 25 -H 500 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 8**: Z = 25, H = 1000

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 25 -H 1000 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 25 -H 1000 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 9**: Z = 50, H = 100

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 50 -H 100 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 50 -H 100 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 10**: Z = 50, H = 250

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 50 -H 250 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 50 -H 250 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 11**: Z = 50, H = 500

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 50 -H 500 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 50 -H 500 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 12**: Z = 50, H = 1000

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 50 -H 1000 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 50 -H 1000 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 13**: Z = 100, H = 100

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 100 -H 100 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 100 -H 100 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 14**: Z = 100, H = 250

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 100 -H 250 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 100 -H 250 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 15**: Z = 100, H = 500

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 100 -H 500 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 100 -H 500 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 16**: Z = 100, H = 1000

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 100 -H 1000 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 1300 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 100 -H 1000 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

## Models 17 - 20: 10x-PBMC-68k subset 15000 samples (~20%)

*For each latent dimension (Z), the top performing model trained on the small subset (1300) was run.*

<br>

**Model 17**: Z = 10, H = 250

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 15000 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 10 -H 250 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 15000 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 10 -H 250 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 18**: Z = 25, H = 500

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 15000 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 25 -H 500 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 15000 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 25 -H 500 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 19**: Z = 50, H = 250

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 15000 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 50 -H 250 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 15000 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 50 -H 250 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>

**Model 20**: Z = 100, H = 500

`python3 -m scvae train 10x-PBMC-68k.json --example-filter random 15000 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 100 -H 500 -K 11 -e 100`

`python3 -m scvae evaluate 10x-PBMC-68k.json --example-filter random 15000 --split-data-set --splitting-fraction 0.8 -m GMVAE -r negative_binomial -l 100 -H 500 -K 11 --decomposition-methods pca tsne --included-analyses metrics latent_values learning_curves predictions images decompositions latent_space`

<br>