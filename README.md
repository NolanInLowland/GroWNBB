# GroWNBB

GroWNBB aims to find  sparse correspondences between cross-domain images, which have semantically related local structures, 
though could be quite different in semantics as well as appearances.

This is our PyTorch implementation for the GroWNBB with reference to [Neural-Best Buddies](https://github.com/kfiraberman/neural_best_buddies) and 
[Gromov-Wasserstein Learning](https://github.com/HongtengXu/gwl).

## Prerequisites

- Python 2 or 3
- CPU or NVIDIA GPU + CUDA CuDNN
- Pytorch > (1.x.x)

## Quick start

Run the following code to achieve a match between two images. The output results are in './results/test'.
```bash
cd GroWNBB
python script.py
```
You can match your own images by modifying DATAROOTA and DATAROOTB in script.py.

# GroWNBB
