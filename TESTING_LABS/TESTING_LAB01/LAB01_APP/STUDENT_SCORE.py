# ==============================================
# Created By: Hossam Mahmoud
# Date: 2025-01-15
# Filename: STUDENT_SCORE.py
# Description: Brief description of what the file does
# Version: 1.0.0
# Last Modified: 2025-01-15 by Hossam
# Dependencies: requests, json
# Copyright (c) 2025 Hossam. All rights reserved.
# TODO: Add future tasks or improvements
# ==============================================

def studentScore(grades):
    if grades < 0:
        return 'Invalid'
    elif grades >= 0 and grades < 50:
        return 'Failed'
    elif grades >= 50 and grades < 65:
        return 'Passed'
    elif grades >= 65 and grades < 75:
        return 'Good'
    elif grades >= 75 and grades < 85:
        return 'V.Good'
    elif grades >= 85 and grades < 100:
        return 'Excellent'
    elif grades > 100:
        return 'Invalid'

# if __name__ == "__main__" :
#     import doctest 
#     doctest.testmod(verbose=True)