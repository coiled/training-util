import coiled

deps = ('coiled==0.0.30 dask-ml pyarrow python-graphviz scikit-learn ' +
        'matplotlib h5py tpot imageio zarr xgboost s3fs pytorch-cpu').split(' ')

coiled.create_notebook(
  name="training-lab",
  conda={
    "channels": ["conda-forge"],
    "dependencies": deps,
  },
  cpu=4,
  memory="16 GiB",
  files=["workspace.json", "run.sh"],
  description="Environment with dependencies for Coiled Dask training labs",
)
