# -*- coding: utf-8 -*-

"""
Author: zhanxin
Email: horacesunhe@gmail.com
date: 2019/9/13 15:32
"""


from utilities.url_utilities import load_urls_from_file


def test_load_file():
    test_urls = load_urls_from_file("input.txt")
    assert(len(test_urls) > 1)
