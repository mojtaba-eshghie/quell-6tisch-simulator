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
parser.add_argument('--simNum', type=int, help='number of simulations', default=5)
args = parser.parse_args()

'''
mote_count = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
pkt_periods = [5, 1, 0.5, 0.1, 0.05, 0.01]
square_sides = [6, 3, 2, 1]
'''



mote_count = [10, 20]
pkt_periods = [5, 1]
square_sides = [1,]


random.seed(time.time())

sim_id = 0

quell_results_dict = list()
of0_results_dict = list()
sim_id_dict = dict()


for mote_number in mote_count:

    for square_side in square_sides:

        for pkt_period in pkt_periods:

            for i in range(1, args.simNum + 1):
                #lets generate an sim_id
                sim_id += 1



                # for quell
                directory = sim_id.__str__()
                time.sleep(random.choice([0.2, 0.1, 0.3, 0.01, 1]))
                command = 'c:\python27\python.exe runSimOneCPU.py --gui --numRuns 1 --numCyclesPerRun 100 --numMotes {mote_number} --squareSide {square_side} --pkPeriod {pkt_period} --pkPeriodVar 0.1 --slotframeLength 23 --slotDuration 0.009 --simDataDir {directory} --objective_function quell'.format(mote_number=mote_number, square_side=square_side, pkt_period=pkt_period, directory=directory)
                print(command)
                return_code = run(command, shell=True, stdout=subprocess.PIPE, timeout=400)
                result = return_code.stdout.decode()
                PER = round(float(result.split('\n')[-3].split(' ')[1]), 4)
                quell_results_dict[sim_id] = PER
                print('QUELL: simulation identity: {0}, PER: {1}, pktPeriod:{2}, squareSide: {3}, numMotes: {4}'.format(sim_id.__str__(), PER.__str__(), pkt_period.__str__(), square_side.__str__(), mote_number.__str__()))
                print(result)



                # for of0
                time.sleep(random.choice([0.2, 0.1, 0.3, 0.01, 1]))
                command = 'c:\python27\python.exe runSimOneCPU.py --gui --numRuns 1 --numCyclesPerRun 100 --numMotes {mote_number} --squareSide {square_side} --pkPeriod {pkt_period} --pkPeriodVar 0.1 --slotframeLength 23 --slotDuration 0.009 --simDataDir {directory} --objective_function OF0'.format(mote_number=mote_number, square_side=square_side, pkt_period=pkt_period, directory=directory)
                return_code = run(command, shell=True, stdout=subprocess.PIPE, timeout=400)
                result = return_code.stdout.decode()
                print('OF0: simulation identity: {0}, PER: {1}, pktPeriod:{2}, squareSide: {3}, numMotes: {4}'.format(sim_id.__str__(), PER.__str__(), pkt_period.__str__(), square_side.__str__(), mote_number.__str__()))
                print(result)
                PER = round(float(result.split('\n')[-3].split(' ')[1]), 4)
                of0_results_dict[sim_id] = PER


                # to generate mean of PER
                if sim_id % 5 is 0:
                    temp_sum = 0
                    for j in range(0, 5):
                        temp_index = sim_id + j
                        temp_sum += quell_results_dict[temp_index]
                    quell_mean = temp_sum / 5

                    temp_sum=0
                    for j in range(0, 5):
                        temp_index = sim_id + j
                        temp_sum += of0_results_dict[temp_index]
                    of0_mean = temp_sum / 5
                    print('mean PER is, for quell: {0}, for OF0: {1}'.format(quell_mean, of0_mean))




                #here we are sure that simulation is ended, so lets add our sim index to the dict
                sim_id_dict.append({
                    'mote_number': mote_number,
                    'pkt_period': pkt_period,
                    'square_side': square_side,
                })





with open('sim_id_dict.json', 'w') as sim_id_storage:
    json.dump(sim_id_dict, sim_id_storage)


with open('quell_pers.txt', 'w') as all_pers:
    all_pers.write(quell_results_dict.__str__())

with open('OF0_pers.txt', 'w') as all_pers:
    all_pers.write(of0_results_dict.__str__())


#these dicts must be stored into json files
#sim_id dict
#quell_results_dict
#of0_results_dict