import os

DATAROOTA = './images/dog.jpg'
DATAROOTB = './images/sculpture.jpg'
NAME = 'test'
K_FINAL = '10'
K_PER_LEVE = '30'
FAST = 'False'
LAMBDA_T = '0.1'

step1 = ("python main.py" + " --datarootA " + DATAROOTA + " --datarootB " + DATAROOTB + " --name "+ NAME + " --k_final " + K_FINAL +
         " --k_per_level " + K_PER_LEVE + " --lambda_T " + LAMBDA_T)
os.system(step1)