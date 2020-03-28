import json
from itertools import product

def loadJsonFromPath(path):
  j = None
  with open(path, 'r') as f:
    j = json.load(f)
  return j

def getGeneralInfoFromTask(task_path):
  j = loadJsonFromPath(task_path)
  j_train, j_test = j['train'], j['test']
  n_patterns, n_test = len(j_train), len(j_test)
  return {
    'task_json': j, 
    'train': j_train, 
    'test': j_test, 
    'n_patterns': n_patterns,
    'n_test': n_test
  }

getNeighCells = lambda x, i, j: { 
  (ip, jp) : x[i+ip, j+jp] 
    for ip, jp in product([1, -1, 0], repeat=2) 
      if 0 <= i+ip < x.shape[0] and 0 <= j+jp < x.shape[1]
}

createGridDict = lambda m: { (i,j): { } for i in range(m.shape[0]) for j in range(m.shape[1]) }