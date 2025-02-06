# ==============================================
# Created By: Hossam Mahmoud
# Date: 2025-01-15
# Filename: CAR_SPEED.py
# Description: Brief description of what the file does
# Version: 1.0.0
# Last Modified: 2025-01-15 by Hossam
# Dependencies: requests, json
# Copyright (c) 2025 Hossam. All rights reserved.
# TODO: Add future tasks or improvements
# ==============================================

def carSpeed(speed):
    if speed < 0:
        return 'Invalid'
    elif speed >= 0 and speed < 40:
        return 'Low'
    elif speed >= 40 and speed < 120:
        return 'Normal'
    elif speed >= 120 and speed < 200:
        return 'High'
    elif speed >= 200 and speed < 220:
        return 'V.High'
    elif speed > 220:
        return 'Invalid'

# if __name__ == "__main__" :
#     import doctest 
#     doctest.testmod(verbose=True)