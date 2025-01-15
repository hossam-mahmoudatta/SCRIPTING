# ==============================================
# Created By: Hossam Mahmoud
# Date: 2025-01-15
# Filename: STUDENT_SCORE_TESTER.py
# Description: Brief description of what the file does
# Version: 1.0.0
# Last Modified: 2025-01-15 by Hossam
# Dependencies: requests, json
# Copyright (c) 2025 Hossam. All rights reserved.
# TODO: Add future tasks or improvements
# ==============================================

import unittest
import math

from STUDENT_SCORE import studentScore

class TestStudentScore(unittest.TestCase):
    def test_student_score(self):
        self.assertEqual(studentScore(-5), 'Invalid')
        self.assertEqual(studentScore(35), 'Failed')
        self.assertEqual(studentScore(60), 'Passed')
        self.assertEqual(studentScore(70), 'Good')
        self.assertEqual(studentScore(80), 'V.Good')
        self.assertEqual(studentScore(90), 'Excellent')
        self.assertEqual(studentScore(110), 'Invalid')


# if __name__ == '__main__':
#     unittest.main()