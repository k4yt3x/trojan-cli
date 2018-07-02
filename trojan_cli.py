#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name: Trojan CLI
Dev: K4YT3X
Date Created: July 1, 2018
Last Modified: July 1, 2018

Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: https://www.gnu.org/licenses/gpl-3.0.txt
(C) 2018 K4YT3X
"""
import avalon_framework as avalon
import json
import os
import random
import string

VERSION = '1.0'


class trojan_server:

    def __init__(self):
        if os.getuid() != 0:
            raise Exception('Insufficient privilege, user must be root.')

    def start(self):
        avalon.info('Starting trojan server')
        os.system('systemctl start trojan')

    def stop(self):
        avalon.info('Stopping trojan server')
        os.system('systemctl stop trojan')

    def restart(self):
        avalon.info('Restarting trojan server')
        os.system('systemctl restart trojan')


class trojan_config:

    def __init__(self, config_path):
        self.tserver = trojan_server()
        self.config_path = config_path
        self.read_config()

    def read_config(self):
        avalon.dbgInfo('Reading config from: {}'.format(self.config_path))
        with open(self.config_path, 'r') as conf:
            self.config = json.load(conf)
            conf.close()

    def write_config(self):
        avalon.dbgInfo('Writing config to: {}'.format(self.config_path))
        with open(self.config_path, 'w') as conf:
            json.dump(self.config, conf, indent=2)
            conf.close()

    def add_user(self, username):
        for password in self.config['password']:
            if username.lower() == password.split(':')[0].lower():
                avalon.error('Aborting: user already exist')
                return
        password = '{}:{}'.format(username, ''.join(random.choices(string.ascii_uppercase + string.digits, k=20)))
        avalon.info('Adding user with password: {}'.format(password))

        self.config['password'].append(password)
        self.write_config()
        self.tserver.restart()

    def del_user(self, username):
        found = False
        for password in self.config['password']:
            if username.lower() == password.split(':')[0].lower():
                found = True
                avalon.info('Deleting user {}'.format(username))
                self.config['password'] = [p for p in self.config['password'] if p.split(':')[0].lower() != username.lower()]
        if not found:
            avalon.warning('No matching user(s) found')
        self.write_config()
        self.tserver.restart()

    def print_help(self):
        print('adduser [username]')
        print('deluser [username]')

    def command_interpreter(self):
        while True:
            raw_input = input('>>> ')
            command = raw_input.lower().split(' ')
            if command[0] == 'help':
                self.print_help()
            elif command[0] == 'adduser':
                self.add_user(command[1])
            elif command[0] == 'deluser':
                self.del_user(command[1])
            else:
                self.print_help()


trojan_config = trojan_config('/etc/trojan.json')
trojan_config.command_interpreter()

'''
# This is deprecated
while True:
    exec(input('>>> '))
'''
