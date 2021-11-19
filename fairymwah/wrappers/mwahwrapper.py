# mwah_wrapper.py

import sys
import os
import subprocess
import functools

submodule_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
        '..','..','submodules','summaWorkflow_public')

def setdefaultpath(submodule_path):
    if not submodule_path:
        submodule_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
        '..','..','submodules','summaWorkflow_public')
    return submodule_path


##WIP
def localworkingdir(func):
    """Decorator - Changes working dir to script_path and resets working dir afterwards"""
    @functools.wraps(func)
    def wrapper(script_path,*args,**kwargs):
        main_working_dir = os.getcwd()
        script_dir = os.path.dirname(script_path)
        os.chdir(script_dir)
        print('working dir of decorator ' + script_dir)
        print(os.getcwd)
        try:
            return func(script_path,*args,**kwargs)
        finally:
            os.chdir(main_working_dir)

def exec_python_lwd(script_path,*args,**kwargs):
    """Executes python script with localized working directory.
    Changes working dir to folder of python script before executing.
    Then changes back to original working directory.

    Args:
        script_path (path string): Path to python script
    """
    main_working_dir = os.getcwd()
    script_dir = os.path.dirname(script_path)
    os.chdir(script_dir)
    exec(open(script_path).read(),globals(),globals())
    os.chdir(main_working_dir)

def subprocess_lwd(script_path,*args,**kwargs):
    main_working_dir = os.getcwd()
    script_dir = os.path.dirname(script_path)
    os.chdir(script_dir)
    subprocess.call(['sh', script_path])
    os.chdir(main_working_dir)    


#%% From here the wrapper functions start

### 1 folder prep
def create_folder_structure(submodule_path: str=None):
    """    Executes the code from summaWorkflow_public step 1_folder_prep. Description from local python file:
    SUMMA workflow: make folder structure
    Makes the initial folder structure for a given control file. All other files in the workflow will look for the file `control_active.txt` during their execution. This script:

    1. Copies the specified control file into `control_active.txt`;
    2. Prepares a folder structure using the settings in `control_active.txt`.
    3. Creates a copy of itself to be stored in the new folder structure.

    The destination folders are referred to as "domain folders".

    :param submodule_path: path to the summaWorkflow_public repository. Defaults to "../submodules/summaWorkflow_public".
    :type submodule_path: str
    """
    if not submodule_path:
        submodule_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
        '..','..','submodules','summaWorkflow_public')

    python_file_to_run = os.path.join(submodule_path,'1_folder_prep','make_folder_structure.py')

    exec_python_lwd(python_file_to_run)

### 2 install
def clone_summa_repo(
    submodule_path: str=os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)),
    '..','..','submodules','summaWorkflow_public'))
    ):

    """This code downloads the latest version of the code base. sh script.
    Settings are given in the control file of mwah.

    Relevant settings in `control_active.txt` that the code in this folder uses:
    - **github_summa, github_mizu**: GitHub URLs from which to clone SUMMA and mizuRoute.

    Args:
        submodule_path (str, optional): path to the summaWorkflow_public repository. 
        Defaults to "../submodules/summaWorkflow_public".
    """
    script_path = os.path.join(submodule_path,'2_install','1a_clone_summa.sh')
    subprocess_lwd(script_path)


def compile_summa(submodule_path: str):

    """[Description]]

    Args:
        submodule_path (str, optional): path to the summaWorkflow_public repository. 
    """
    script_path = os.path.join(submodule_path,'2_install','1b_compile_summa.sh')
    subprocess_lwd(script_path)

def clone_mizuroute_repo(submodule_path: str):
    """[Description]]

    Args:
        submodule_path (str, optional): path to the summaWorkflow_public repository. 
    """
    script_path = os.path.join(submodule_path,'2_install','2a_clone_mizuroute.sh')
    subprocess_lwd(script_path)


def compile_mizuroute(submodule_path: str):
    """[Description]]

    Args:
        submodule_path (str, optional): path to the summaWorkflow_public repository. 
    """
    script_path = os.path.join(submodule_path,'2_install','2b_compile_mizuroute.sh')
    subprocess_lwd(script_path)

### 3a forcing
def download_ERA5_pressureLevel_annual():
    pass

def download_ERA5_surfaceLevel_annual():
    pass

def run_download_ERA5_pressureLevel_paralell():
    pass

def run_download_ERA5_surfaceLevel_paralell():
    pass

def download_ERA5_geopotential():
    pass

