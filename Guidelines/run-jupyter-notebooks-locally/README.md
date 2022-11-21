# How can I work with Jupyter notebooks locally?

Note: There are multiple ways to work with [Jupyter](https://jupyter.org/) notebooks and manage Python environments on your local machine. This guideline describes the _recommended_ setup for the accompanying exercises of the Artificial Intelligence course.

1. Download, install and launch the latest version of [Anaconda Individual Edition](https://www.anaconda.com/products/individual)
![](./screenshots/1.png)
2. Create a new conda environment and install required packages (use the latest available versions).
![](./screenshots/2a.png)
![](./screenshots/2b.png)
  - The required packages will vary between exercises. Install at least `notebook`, `pandas`, `scikit-learn` and `matplotlib`, `seaborn`, `statsmodels`.
![](./screenshots/2c.png)
  - Click apply and wait for the installation to finish.
![](./screenshots/2d.png)
  - For some exercises, we may provide a predefined environment file (e.g. [env-hhz-py38.yml](./env-hhz-py38.yml)) that simplifies the installation of required package dependencies and allows to setup reproducible environments across different work stations.
![](./screenshots/2f.png)
3. Launch notebook and run Python code
![](./screenshots/3.png)
  - Either navigate to existing notebooks (`.ipynb` files), or create a new notebook as shown
![](./screenshots/4.png)
![](./screenshots/5.png)

