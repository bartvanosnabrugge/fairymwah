# from ..context import fairymwah as fm
import os
from pathlib import Path
import shutil
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from fairymwah.wrappers import mwahwrapper as fm

os.chdir(os.path.dirname(os.path.realpath(__file__)))
mwah_sbmodule_folder = "/Users/ayx374/Documents/GitHub/forks/comphydShared_summa/submodules/summaWorkflow_public"

reset_test = False
if reset_test:
    ## manage context of test: copy test data to required folder
    results_folder_path = Path("./results")
    # remove results folder if exists
    if os.path.exists(results_folder_path):
        shutil.rmtree(results_folder_path)
    # create results folder
    # copy test_data to results folder as in mwah results and previous result share the same root folder (by default)

    shutil.copytree("./test_data/domain_BowAtBanff", "./results/domain_BowAtBanff")
    fm.create_folder_structure(mwah_sbmodule_folder)

#%% start example

#%% download data (downloads not included in example) - data specific input layer - part 1

## fm.run_download_ERA5_pressureLevel_paralell(mwah_sbmodule_folder)
## fm.run_download_ERA5_surfaceLevel_paralell(mwah_sbmodule_folder)
## fm.download_merit_hydro_adjusted_elevation(mwah_sbmodule_folder)
## fm.download_modis_mcd12q1_v6(mwah_sbmodule_folder)
## fm.download_soilgrids_soilclass_global(mwah_sbmodule_folder)

#%% process downloaded data - data specific input layer - part 2

### forcing ERA5 ###
#fm.merge_forcing(mwah_sbmodule_folder)
#fm.create_ERA5_shapefile(mwah_sbmodule_folder)

## merit hydro ##
#fm.unpack_merit_hydro(mwah_sbmodule_folder)
#fm.create_merit_hydro_virtual_dataset(mwah_sbmodule_folder)
#fm.specify_merit_hydro_subdomain(mwah_sbmodule_folder)
#fm.convert_merit_hydro_vrt_to_tif(mwah_sbmodule_folder)

## MODIS ##
#fm.create_modis_virtual_dataset(mwah_sbmodule_folder)
#fm.reproject_modis_virtual_dataset(mwah_sbmodule_folder)
#fm.specify_modis_subdomain(mwah_sbmodule_folder)
#fm.create_multiband_modis_vrt(mwah_sbmodule_folder)
#fm.convert_modis_vrt_to_tif(mwah_sbmodule_folder)
#fm.find_mode_modis_landclass(mwah_sbmodule_folder)

## SOILGRIDS ##
#fm.extract_soilgrids_domain(mwah_sbmodule_folder)

#%% model agnostic mapping layer
#fm.sort_catchment_shape(mwah_sbmodule_folder)

#fm.find_HRU_elevation(mwah_sbmodule_folder)
#fm.find_HRU_land_classes(mwah_sbmodule_folder)
#fm.find_HRU_soil_classes(mwah_sbmodule_folder)


#fm.make_single_weighted_forcing_file(mwah_sbmodule_folder)
#fm.make_all_weighted_forcing_files(mwah_sbmodule_folder)
#fm.temperature_lapsing_and_datastep(mwah_sbmodule_folder)

#%% Model specific processing layer
## Build repo clones and compile ## Compiling not included
#fm.clone_summa_repo(mwah_sbmodule_folder)
#fm.clone_mizuroute_repo(mwah_sbmodule_folder)
##fm.compile_summa(mwah_sbmodule_folder)
##fm.compile_mizuroute(mwah_sbmodule_folder)

## mizuRoute ##
#fm.copy_mizuroute_base_settings(mwah_sbmodule_folder)
#fm.create_mizuroute_network_topology_file(mwah_sbmodule_folder)
#fm.remap_summa_catchments_to_mizurouting(mwah_sbmodule_folder)
#fm.create_mizuroute_control_file(mwah_sbmodule_folder)


## SUMMA ##
fm.copy_summa_base_settings(mwah_sbmodule_folder)
fm.create_summa_file_manager(mwah_sbmodule_folder)
fm.create_summa_forcing_file_list(mwah_sbmodule_folder)
fm.create_summa_cold_state(mwah_sbmodule_folder)
fm.create_summa_trial_parameters(mwah_sbmodule_folder)
fm.initialize_summa_attributes_nc(mwah_sbmodule_folder)
fm.insert_soilclass_from_hist_into_summa_attributes(mwah_sbmodule_folder)
fm.insert_landclass_from_hist_into_summa_attributes(mwah_sbmodule_folder)
#fm.insert_elevation_from_hist_into_summa_attributes(mwah_sbmodule_folder)

fm.run_summa(mwah_sbmodule_folder)
#fm.run_mizuroute(mwah_sbmodule_folder)
#--- tested till here