def merge_forcing(submodule_path: str=submodule_path):
    """ 3a_forcing, 2_merge_forcing
Combine separate surface and pressure level downloads
Creates a single monthly `.nc` file with SUMMA-ready variables for further processing. 
Combines ERA5's `u` and `v` wind components into a single directionless wind vector.

This script goes through the following steps:
1. Convert longitude coordinates in pressureLevel file to range [-180,180]
2. Checks
- are lat/lon the same for both data sets?
- are times the same for both datasets?
3. Aggregate data into a single file 'ERA5_NA_[yyyymm].nc', keeping the relevant metadata in place

    Args:
        submodule_path (str, optional): path to the summaWorkflow_public repository. Defaults to submodule_path.
    """
    python_file_to_run = os.path.join(submodule_path,'3a_forcing','2_merge_forcing',
    'ERA5_surface_and_pressure_level_combiner.py')

    exec_python_lwd(python_file_to_run)

def create_ERA5_shapefile(submodule_path: str=submodule_path):
    """ mwah workflow 3a_forcing, 3_create_shapefile
    The shapefile for the forcing data needs to represent the regular latitude/longitude grid of the ERA5 data. We need this for later intersection with the catchment shape(s) so we can create appropriately weighted forcing for each model element.

Notebook/script reads location of merged forcing data and the spatial extent of the data from the control file. 

## Assumptions not included in `control_active.txt`
- Code assumes that the merged forcing contains dimension variables with the names "latitude" and "longitude". This is the case for ERA5. 

    Args:
        submodule_path (str, optional): [description]. Defaults to submodule_path.
    """
    python_file_to_run = os.path.join(submodule_path,'3a_forcing','3_create_shapefile',
    'create_ERA5_shapefile.py')

    exec_python_lwd(python_file_to_run)



 ### 3b parameters
 ## Merit Hydro

def download_merit_hydro_adjusted_elevation():
     pass

def unpack_merit_hydro():
    pass

def create_merit_hydro_virtual_dataset():
    pass

def specify_merit_hydro_subdomain():
    pass

def convert_merit_hydro_vrt_to_tif():
    pass

## MODIS

def download_modis_mcd12q1_v6():
    pass

def create_modis_virtual_dataset():
    pass

def reproject_modis_virtual_dataset():
    pass

def specify_modis_subdomain():
    pass

def create_multiband_modis_vrt():
    pass

def convert_modis_vrt_to_tif():
    pass

def find_mode_modis_landclass():
    pass

### Soilgrids

def download_soilgrids_soilclass_global():
    pass

def extract_soilgrids_domain():
    pass

### 4a sort shape
def sort_catchment_shape():
    pass

### 4b remapping
## 1 topo
def find_HRU_elevation():
    pass

def find_HRU_soil_classes():
    pass

def find_HRU_land_classes():
    pass

## 2 forcing
def make_single_weighted_forcing_file():
    pass

def make_all_weighted_forcing_files():
    pass

def temperature_lapsing_and_datastep():
    pass

### 5 model input
## mizuRoute
def read_mizuroute_base_settings():
    pass

def copy_mizuroute_base_settings():
    pass

def create_mizuroute_network_topology_file():
    pass

def remap_summa_catchments_to_mizurouting():
    pass

def create_mizuroute_control_file():
    pass

## SUMMA
def read_summa_base_settings():
    pass

def copy_summa_base_settings():
    pass

def create_summa_file_manager():
    pass

def create_summa_forcing_file_list():
    pass

def create_cold_state():
    pass

def create_trial_parameters():
    pass

# attributes

def initialize_summa_attributes_nc():
    pass

def insert_soilclass_from_hist_into_summa_attributes():
    pass

def insert_landclass_from_hist_into_summa_attributes():
    pass

def insert_elevation_from_hist_into_summa_attributes():
    pass

### 6 Model runs
def run_summa():
    pass

def run_summa_as_array():
    pass

def run_mizuroute():
    pass

### 7 Visualization

def plot_mizuroute_and_summa_shapefiles():
    pass

def plot_ERA5_download_coordinates_and_catchment_shapefile():
    pass

def plot_forcing_grid_vs_catchment_averaged():
    pass

def plot_temperature_lapse_rates():
    pass

def plot_geospatial_parameters_to_model_elements():
    pass

def plot_SWE_SM_ET_Q_per_GRU():
    pass

def plot_SWE_and_streamflow_per_HRU():
    pass





#%% test area
mwah_sbmodule_folder = '/Users/ayx374/Documents/GitHub/forks/comphydShared_summa/submodules/summaWorkflow_public'

#create_folder_structure(mwah_sbmodule_folder)
#clone_summa_repo(mwah_sbmodule_folder)
clone_mizuroute_repo(mwah_sbmodule_folder)
#merge_forcing(mwah_sbmodule_folder)
#create_ERA5_shapefile(mwah_sbmodule_folder)


