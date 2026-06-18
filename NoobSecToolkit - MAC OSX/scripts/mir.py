#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

url = input("What Service do you want to Mirror?: ").strip()
os.system("wget -m " + url)
