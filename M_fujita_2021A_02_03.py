#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# M_fujita_2021A_02_03.py
#
# Copyright (c) 2021-2023 shihashi
#
# Released under the MIT license.
# see https://opensource.org/licenses/mit-license.php
#

import itertools

item_list = ['1', '2', '11', '12']
num_repeat = 3

print(len({int(''.join(x)) for x in itertools.product(item_list, repeat = num_repeat)}))
