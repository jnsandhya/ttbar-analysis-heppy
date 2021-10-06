import subprocess
import time
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('directory', help='display your directory')


args = parser.parse_args()
directory = args.directory


if directory[-1] != '/':
    directory += '/'

def sleep_minutes(minutes):
    time.sleep(minutes * 60)


script = 'check_job.py'

for i in range(20):
    p = subprocess.Popen(['python', script, directory], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    sleep_minutes(1)
    out, err = p.communicate('y')
    print 'From other process: ' + out
    sleep_minutes(10)
