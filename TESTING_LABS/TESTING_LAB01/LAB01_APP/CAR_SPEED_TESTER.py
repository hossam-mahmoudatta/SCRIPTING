# ==============================================
# Created By: Hossam Mahmoud
# Date: 2025-01-15
# Filename: CAR_SPEED_TESTER.py
# Description: Test script for testing the Car Speed Function
# Version: 1.0.0
# Last Modified: 2025-01-15 by Hossam
# Dependencies: requests, json
# Copyright (c) 2025 Hossam. All rights reserved.
# TODO: Add future tasks or improvements
# ==============================================

import unittest
import math

from CAR_SPEED import carSpeed

class TestCarSpeed(unittest.TestCase):
    def test_car_speed(self):
        self.assertEqual(carSpeed(-5), 'Invalid')
        self.assertEqual(carSpeed(35), 'Low')
        self.assertEqual(carSpeed(45), 'Normal')
        self.assertEqual(carSpeed(120), 'High')
        self.assertEqual(carSpeed(210), 'V.High')
        self.assertEqual(carSpeed(225), 'Invalid')


# if __name__ == '__main__':
#     unittest.main()