# Content

This repository contains code and data for our paper:

> Bossek, J., & Sudholt, D. (2021). Do Additional Optima Speed Up Evolutionary Algorithms?. In Proceedings of the 16th ACM/SIGEVO Workshop on Foundations of Genetic Algorithms (FOGA XVI), Dornbirn, Austria.

## Note

* Files `studyX_parameters.py` produce the parameter settings for our experiments. Each of these files generates a csv setup files in data/.
* The R-script `submitter.R` runs the algorithms adopting the R-package [batchtools](https://github.com/mllg/batchtools) for massive parallelization of runs. This script should work fine locally (if not HPC is available), but execution may take some time due to 100k+ runs.
* File `collect.R` collects the raw algorithm run data.
* File `analyze.R` eventually generates the plots.

## Contact

Please address questions to the author Jakob Bossek <j.bossek@gmail.com>.
