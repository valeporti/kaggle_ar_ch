import json

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