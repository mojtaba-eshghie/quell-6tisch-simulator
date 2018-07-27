#!/usr/bin/python27

import argparse
import os

parser = argparse.ArgumentParser(description='This script is for calculating latency based on any criteria that you select.')
parser.add_argument('--topdir', type=str, help='The directory that contains the toppest structure containing quell and of0 ods result file folders', default='C:\\Users\\mojtaba\\Desktop\\fresh\\anali')
args = parser.parse_args()
top_directory = args.topdir


def latency_on_load(file=None):
    with open(file, 'r') as file_object:
        # the total number of pkts which have reached the root of DODAG
        total_pkts_made = 0
        sigma = 0
        line_number = 1
        for line in file_object:
            if 35 <= line_number <= 134:
                pkts_reached = int(line.split()[3])
                row_latency = float(line.split()[7])
                if pkts_reached is not 0:
                    total_pkts_made += pkts_reached
                    # line.split()[7]
                    sigma += (pkts_reached * row_latency)
            # here is last line of for loop
            line_number += 1
        mean_latency = sigma / total_pkts_made
        return mean_latency


def queue_drop_on_load(file=None):
    # 17 dropqueuefull
    # 8 queuelatency
    with open(file, 'r') as file_object:
        # the total number of pkts which have reached the root of DODAG
        total_pkts_made = 0
        sigma = 0
        line_number = 1
        for line in file_object:
            if 35 <= line_number <= 134:
                pkts_reached = int(line.split()[3])
                row_queue_drop = float(line.split()[16])
                if pkts_reached is not 0:
                    total_pkts_made += pkts_reached
                    # line.split()[7]
                    sigma += (pkts_reached * row_latency)
            # here is last line of for loop
            line_number += 1
        mean_drop = sigma / total_pkts_made
        return mean_drop


def give_ods_files(directory=None):
    '''
    :return: A list that contains all the files in all subdirectories that are contained within an output_...._ directory
    '''
    if directory is not None:
        file_list = list()
        dir_list = os.listdir(directory)
        for dir in dir_list:
            dir = directory + '\\' + dir
            file_list.append(dir + '\\' + os.listdir(dir)[0])
        return file_list
    else:
        raise IOError('You have not supplied me with a proper directory!')


for dir in os.listdir(top_directory):
    print('doing it for: {},'.format(dir))
    final_file_list = list()
    dir = top_directory + '\\' + dir
    files = give_ods_files(directory=dir)
    for file in files:
        final_file_list.append(file)
        print('for file: {0}, it is: {1}'.format(file.__str__(), give_me(file)))