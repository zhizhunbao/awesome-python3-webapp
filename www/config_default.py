#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__='Peng Wang'

configs = {
    'debug': True,
    'db': {
        'host': 'hadoop-test-01',
        'port': 3306,
        'user': 'www-data',
        'password': 'www-data',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
