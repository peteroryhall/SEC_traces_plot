## Step 1: Create the environment and install required packages

This tutorial sets up the `sec-graphs` environment for plotting.

### Create the environment
```bash
micromamba create -n sec-graphs -y
```
Activate the environment
```bash
micromamba activate sec-graphs
```
Install essential packages
```
```bash
micromamba install -c conda-forge python matplotlib -y
```
Optional: install pandas for sample data
```bash
micromamba install -c conda-forge pandas -y
```
Clone the SEC traces plotting repository
```bash
git clone https://github.com/peteroryhall/SEC_traces_plot.git
cd SEC_traces_plot
```

## Step 2: Running the Script to Plot Your SEC Graph

1. Open the provided CSV template (`template_sec_data.csv`) and paste your SEC data into it.

   - Column 1 must be the X-axis: `Volume (mL)`
   - All additional columns are absorbance traces in `mAU`
   - Add as many traces as you want:
     ```
     Volume (mL),UV Trace 1,UV Trace 2
     ```

2. Save your edited file (e.g., `mydata.csv`).

3. Run the plotting script.  
   The script **requires** you to define the X and Y axis limits so it displays only the region you want.

   **Example: plot 0–25 mL on X and 0–200 mAU on Y**
   ```bash
   python plot_sec_traces.py mydata.csv --xmin 0 --xmax 25 --ymin 0 --ymax 200



