### Steps I took to perform the analysis

- First I downloaded CSV datasets from *https://energydata.info/datasets* regarding solar radiation measurments from **Togo**, **Benin**, and **Sierra Leone,**
- Then I added a new column to each dataset named **country** with values same as the country the dataset belongs to,
- Then I merged all the three files in to a single file name *merged-solar-solar-radiation-measurement.csv* which can be found in this folder,
- Then I performed the data analysis in the jupyter notebook *EDA.ipynb*. (The notebook is self explanatory.)

*NB: make sure to add the python virtual environment as a jupyter kernel*

**command**: *python -m ipykernel install --user --name=venv_name*

*Replace `venv_name` with the name of the virtual environment where packages are installed.*
