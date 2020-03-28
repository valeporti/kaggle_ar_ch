import helpers as hp
import display as dp
from pprint import pprint as pp

def showNTrainingSamples(n, tasks, tasks_path, test_task=False, show=False):
  limit, count = n, 0
  for i, path in enumerate(tasks):
    count += 1
    if limit < count : break
    task_info = hp.getGeneralInfoFromTask(f'{tasks_path}/{path}')
    if show: pp(task_info)
    dp.plot_task(task_info, i, path.split('.')[0], test_task=test_task)