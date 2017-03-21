import unittest
from collections import OrderedDict
import sys
import os
import datetime
import hashlib
import time
import subprocess
sys.path.insert(0, "../hw_test_common")

import argparse
import tempfile
import json

    

from test_ms_common import TestCO2, TestBuzzer, TestIlluminance, TestSPLNew, TestTH, TestHStrict, TestEEPROMPersistence, MSTesterBase, Test1Wire
from periph_common import parse_comma_separated_set, SerialDeviceHandler, SerialDriverHandler, ModbusDeviceTestLog, get_wbmqtt
import periph_common




class TestIlluminanceMSW2(TestIlluminance):
    MAX_AMBIENT = 20
    ILLUMINATED_DIFF = 6500
    ILLUMINATED_DIFF_ERR = 0.10

class TestSPLMSW(TestSPLNew):
    SOUND_CARD_VOLUME_LOUD = "74%"
    SOUND_LEVEL_LOUD_MIN = 81.1
    SOUND_LEVEL_LOUD_MAX = 85.1

    SOUND_CARD_VOLUME_QUIET = "11%"
    SOUND_LEVEL_QUIET_MAX = 46.5
    SOUND_LEVEL_QUIET_MIN = 40

    AMBIENT_MAX = 42


class TestTHMSW(TestTH):
    REFERENCE_DEVICE_ID = 'hdc1080'

class TestHStrictMSW(TestHStrict):
    REFERENCE_DEVICE_ID = 'hdc1080'


class Tester(MSTesterBase):
    MQTT_DEVICE_ID = 'wbmsw2-test'
    CONFIG_FNAME = "wbmsw2.conf"

    def init_mapping(self):
        self.mapping = OrderedDict([
                (TestSPLMSW, 2),
                (TestIlluminanceMSW2, 3),
                (TestTHMSW, 4),
                (TestHStrictMSW, 8),
                (TestCO2, 5),
                (TestBuzzer, 6),
                (TestEEPROMPersistence, 1),
        ])




if __name__ == '__main__':
    try:
        while 1:
            periph_common.get_wbmqtt().watch_device('am2320')
            Tester().main()

            while 1:
                e = raw_input("press Enter to continue or Control+C to exit")
                if e == '':
                    break

            print "\n" * 5



    finally:
        periph_common.get_wbmqtt().close()
