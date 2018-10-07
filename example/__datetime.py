# -*- coding: utf-8 -*-
import datetime

# 字符串转时间
dt = datetime.datetime.strptime('2014-11-02 13:36', '%Y-%m-%d %H:%M')
print(type(dt), dt)

# 时间转时间戳（秒级）
t = dt.timestamp()
# <class 'float'> 1414906560.0
print(type(t), t)


def strptime(str, format='%Y-%m-%d %H:%M'):
    """
    时间字符串转换

    :param str:
    :param format:
    :return:
    """
    dt = datetime.datetime.strptime('2014-11-02 13:36', '%Y-%m-%d %H:%M')
    if dt:
        return {
            'strptime': str,
            'timestamp': int(dt.timestamp()),
            # 'date': dt.date(),
            # 'time': dt.time(),
            'ctime': dt.ctime()
        }


# {'strptime': '2014-11-02 13:36', 'timestamp': 1414906560, 'ctime': 'Sun Nov  2 13:36:00 2014'}
print(strptime('2014-11-02 13:36'))
