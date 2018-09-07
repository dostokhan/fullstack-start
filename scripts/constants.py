#!/usr/bin/env python

TASK_LIST = {
    'start': {
        'name': 'Start Containers',
        'action': 'up',
    },
    'stop': {
        'name': 'Stop Containers',
        'action': 'down',
    },
    'log': {
        'name': 'See Container log',
        'action': 'log',
    },
    'bash': {
        'name': 'See Container log',
        'action': 'bash',
    },
};
PROJECT_LIST = {
    'frontback': {
        'name': 'FRONTEND + BACKEND',
        'action': 'frontendbackend',
    },
    'front': {
        'name': 'FRONTEND',
        'action': 'frontend',
    },
    'back': {
        'name': 'BACKEND',
        'action': 'backend',
    }
}

