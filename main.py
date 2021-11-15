#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import importlib

from TK_1 import input_data_from_console
from TK_2 import get_min_max_from_list
from TK_3 import get_divided_list
from TK_4 import get_multiplied_list
TK_5 = importlib.import_module('TK_5')


def main():
    count_elements = int(input('Get number of elements: '))
    list_data = input_data_from_console(count_elements)
    print(get_min_max_from_list(list_data))
    print(get_divided_list(list_data))
    print(get_multiplied_list(list_data))
    print(TK_5.get_squared_list(list_data))
    return 0


if __name__ == '__main__':
        sys.exit(main())