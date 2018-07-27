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
import random
import time

parser = argparse.ArgumentParser(description='6tisch simulator')
parser.add_argument('--simNum', type=int, help='number of simulations', default=10)
args = parser.parse_args()

mote_count = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]




command = "c:\python27\python.exe runSimOneCPU.py --gui --numRuns 1 --numCyclesPerRun 100 --squareSide 1 --pkPeriod 0.01 --pkPeriodVar 0.01 --slotframeLength 23 --slotDuration 0.005 --objective_function {ofname} --simDataDir {ofname} --numMotes {motenumber}"


quell_results_dict = dict()
of0_results_dict = dict()

quell_mean_of_p_c = dict()
of0_mean_of_p_c = dict()


fscore_quell = dict()
fscore_of0 = dict()

random.seed(time.time())

for mote_number in mote_count:
    for i in range(1, args.simNum + 1):
        #for quell
        time.sleep(random.choice([0.1, 0.5, 1, 0.05]))
        command = "c:\python27\python.exe runSimOneCPU.py --gui --numRuns 1 --numCyclesPerRun 100 --squareSide 1 --pkPeriod 0.01 --pkPeriodVar 0.01 --slotframeLength 23 --slotDuration 0.005 --objective_function {0} --simDataDir {1} --numMotes {2}".format('quell', 'quell', str(mote_number))
        print(command)
        return_code = run(command, shell=True, stdout=subprocess.PIPE, timeout=400)
        result = return_code.stdout.decode()
        print('simulating with {0}, sim number is: {1}, mote num is: {2}'.format('quell', i, mote_number))
        print(result)
        total = int(result.split('\n')[6].split(' ')[2])
        quell_c_prime = result.split('\n')[2].split(' ')[-1][0:-1]
        quell_p_prime = result.split('\n')[3].split(' ')[-1][0:-1]
        quell_results_dict[i] = {
            'p_prime': round(int(quell_p_prime)/total, 6),
            'c_prime': round(int(quell_c_prime)/total, 6)
        }

        #for of0
        time.sleep(random.choice([0.1, 0.5, 1, 0.05]))
        command = "c:\python27\python.exe runSimOneCPU.py --gui --numRuns 1 --numCyclesPerRun 100 --squareSide 1 --pkPeriod 0.01 --pkPeriodVar 0.01 --slotframeLength 23 --slotDuration 0.005 --objective_function {0} --simDataDir {1} --numMotes {2}".format('OF0', 'OF0', str(mote_number))
        print(command)
        return_code = run(command, shell=True, stdout=subprocess.PIPE, timeout=400)
        result = return_code.stdout.decode()
        print('simulating with {0}, sim number is: {1}, mote num is: {2}'.format('OF0', i, mote_number))
        print(result)
        of0_c_prime = result.split('\n')[2].split(' ')[-1][0:-1]
        of0_p_prime = result.split('\n')[3].split(' ')[-1][0:-1]
        total = int(result.split('\n')[6].split(' ')[2])
        of0_results_dict[i] = {
            'p_prime': round(int(of0_p_prime)/total, 6),
            'c_prime': round(int(of0_c_prime)/total, 6)
        }



    p_temp_sum = 0
    p_temp_mean = 0
    c_temp_sum = 0
    c_temp_mean = 0
    for key in quell_results_dict.keys():
        p_temp_sum += quell_results_dict[key]['p_prime']
        c_temp_sum += quell_results_dict[key]['c_prime']
    p_temp_mean = round(p_temp_sum / args.simNum, 6)
    c_temp_mean = round(c_temp_sum / args.simNum, 6)
    quell_mean_of_p_c[mote_number] = {
        'p_prime': p_temp_mean,
        'c_prime': c_temp_mean
    }
    print('********* for quell *********')
    print(quell_mean_of_p_c)
    quell_results_dict = dict()

    p_temp_sum = 0
    p_temp_mean = 0
    c_temp_sum = 0
    c_temp_mean = 0
    for key in of0_results_dict.keys():
        p_temp_sum += of0_results_dict[key]['p_prime']
        c_temp_sum += of0_results_dict[key]['c_prime']
    p_temp_mean = round(p_temp_sum / args.simNum, 6)
    c_temp_mean = round(c_temp_sum / args.simNum, 6)
    of0_mean_of_p_c[mote_number] = {
        'p_prime': p_temp_mean,
        'c_prime': c_temp_mean
    }
    print('********* for OF0 *********')
    print(of0_mean_of_p_c)
    of0_results_dict = dict()

    fscore_of0[mote_number] = round((2 * (of0_mean_of_p_c[mote_number]['p_prime'] * of0_mean_of_p_c[mote_number]['c_prime'])) / (of0_mean_of_p_c[mote_number]['p_prime'] + of0_mean_of_p_c[mote_number]['c_prime']), 6)
    fscore_quell[mote_number] = round((2 * (quell_mean_of_p_c[mote_number]['p_prime'] * quell_mean_of_p_c[mote_number]['c_prime'])) / (quell_mean_of_p_c[mote_number]['p_prime'] + quell_mean_of_p_c[mote_number]['c_prime']), 6)



print('++++++++++++++++++++++++++ final fscores ++++++++++++++++++++++++++++')
print('quell:')
print(fscore_quell)
print('OF0:')
print(fscore_of0)

with open('f1_scores_quell.json', 'w') as f1_scores_quell:
    json.dump(fscore_quell, f1_scores_quell)

with open('f1_scores_of0.json', 'w') as f1_scores_of0:
    json.dump(fscore_of0, f1_scores_of0)