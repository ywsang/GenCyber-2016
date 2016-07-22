# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 11:23:01 2016

@author: student
"""

import qrcode
img = qrcode.make('food tastes good')
img.show()
img.save('qrgen.png')