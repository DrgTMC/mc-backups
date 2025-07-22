#!/usr/bin/python3
#DRG - april 2021
#-*- coding: utf-8 -*-

import os, json, sys, shutil
from datetime import datetime

#log date format
def log_date():
    return "[" + str(datetime.today().strftime('%H:%M:%S')) + "] - "

#load vats worldname and backups location
def load_vars():
    config_file = os.path.dirname(os.path.dirname(__file__))+"/.config/config.json"
    f = open(config_file)
    data = json.load(f)
    
    for i in data:
        worldname = i['mcworldpath']
        backuplocation = i['backup-location']
        break
    
    return worldname, backuplocation

#backups function
def do_backup(mc_world, destination):
    namedate = datetime.today().strftime('%Y%m%d%H%M%S')
    destination_filename = destination + "/" + str(namedate)

    #try doing the backup
    print(log_date() + "Starting backup")
    try: shutil.make_archive(destination_filename, 'zip', mc_world)
    except:
        print(log_date() + "Errors where found")
        return
    print(log_date() + "Backup completed")

#main
if __name__ == '__main__':
    print(log_date() + "Loading configuration")
    worldpath, backuplocation  = load_vars()

    #check if minecraft world and backup location exists
    if not os.path.exists(backuplocation) or not os.path.exists(worldpath):
        print(log_date() + "Some path doesnt exist")
        sys.exit()
    else:
        do_backup(worldpath, backuplocation)
