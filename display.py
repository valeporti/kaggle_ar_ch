import matplotlib.pyplot as plt
from matplotlib import colors
from pprint import pprint as pp
import numpy as np

cmap = colors.ListedColormap(['#000000', '#0074D9','#FF4136','#2ECC40','#FFDC00','#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25'])
norm = colors.Normalize(vmin=0, vmax=9)
    
def plotResults(task_samples, predictions):
  for sample, prediction in zip(task_samples, predictions):
    t_in, t_out, prediction = np.array(sample["input"]), np.array(sample["output"]), np.array(prediction)
    titles = [f'Input {t_in.shape}', f'Output {t_out.shape}', f'Predicted {prediction.shape}']
    figures = [t_in, t_out, prediction]
    fig, axs = plt.subplots(1, 3, figsize=(2*3, 32))
    for i, (figure, title) in enumerate(zip(figures, titles)):
      plotOne(axs[i], figure, title)
    plt.show()

def showTotalColors():
  # 0:black, 1:blue, 2:red, 3:greed, 4:yellow,
  # 5:gray, 6:magenta, 7:orange, 8:sky, 9:brown
  plt.figure(figsize=(5, 2), dpi=100)
  plt.imshow([list(range(10))], cmap=cmap, norm=norm)
  plt.xticks(list(range(10)))
  plt.yticks([])
  plt.show()

def plotOne(ax, task_in_out, title):
  ax.imshow(task_in_out, cmap=cmap, norm=norm)
  ax.set_title(title)
  #ax.axis('off')
  ax.set_yticks([x-0.5 for x in range(1+task_in_out.shape[0])])
  ax.set_xticks([x-0.5 for x in range(1+task_in_out.shape[1])])  
  ax.set_xticklabels([])
  ax.set_yticklabels([])
  ax.grid(True, which='both', color='lightgrey', linewidth=0.5) 
  """ axs[0, fig_num].imshow(train_info[i]['input'], cmap=cmap, norm=norm)
  axs[0, fig_num].set_title(f'Train Input {i}')
  #axs[0, fig_num].axis('off')
  axs[0, fig_num].set_yticks(list(range(t_in.shape[0])))
  axs[0, fig_num].set_xticks(list(range(t_in.shape[1])))
  axs[1, fig_num].imshow(train_info[i]['output'], cmap=cmap, norm=norm)
  axs[1, fig_num].set_title(f'Train Output {i}')
  #axs[1, fig_num].axis('off')
  axs[1, fig_num].set_yticks(list(range(t_out.shape[0])))
  axs[1, fig_num].set_xticks(list(range(t_out.shape[1]))) """

def plot_task(task_info, n, name, test_task=False):
  # 0:black, 1:blue, 2:red, 3:greed, 4:yellow,
  # 5:gray, 6:magenta, 7:orange, 8:sky, 9:brown
  n_pairs = task_info['n_patterns'] + task_info['n_test']
  train_info, test_info = task_info['train'], task_info['test']
  
  plt.subplots_adjust(wspace=0, hspace=0)
  fig, axs = plt.subplots(2, n_pairs, figsize=(4*n_pairs,8),  dpi=50)
  fig_num = 0
  
  for i, t in enumerate(task_info['train']):
    t_in, t_out = np.array(t["input"]), np.array(t["output"])
    if (t_in > 9).any() or (t_out > 9).any(): print(f"Number Out of color range ({np.max(t_in)}, {np.max(t_out)}")
    plotOne(axs[0, fig_num], t_in, f'{n}: Train Input {i} - {t_in.shape} - {name}')
    plotOne(axs[1, fig_num], t_out, f'{n}: Train Output {i} - {t_out.shape} - {name}')
    fig_num += 1
  for i, t in enumerate(task_info['test']):
    t_in, t_out = np.array(t["input"]), np.array(t["output"]) if not test_task else None
    if (t_in > 9).any() or (t_out > 9).any(): print(f"Number Out of color range ({np.max(t_in)}, {np.max(t_out)}")
    plotOne(axs[0, fig_num], t_in, f'{n}: Test Input {i} - {t_in.shape} - {name}')
    if not test_task: 
      plotOne(axs[1, fig_num], t_out, f'Test Output {i} - {t_out.shape} - {name}')
    else:
      axs[1, fig_num].axis('off')
    fig_num += 1

  plt.tight_layout()
  plt.show()