import matplotlib.pyplot as plt
plt.rcParams["savefig.dpi"] = 300

def plot_data(x_data, y_data, x_title, y_title, plot_title, save_path=None, add_grid=True):
    
    plt.plot(x_data, y_data, marker="o")
    plt.xlabel(x_title)
    plt.ylabel(y_title) 
    plt.title(plot_title)
    plt.grid(add_grid)
    plt.show()
    
    
