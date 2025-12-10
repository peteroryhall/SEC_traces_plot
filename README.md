# Step 1: Create the environment and install required packages
# This tutorial will set up the "sec-graphs" environment and prepare it for plotting.

# Create the environment
micromamba create -n sec-graphs -y

# Activate the environment
micromamba activate sec-graphs

# Install essential packages
micromamba install -c conda-forge python matplotlib -y

# Optional: install pandas if you want sample data handling
# micromamba install -c conda-forge pandas -y
