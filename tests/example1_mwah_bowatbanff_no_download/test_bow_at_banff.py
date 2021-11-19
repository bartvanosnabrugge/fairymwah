# from ..context import fairymwah as fm
import os
from pathlib import Path
import shutil
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import fairymwah as fm

os.chdir(os.path.dirname(os.path.realpath(__file__)))

## manage context of test: copy test data to required folder
results_folder_path = Path("./results")
# remove results folder if exists
if os.path.exists(results_folder_path):
    os.rmdir(results_folder_path)
# create results folder
# copy test_data to results folder as in mwah results and previous result share the same root folder (by default)

shutil.copytree("./test_data/domain_BowAtBanff", "./results/domain_BowAtBanff")

mwah_sbmodule_folder = "/Users/ayx374/Documents/GitHub/forks/comphydShared_summa/submodules/summaWorkflow_public"

fm.create_folder_structure(mwah_sbmodule_folder)
# fm.clone_summa_repo(mwah_sbmodule_folder)
# fm.clone_mizuroute_repo(mwah_sbmodule_folder)
# fm.merge_forcing(mwah_sbmodule_folder)
# fm.create_ERA5_shapefile(mwah_sbmodule_folder)
