**********************
ESA LTC 2022 Materials
**********************


This package contains the jupyter notebooks for the "Soil Moisture" and "Drought" exercises held at the `ESA Land Training Course 2022 <https://landtraining2022.esa.int/>`_.

The package is designed to run on `mybinder.org <https://mybinder.org/>`_. To open a notebook in your browser click on one of the following badges. Please note that opening the files on mybinder may take a few minutes (`it takes longer if the notebook was not used for some time <https://mybinder.readthedocs.io/en/latest/about/user-guidelines.html#performance-and-speed>`_).

If you wish to run the notebooks locally, see the 'Local installation' section below

------------

**Exercise 1 - Satellite Soil Moisture** (click badge to launch)

.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/pstradio/esa_ltc_materials/ltc_2023?labpath=lecture1_soil_moisture.ipynb

**Note**: *It can take a few minutes to open notebooks on mybinder. If jupyter-lab does not open in your browser after e.g. 5-10 minutes, refresh the mybinder loading page and try again.*

------------

**Exercise 2 - Droughts** (click badge to launch)
 
.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/pstradio/esa_ltc_materials/ltc_2023?labpath=lecture2_droughts.ipynb
 
**Note**: *It can take a few minutes to open notebooks on mybinder. If jupyter-lab does not open in your browser after e.g. 5-10 minutes, refresh the mybinder loading page and try again.*

------------

Jupyter notebook controls
-------------------------
If you are not familiar with Jupyter Notebooks, there are numerous tutorials available online, e.g. `here <https://www.dataquest.io/blog/jupyter-notebook-tutorial/>`_ or `here <https://jupyter-tutorial.readthedocs.io/en/latest/first-steps/create-notebook.html>`_. Some cells in the notebooks depend on running previous cells first (otherwise you will see an error message). Therefore it is recommended to either run all cells directly (click 🞂🞂) or running individual cells from top to bottom (►).

- **►** Run all code in a single block (cell)
- **■** Interrupt the kernel to stop any code execution
- **⟳** Restart the kernel
- **🞂🞂** Restart Kernel and run all cells

Other
-----
Data used in the tutorials is automatically downloaded when using binder (see the file ``postBuild``). However, if you want to download the data manually you can do this at https://cloud.geo.tuwien.ac.at/s/cNoJcXojZQyTfWG

At some point the materials might not be available anymore, in this case you can open an issue on github and we will send you the files.

Local installation
------------------
To run the notebooks locally, you need to clone the repository first (from the fork belonging to USER):

`git clone https://github.com/<USER>/esa_ltc_materials.git`

and move to the repository:

`cd path/to/esa_ltc_materials`

The datasets needed to run the notebooks are stored at the download link given in the `postBuild` script. Under linux you can just run it directly `./postBuild` which handles unzipping and creating the softlink for you. But you may also download and unzip the material manually, and copy (or softlink, with: `ln -s`) to the `esa_ltc_materials` local directory and rename it to `LTC_DATA`. The proper environment can be installed with 

`conda env create -f path/to/esa_ltc_materials/environment.yml -n esa_ltc` 

and activated: 

`conda activate esa_ltc`

After this, the notebooks can be run with the command: 

`jupyter lab`

Windows installation
--------------------
Download the repo with the installation and run scripts under this link:

https://owncloud.tuwien.ac.at/index.php/s/VunDPPGVaR8WKeM/download

Execute `install.bat` and then execute `run.bat`
