#!/bin/bash

# Script to download ERA5 surface level data
# Reads download path, years to download and spatial extent from 'summaWorkflow_public/0_control_files/control_active.txt'.

module load python

# --- Settings
# -- Find where to save data
# Find the line with the forcing path
setting_line=$(grep -m 1 "forcing_raw_path" ../../0_control_files/control_active.txt) # -m 1 ensures we only return the top-most result. This is needed because variable names are sometimes used in comments in later lines

# Extract the path
forcing_path=$(echo ${setting_line##*|}) # remove the part that ends at "|"
forcing_path=$(echo ${forcing_path%% #*}) # remove the part starting at '#'; does nothing if no '#' is present

# Specify the default path if needed
if [ "$forcing_path" = "default" ]; then
  
 # Get the root path
 root_line=$(grep -m 1 "root_path" ../../0_control_files/control_active.txt)
 root_path=$(echo ${root_line##*|}) 
 root_path=$(echo ${root_path%% #*}) 
 
 # Get the domain path
 domain_line=$(grep -m 1 "domain_name" ../../0_control_files/control_active.txt)
 domain_name=$(echo ${domain_line##*|}) 
 domain_name=$(echo ${domain_name%% #*})  
 
 forcing_path="${root_path}/domain_${domain_name}/forcing/1_ERA5_raw_data/"
fi

# Make the folder if it doesn't exist
mkdir -p $forcing_path

# -- Find temporal and spatial domain
# - time
setting_line=$(grep -m 1 "forcing_raw_time" ../../0_control_files/control_active.txt)
years=$(echo ${setting_line##*|}) 
years=$(echo ${years%% #*}) 
arrayYears=(${years//,/ }) # split string into array for later use, based on delimiter ','

# - space
setting_line=$(grep -m 1 "forcing_raw_space" ../../0_control_files/control_active.txt)
coordinates=$(echo ${setting_line##*|}) 
coordinates=$(echo ${coordinates%% #*})


# --- Parallel runs
# Build the target variable (we need this because we can't use brace expansion based on 'arrayYears'
years=""; 
for (( year=$(( arrayYears[0] )); year<=$(( arrayYears[1] )); year++ )); do
 years="$years $year";
done

# Run the ERA5 downloads with the parallel command, and move them to background
parallel --jobs=5 python download_ERA5_surfaceLevel_annual.py ::: $years ::: $coordinates ::: $forcing_path

# --- Code provenance
# Generates a basic log file in the domain folder and copies the control file and itself there.

# Make a log directory if it doesn't exist
log_path="${forcing_path}/_workflow_log"
mkdir -p $log_path

# Log filename
today=`date '+%F'`
log_file="${today}_surface_level_log.txt"

# Copy this script
this_file='run_download_ERA5_surfaceLevel.sh'
that_file='download_ERA5_surfaceLevel_annual.py'
cp $this_file $log_path
cp $that_file $log_path

# Create a log file
echo "Log generated by ${this_file} on `date '+%F %H:%M:%S'`"  > $log_path/$log_file # 1st line, store in new file
echo "Downloaded ERA5 surface level data for space (lat_max, lon_min, lat_min, lon_max) [${coordinates}] for time Jan-${arrayYears[0]} / Dec-${arrayYears[1]}" >> $log_path/$log_file # 2nd line, append to existing file