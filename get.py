#!/usr/bin/env python3
# Created by Constantine in 2k25
import subprocess

# Available slots you can find via command: ssacli ctrl all show
available_slots_for_getting_info = [0] # slots array

get_controller_info_description = subprocess.run(['ssacli', 'ctrl', 'all', 'show'], capture_output=True, text=True)
controller_info_description = get_controller_info_description.stdout
print ('#', controller_info_description.strip())

print ('# TYPE ssacli_physicaldrive_combined gauge')

string_1 = 'node_ssacli_physicaldrive_combined{drive="'
string_2 = '",status="'
string_3 = '",serialnumber="'
string_4 = '",bay="'
string_5 = '"} '
for slot in available_slots_for_getting_info:
    disks_status_result = subprocess.run(['ssacli', 'ctrl', 'slot='+str(slot), 'pd', 'all', 'show', 'status'], capture_output=True, text=True)
    all_disks = list(filter(None,disks_status_result.stdout.split('\n')))
    for disk in all_disks:
        diskinfo = disk.strip().split()
        get_serial_cmd = 'ssacli ctrl slot=0 pd '+diskinfo[1]+' show | grep Serial'
        get_serial_cmd_run = subprocess.Popen(get_serial_cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        serial_output = get_serial_cmd_run.communicate()[0]
        serial_number = serial_output.decode("utf-8").strip().split()[2]
        digital_status_if_ok = 1 if diskinfo[8] == 'OK' else 0
        print (string_1+diskinfo[1]+string_2+diskinfo[8]+string_3+serial_number+string_4+diskinfo[5].replace(',','')+string_5+str(digital_status_if_ok))

