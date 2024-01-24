import numpy as np  
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pareto

# Simulate variety data
num_varieties = 5000 

yields = np.random.normal(5, 1, size=num_varieties)   
drought_res = np.random.normal(3, 1, size=num_varieties)
pest_res = np.random.normal(2, 1, size=num_varieties)

varieties = [[yields[i], drought_res[i], pest_res[i]] for i in range(num_varieties)]

# Determine Pareto front  
front = pareto.eps_sort(varieties)  

# Convert front list to NumPy array
front = np.array(front)   

# Plot  
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(yields, drought_res, pest_res)
ax.plot(front.T[0], front.T[1], front.T[2], c='r')  

ax.set_xlabel('Yield')
ax.set_ylabel('Drought Resistance')   
ax.set_zlabel('Pest Resistance')
    
plt.show()