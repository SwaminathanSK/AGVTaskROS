import yaml
import numpy as np
import random

stream = open("cmd_vel (copy).yaml", "r")
docs = yaml.load_all(stream, yaml.FullLoader)
with open("cmd_vel.yaml", "w") as f:
    for list_doc in docs:
        if list_doc:
            noise = np.random.multivariate_normal(np.array([list_doc["linear"]['x'], list_doc["linear"]['y'], list_doc["linear"]['z']]), [[2, 0, 0], [0, 2, 0], [0, 0, 2]], size=None, check_valid='warn', tol=1e-8)
            list_doc = {"angular": list_doc["angular"], "linear": {"x" : list_doc["linear"]['x'] + noise[0], "y": list_doc["linear"]['y'] + noise[1], "z": list_doc["linear"]['z'] + noise[2]}}
            print(list_doc)

            yaml.dump(list_doc, f)