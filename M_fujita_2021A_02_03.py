#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# M_fujita_2021A_02_03.py
#
# Copyright (c) 2021 shihashi
#
# Released under the MIT license.
# see https://opensource.org/licenses/mit-license.php
#

import itertools

itemList = ['1', '2', '11', '12']
numRepeat = 3


def main():
    print(len({int(''.join(x)) for x in itertools.product(itemList, repeat = numRepeat)}))


if __name__ == '__main__':
    main()
