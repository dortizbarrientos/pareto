# Variety Data Simulation and Pareto Front Visualization

## Description
This repository contains a Python script that simulates crop variety data, including **yield**, **drought resistance**, and **pest resistance**. It uses this simulated data to identify and visualize the **Pareto front** in 3D. The Pareto front helps to visualize optimal trade-offs between these competing traits, commonly used in multi-objective optimization problems like plant breeding.

The script generates random data for 5000 varieties, calculates the Pareto front using the `pareto` library, and plots the data in 3D space using **matplotlib**.

### Key Features:
- Simulates variety data for three traits: yield, drought resistance, and pest resistance.
- Identifies the Pareto front using the `pareto` library.
- Visualizes the entire dataset and the Pareto front in a 3D plot.

## Requirements
To run the script, you will need the following Python packages installed:

- **streamlit** (>=1.10)
- **pandas** (>=1.3)
- **numpy** (>=1.22)
- **matplotlib** (>=3.5)
- **pareto** (version not specified)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/variety-pareto-front.git
    cd variety-pareto-front
    ```

2. **Install the required packages**:
   You can install the necessary dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once you have cloned the repository and installed the dependencies, you can run the script as follows:

```bash
python pareto_visualization.py
```

This will:
- Simulate data for 5000 varieties with three traits: yield, drought resistance, and pest resistance.
- Compute the Pareto front of these traits.
- Visualize the data in a 3D scatter plot with the Pareto front highlighted in red.

### Code Overview

1. **Simulate variety data**:
   - 5000 varieties are simulated, each with random values for yield, drought resistance, and pest resistance.
   - The `numpy` library is used to generate these random values.
   
2. **Compute Pareto front**:
   - The `pareto.eps_sort` function is used to compute the Pareto front from the generated variety data.
   
3. **Visualization**:
   - A 3D scatter plot is created using `matplotlib`, where each point represents a variety.
   - The Pareto front is plotted in red on the 3D plot to highlight the optimal trade-offs between the three traits.

### Plot
The resulting plot will show:
- **Blue scatter points** representing the simulated variety data in terms of yield, drought resistance, and pest resistance.
- A **red line** indicating the Pareto front, showing the set of non-dominated varieties that offer optimal trade-offs among the three traits.

## Project Structure

```
variety-pareto-front/
│
├── pareto_visualization.py       # Main Python script for simulating data and visualizing the Pareto front
├── requirements.txt              # Requirements file listing dependencies
├── README.md                     # This README file
```

## Contributing
Contributions are welcome! If you would like to improve the script, add more features (e.g., more traits or analysis methods), or fix any issues, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
For any questions or feedback, please contact:

- **Daniel Ortiz-Barrientos**
- Email: [d.ortizbarrientos@uq.edu.au](mailto:d.ortizbarrientos@uq.edu.au)

## Addition of Figure
3D Scatter Plot of Variety Data with Pareto Front (Improved Visualization)

This figure represents an 3D scatter plot showcasing the relationship between three traits of 5000 simulated crop varieties: yield (x-axis), drought resistance (y-axis), and pest resistance (z-axis). The blue points represent individual crop varieties, with their positions determined by their corresponding trait values.

The Pareto front is shown using distinct red markers, making it clear which are the optimal varieties. The markers indicate varieties that offer the best trade-offs among the three traits

Key Elements:

Blue Points: Represent individual crop varieties, with random values for yield, drought resistance, and pest resistance.

Red Markers: Represent the varieties that form the Pareto front, showing the optimal balance among the three traits. These markers stand out due to their larger size and distinct colour.

Axes:
X-axis (Yield): Measures crop yield.
Y-axis (Drought Resistance): Measures the crop’s resistance to drought.
Z-axis (Pest Resistance): Measures the crop’s resistance to pests.
