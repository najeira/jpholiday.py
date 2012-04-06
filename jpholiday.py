# -*- coding: utf-8 -*-

"""
jpholyday.py
============

:copyright: 2012 by najeira <najeira@gmail.com>.
:license: Apache License 2.0, see LICENSE for more details.

see: http://ja.wikipedia.org/wiki/%E5%9B%BD%E6%B0%91%E3%81%AE%E7%A5%9D%E6%97%A5
"""

import sys
import math
import datetime


def get(day):
  y = day.year
  m = day.month
  d = day.day
  w = day.weekday()
  name = _get(y, m, d, w)
  
  #振替休日
  if not name:
    if 1973 <= y and w == 0:
      yesterday = day - datetime.timedelta(days=1)
      yname = _get(yesterday.year, yesterday.month, yesterday.day, yesterday.weekday())
      if yname:
        name = '振替休日'
    elif m == 5 and d == 6 and 2007 <= y and w in (1, 2):
      #祝日が連続する場合に月曜日以外で振替休日となる可能性がある
      name = '振替休日'
  
  if name and sys.version_info[0] < 3:
    name = unicode(name, 'utf-8')
  return name


def _get(y, m, d, w):
  
  #皇室慶弔行事に伴う休日
  if y == 1959 and m == 4 and d == 10:
    return '皇太子・明仁親王の結婚の儀'
  elif y == 1989 and m == 2 and d == 24:
    return '昭和天皇の大喪の礼'
  elif y == 1990 and m == 11 and d == 12:
    return '即位の礼正殿の儀'
  elif y == 1993 and m == 6 and d == 9:
    return '皇太子・徳仁親王の結婚の儀'
  
  #国民の祝日
  if m == 1:
    if d == 1:
      return '元日'
    else:
      if 1949 <= y <= 1999:
        if d == 15:
          return '成人の日'
      elif 2000 <= y:
        if 8 <= d <= 14 and w == 0:
          return '成人の日'
    
  elif m == 2:
    if 1967 <= y:
      if d == 11:
        return '建国記念の日'
    
  elif m == 3:
    if 19 <= d <= 22:
      if d == get_shun_bun(y):
        return '春分の日'
    
  elif m == 4:
    if d == 29:
      if y <= 1988:
        return '天皇誕生日'
      elif y <= 2006:
        return 'みどりの日'
      else:
        return '昭和の日'
    
  elif m == 5:
    if d == 3:
      return '憲法記念日'
    elif d == 4:
      if 1988 <= y <= 2006 and w in (1, 2, 3, 4, 5):
        return '国民の休日'
      elif 2007 <= y:
        return 'みどりの日'
    elif d == 5:
      return 'こどもの日'
    
  elif m == 7:
    if 1996 <= y <= 2002:
      if d == 20:
        return '海の日'
    elif 2003 <= y:
      if 15 <= d <= 21 and w == 0:
        return '海の日'
    
  elif m == 9:
    if 1966 <= y <= 2002:
      if d == 15:
        return '敬老の日'
    elif 2003 <= y:
      if 15 <= d <= 21 and w == 0:
        return '敬老の日'
    
    if 2009 <= y and w == 1:
      if 22 <= (d + 1) <= 24:
        if (d + 1) == get_shuu_bun(y):
          return '国民の休日'
    
    if 22 <= d <= 24:
      if d == get_shuu_bun(y):
        return '秋分の日'
    
  elif m == 10:
    if 1966 <= y <= 1999:
      if d == 10:
        return '体育の日'
    elif 2000 <= y:
      if 8 <= d <= 14 and w == 0:
        return '体育の日'
    
  elif m == 11:
    if d == 3:
      return '文化の日'
    elif d == 23:
      return '勤労感謝の日'
    
  elif m == 12:
    if 1989 <= y:
      if d == 23:
        return '天皇誕生日'
  
  return None


def get_shun_bun(y):
  add = 0.242194 * (y - 1980) - math.floor((y - 1980) / 4)
  if 1980 <= y:
    if 2100 <= y <= 2150:
      return math.floor(21.8510 + add)
    else:
      return math.floor(20.8431 + add)
  elif 1851 <= y:
    if 1900 <= y:
      return math.floor(20.8357 + add)
    else:
      return math.floor(19.8277 + add)
  return 0


def get_shuu_bun(y):
  add = 0.242194 * (y - 1980) - math.floor((y - 1980) / 4)
  if 1980 <= y:
    if 2100 <= y <= 2150:
      return math.floor(24.2488 + add)
    else:
      return math.floor(23.2488 + add)
  elif 1851 <= y:
    if 1900 <= y:
      return math.floor(23.2588 + add)
    else:
      return math.floor(22.2588 + add)
  return 0
