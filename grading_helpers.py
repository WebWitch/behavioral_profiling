#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:14:51 2019

@author: ashraf
"""
# used to access data from csv file
field_names = ['index', 'time_stamp', 'total_trips_time', 'time_during_lap', 'time_interval', 'throttle', 'rpm',
               'speed', 'acceleration', 'jerk', 'latitude', 'longitude', 'total_trips_distance', 'distance_interval',
               'grading_distance', 'distance_in_lap']

# to provide a number to each segment with a value indicating straight segment or any particular special segment
segment_type = {
    0: 'start',
    1: 'straight',
    2: 'stop',
    3: 'straight',
    4: 'signal',
    5: 'straight',
    6: 'stop',
    7: 'straight',
    8: 'signal',
    9: 'straight',
    10: 'turn',
    11: 'straight',
    12: 'turn',
    13: 'straight',
    14: 'stop',
    15: 'straight',
    16: 'signal',
    17: 'straight',
    18: 'signal',
    19: 'straight',
    20: 'signal',
    21: 'straight',
    22: 'signal',
    23: 'straight',
    24: 'signal',
    25: 'signal',
    26: 'straight',
    27: 'roundabout',
    28: 'straight',
    29: 'roundabout',
    30: 'straight',
    31: 'roundabout',
    32: 'straight',
    33: 'turn',
    34: 'straight',
    35: 'end'
}

# sets the distance limits in meters for a segment of the road
segment_limits = [
    (0.0, 20.0),  # 0 start
    (20.0, 70.0),  # 1 straight to airport rd. stop
    (70.0, 150.0),  # 2 airport rd stop sign
    (150.0, 1800.0),  # 3 airport rd
    (1800.0, 2200.0),  # 4 airport rd. signal
    (2200.0, 4200.0),  # 5 highway
    (4200.0, 4375.0),  # 6 highway end stop-sign left
    (4375.0, 4500.0),  # 7 straight on bridge
    (4500.0, 4670.0),  # 8 signal on bridge
    (4670.0, 4700.0),  # 9 straight to issac newton drive
    (4700.0, 4820.0),  # 10 issac newton drive free right
    (4820.0, 4880.0),  # 11 straight
    (4880.0, 4950.0),  # 12 2nd free right on issac newton drive
    (4950.0, 4980.0),  # 13 straight
    (4980.0, 5100.0),  # 14 stop sign right to S 16th
    (5100.0, 5150.0),  # 15 straight
    (5150.0, 5400.0),  # 16 signal A7
    (5400.0, 7000.0),  # 17 straight A7 2
    (7000.0, 7250.0),  # 18 signal A7 2 # near old chicago
    (7250.0, 9100.0),  # 19 straight A7 3 - A7 4
    (9100.0, 9350.0),  # 20 signal left Jacktrice /S7
    (9350.0, 9700.0),  # 21 straight A8 1
    (9700.0, 9950.0),  # 22 signal A8 1
    (9950.0, 10200.0),  # 23 straight A8 1
    (10200.0, 10430.0),  # 24 signal A8 1. the leaving zone of this signal becomes the approaching zone for next signal
    (10430.0, 10600.0),  # 25 signal A8 1
    (10600.0, 10950.0),  # 26 straight A8 2
    (10950.0, 11075.0),  # 27 roundabout
    (11075.0, 11375.0),  # 28 straight
    (11375.0, 11510.0),  # 29 roundabout
    (11510.0, 11830.0),  # 30 straight
    (11830.0, 11960.0),  # 31 roundabout
    (11960.0, 12020.0),  # 32 straight
    (12020.0, 12100.0),  # 33 right turn to S loop drive
    (12100.0, 12650.0),  # 34 straight
    (12650.0, 12750.0)  # 35 ending stop sign
]

# straight segments are sub divided in to different zones according to speed limits
# special segments are always sub divided in to 3 or 4 zones
zone_limits = [
    [(0.0, 20.0)],
    [(20.0, 70.0)],
    [(70.0, 90.0), (90.0, 105.0), (105.0, 130.0), (130.0, 150.0)],
    [(150.0, 1800.0)],
    [(1800.0, 2015.0), (2015.0, 2085.0), (2085.0, 2200.0)],
    [(2200.0, 4200.0)],
    [(4200.0, 4290.0), (4290.0, 4315.0), (4315.0, 4340.0), (4340.0, 4375.0)],
    [(4375.0, 4500.0)],
    [(4500.0, 4605.0), (4605.0, 4640.0), (4640.0, 4670.0)],
    [(4670.0, 4700.0)],
    [(4700.0, 4760.0), (4760.0, 4805.0), (4805.0, 4820.0)],
    [(4820.0, 4880.0)],
    [(4880.0, 4915.0), (4915.0, 4930.0), (4930.0, 4950.0)],
    [(4950.0, 4980.0)],
    [(4980.0, 5030.0), (5030.0, 5055.0), (5055.0, 5080.0), (5080.0, 5100.0)],
    [(5100.0, 5150.0)],
    [(5150.0, 5230.0), (5230.0, 5290.0), (5290.0, 5400.0)],
    [(5400.0, 7000.0)],
    [(7000.0, 7130.0), (7130.0, 7170.0), (7170.0, 7250.0)],
    [(7250.0, 9100.0)],
    [(9100.0, 9210.0,), (9210.0, 9250.0), (9250.0, 9350.0)],
    [(9350.0, 9700.0)],
    [(9700.0, 9815.0), (9815.0, 9860.0), (9860.0, 9950.0)],
    [(9950.0, 10200.0)],
    [(10200.0, 10350.0), (10350.0, 10380.0), (10380.0, 10430.0)],
    [(10430.0, 10510.0), (10510.0, 10550.0), (10550.0, 10600.0)],
    [(10600.0, 10950.0)],
    [(10950.0, 11010.0), (11010.0, 11050.0), (11050.0, 11075.0)],
    [(11075.0, 11375.0)],
    [(11375.0, 11430.0), (11430.0, 11480.0), (11480.0, 11510.0)],
    [(11510.0, 11830.0)],
    [(11830.0, 11890.0), (11890.0, 11925.0), (11925.0, 11960.0)],
    [(11960.0, 12020.0)],
    [(12020.0, 12050.0), (12050.0, 12070.0), (12070.0, 12100.0)],
    [(12100.0, 12650.0)],
    [(12650.0, 12750.0)]
]

"""
list of threshold coefficients
Straight segments as part of special zone are called regular
So, Regular special segments and Turns each follow slightly different regression equation for accelerations
and decelerations.
For straight segments, i.e. ones not special have a separate regression equation being followed during highways
and normal road segments
"""

# jerk threshold is constant across the entire route
JERK_THRESHOLD = 2.5

# coefficients for regular portion of special segments
REG_SPECIAL_ACCN_ALPHA = 14.477
REG_SPECIAL_ACCN_BETA = -0.034
REG_SPECIAL_DCCN_ALPHA = 13.028
REG_SPECIAL_DCCN_BETA = -0.01

# coefficients for Turns of special segments
TURN_ACCN_ALPHA = 7.7871
TURN_ACCN_BETA = -0.051
TURN_DCCN_ALPHA = 8.28
TURN_DCCN_BETA = -0.037

# coefficients for straight road segments in city
CITY_ACCN_A = 0.0012
CITY_ACCN_B = -0.248
CITY_ACCN_C = 13.117
CITY_DCCN_A = 0.0011
CITY_DCCN_B = -0.2187
CITY_DCCN_C = 13.461

# coefficients for highway segments
HIGHWAY_ACCN_A = 0.002
HIGHWAY_ACCN_B = -0.4807
HIGHWAY_ACCN_C = 29.854
HIGHWAY_DCCN_A = 0.0011
HIGHWAY_DCCN_B = -0.2187
HIGHWAY_DCCN_C = 12.461

# threshold tuple contains this format: (speed limit, accA,accB, decA, decB , jerk) for each zone
# each tuple contains different thresholds required to grade a particular zone in a segment.
# if there is only tuple, indicates that there is only zone
# each row of zone_thresholds indicates the corresponding segment number
# eg. zone_thresholds[0][0] gives the thresholds required for first zone of first segment
zone_thresholds = [
    [(32.18, TURN_ACCN_ALPHA, TURN_ACCN_BETA, TURN_DCCN_ALPHA, TURN_DCCN_BETA, JERK_THRESHOLD)],
    [(40.23, CITY_ACCN_A, CITY_ACCN_B, CITY_ACCN_C, CITY_DCCN_A, CITY_DCCN_B, CITY_DCCN_C, JERK_THRESHOLD)],
    [(40.23, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
      JERK_THRESHOLD), (40.23, TURN_ACCN_ALPHA, TURN_ACCN_BETA, TURN_DCCN_ALPHA, TURN_DCCN_BETA, JERK_THRESHOLD),
     (32.18, TURN_ACCN_ALPHA, TURN_ACCN_BETA, TURN_DCCN_ALPHA, TURN_DCCN_BETA, JERK_THRESHOLD), (
     72.41, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD)],
    [(72.41, CITY_ACCN_A, CITY_ACCN_B, CITY_ACCN_C, CITY_DCCN_A, CITY_DCCN_B, CITY_DCCN_C, JERK_THRESHOLD)],
    [(72.41, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
      JERK_THRESHOLD), (40.23, TURN_ACCN_ALPHA, TURN_ACCN_BETA, TURN_DCCN_ALPHA, TURN_DCCN_BETA, JERK_THRESHOLD), (
     56.32, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD)],
    [(105, HIGHWAY_ACCN_A, HIGHWAY_ACCN_B, HIGHWAY_ACCN_C, HIGHWAY_DCCN_A, HIGHWAY_DCCN_B, HIGHWAY_DCCN_C,
      JERK_THRESHOLD)],
    [(32.18, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
      JERK_THRESHOLD), (32.18, TURN_ACCN_ALPHA, TURN_ACCN_BETA, TURN_DCCN_ALPHA, TURN_DCCN_BETA, JERK_THRESHOLD),
     (32.18, TURN_ACCN_ALPHA, TURN_ACCN_BETA, TURN_DCCN_ALPHA, TURN_DCCN_BETA, JERK_THRESHOLD), (
     56.32, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD)],
    [(56.32, CITY_ACCN_A, CITY_ACCN_B, CITY_ACCN_C, CITY_DCCN_A, CITY_DCCN_B, CITY_DCCN_C, JERK_THRESHOLD)],
    [(56.32, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
      JERK_THRESHOLD), (
     56.32, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD), (
     40.23, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD)],
    [(40.23, CITY_ACCN_A, CITY_ACCN_B, CITY_ACCN_C, CITY_DCCN_A, CITY_DCCN_B, CITY_DCCN_C, JERK_THRESHOLD)],
    [(40.23, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
      JERK_THRESHOLD), (32.18, TURN_ACCN_ALPHA, TURN_ACCN_BETA, TURN_DCCN_ALPHA, TURN_DCCN_BETA, JERK_THRESHOLD), (
     40.23, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD)],
    [(40.23, CITY_ACCN_A, CITY_ACCN_B, CITY_ACCN_C, CITY_DCCN_A, CITY_DCCN_B, CITY_DCCN_C, JERK_THRESHOLD)],
    [(40.23, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
      JERK_THRESHOLD), (32.18, TURN_ACCN_ALPHA, TURN_ACCN_BETA, TURN_DCCN_ALPHA, TURN_DCCN_BETA, JERK_THRESHOLD), (
     40.23, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD)],
    [(40.23, CITY_ACCN_A, CITY_ACCN_B, CITY_ACCN_C, CITY_DCCN_A, CITY_DCCN_B, CITY_DCCN_C, JERK_THRESHOLD)],
    [(40.23, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
      JERK_THRESHOLD), (40.23, TURN_ACCN_ALPHA, TURN_ACCN_BETA, TURN_DCCN_ALPHA, TURN_DCCN_BETA, JERK_THRESHOLD),
     (32.18, TURN_ACCN_ALPHA, TURN_ACCN_BETA, TURN_DCCN_ALPHA, TURN_DCCN_BETA, JERK_THRESHOLD), (
     56.32, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD)],
    [(56.32, CITY_ACCN_A, CITY_ACCN_B, CITY_ACCN_C, CITY_DCCN_A, CITY_DCCN_B, CITY_DCCN_C, JERK_THRESHOLD)],
    [(56.32, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
      JERK_THRESHOLD), (
     56.32, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD), (
     56.32, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD)],
    [(56.32, CITY_ACCN_A, CITY_ACCN_B, CITY_ACCN_C, CITY_DCCN_A, CITY_DCCN_B, CITY_DCCN_C, JERK_THRESHOLD)],
    [(56.32, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
      JERK_THRESHOLD), (
     56.32, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD), (
     56.32, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD)],
    [(56.32, CITY_ACCN_A, CITY_ACCN_B, CITY_ACCN_C, CITY_DCCN_A, CITY_DCCN_B, CITY_DCCN_C, JERK_THRESHOLD)],
    [(56.32, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
      JERK_THRESHOLD), (32.18, TURN_ACCN_ALPHA, TURN_ACCN_BETA, TURN_DCCN_ALPHA, TURN_DCCN_BETA, JERK_THRESHOLD), (
     72.41, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD)],
    [(72.41, CITY_ACCN_A, CITY_ACCN_B, CITY_ACCN_C, CITY_DCCN_A, CITY_DCCN_B, CITY_DCCN_C, JERK_THRESHOLD)],
    [(72.41, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
      JERK_THRESHOLD), (
     72.41, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD), (
     72.41, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD)],
    [(72.41, CITY_ACCN_A, CITY_ACCN_B, CITY_ACCN_C, CITY_DCCN_A, CITY_DCCN_B, CITY_DCCN_C, JERK_THRESHOLD)],
    [(72.41, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
      JERK_THRESHOLD), (
     72.41, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD), (
     72.41, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD)],
    [(72.41, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
      JERK_THRESHOLD), (
     72.41, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD), (
     72.41, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD)],
    [(72.41, CITY_ACCN_A, CITY_ACCN_B, CITY_ACCN_C, CITY_DCCN_A, CITY_DCCN_B, CITY_DCCN_C, JERK_THRESHOLD)],
    [(32.18, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
      JERK_THRESHOLD), (32.18, TURN_ACCN_ALPHA, TURN_ACCN_BETA, TURN_DCCN_ALPHA, TURN_DCCN_BETA, JERK_THRESHOLD), (
     32.18, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD)],
    [(56.32, CITY_ACCN_A, CITY_ACCN_B, CITY_ACCN_C, CITY_DCCN_A, CITY_DCCN_B, CITY_DCCN_C, JERK_THRESHOLD)],
    [(32.18, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
      JERK_THRESHOLD), (32.18, TURN_ACCN_ALPHA, TURN_ACCN_BETA, TURN_DCCN_ALPHA, TURN_DCCN_BETA, JERK_THRESHOLD), (
     32.18, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD)],
    [(56.32, CITY_ACCN_A, CITY_ACCN_B, CITY_ACCN_C, CITY_DCCN_A, CITY_DCCN_B, CITY_DCCN_C, JERK_THRESHOLD)],
    [(32.18, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
      JERK_THRESHOLD), (32.18, TURN_ACCN_ALPHA, TURN_ACCN_BETA, TURN_DCCN_ALPHA, TURN_DCCN_BETA, JERK_THRESHOLD), (
     32.18, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD)],
    [(56.32, CITY_ACCN_A, CITY_ACCN_B, CITY_ACCN_C, CITY_DCCN_A, CITY_DCCN_B, CITY_DCCN_C, JERK_THRESHOLD)],
    [(56.32, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
      JERK_THRESHOLD), (32.18, TURN_ACCN_ALPHA, TURN_ACCN_BETA, TURN_DCCN_ALPHA, TURN_DCCN_BETA, JERK_THRESHOLD), (
     40.23, REG_SPECIAL_ACCN_ALPHA, REG_SPECIAL_ACCN_BETA, REG_SPECIAL_DCCN_ALPHA, REG_SPECIAL_DCCN_BETA,
     JERK_THRESHOLD)],
    [(40.23, CITY_ACCN_A, CITY_ACCN_B, CITY_ACCN_C, CITY_DCCN_A, CITY_DCCN_B, CITY_DCCN_C, JERK_THRESHOLD)],
    [(32.18, TURN_ACCN_ALPHA, TURN_ACCN_BETA, TURN_DCCN_ALPHA, TURN_DCCN_BETA, JERK_THRESHOLD)]
]
