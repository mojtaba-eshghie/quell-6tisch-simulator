'''
c:\python27\python.exe runSimOneCPU.py --gui --numRuns 1 --numCyclesPerRun 100 --scheduler flowp
--numMotes 8
--squareSide 2
--pkPeriod 0.01
--pkPeriodVar 0
--slotframeLength 101
--slotDuration 0.01
--objective_function
--simDataDir simData3
'''
from subprocess import run
import subprocess
import argparse
import json
import time
import random

parser = argparse.ArgumentParser(description='6tisch simulator')
parser.add_argument('--simNum', type=int, help='number of simulations', default=10)
args = parser.parse_args()

#mote_count = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
mote_count = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
pkt_period = [5, 1, 0.5, 0.1, 0.05, 0.01]
square_side = [6, 3, 2, 1]


command = "c:\python27\python.exe runSimOneCPU.py --gui --numRuns 1 --numCyclesPerRun 100 --squareSide 1 --pkPeriod 0.01 --pkPeriodVar 0.01 --slotframeLength 23 --slotDuration 0.005 --objective_function {ofname} --simDataDir {ofname} --numMotes {motenumber}"

quell_results_aggregated = dict()
quell_results_dict = dict()

of0_results_aggregated = dict()
of0_results_dict = dict()


random.seed(time.time())

for mote_number in mote_count:
    for i in range(1, args.simNum + 1):
        #for quell
        time.sleep(random.choice([0.2, 0.1, 0.3, 0.01, 1]))


        command = "c:\python27\python.exe runSimOneCPU.py --gui --numRuns 1 --numCyclesPerRun 100 --squareSide 1 --pkPeriod 0.01 --pkPeriodVar 0.01 --slotframeLength 23 --slotDuration 0.005 --objective_function {0} --simDataDir {1} --numMotes {2}".format('quell_a', 'quell', str(mote_number))
        print(command)
        return_code = run(command, shell=True, stdout=subprocess.PIPE, timeout=400)
        result = return_code.stdout.decode()
        print('simulating with {0}, sim number is: {1}, mote num is: {2}'.format('quell', i, mote_number))
        print(result)
        PER = round(float(result.split('\n')[-3].split(' ')[1]), 4)
        quell_results_dict[i] = PER


        #for of0
        time.sleep(random.choice([0.2, 0.1, 0.3, 0.01, 1]))
        command = "c:\python27\python.exe runSimOneCPU.py --gui --numRuns 1 --numCyclesPerRun 100 --squareSide 1 --pkPeriod 0.01 --pkPeriodVar 0.01 --slotframeLength 23 --slotDuration 0.005 --objective_function {0} --simDataDir {1} --numMotes {2}".format('OF0_a', 'OF0', str(mote_number))
        print(command)
        return_code = run(command, shell=True, stdout=subprocess.PIPE, timeout=400)
        result = return_code.stdout.decode()
        print('simulating with {0}, sim number is: {1}, mote num is: {2}'.format('OF0', i, mote_number))
        print(result)
        PER = round(float(result.split('\n')[-3].split(' ')[1]), 4)
        of0_results_dict[i] = PER


    temp_sum = 0
    for i, per in quell_results_dict.items():
        temp_sum += per
    quell_results_aggregated[mote_number] = temp_sum / args.simNum
    del quell_results_dict
    quell_results_dict = dict()


    temp_sum = 0
    for i, per in of0_results_dict.items():
        temp_sum += per
    of0_results_aggregated[mote_number] = temp_sum / args.simNum
    del of0_results_dict
    of0_results_dict = dict()


with open('quell_per_results.json', 'w') as quell_per_results:
    json.dump(quell_results_aggregated, quell_per_results)


with open('of0_per_results.json', 'w') as of0_per_results:
    json.dump(of0_results_aggregated, of0_per_results)