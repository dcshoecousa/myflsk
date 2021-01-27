"""
author: gd199
date: 2021-01-11

"""

from flask import signals

# 内置信号
# def test(*args, **kwargs):
#     print("Test")
#
# signals.request_started.connect(test)

def audit_save(*args, **kwargs):
    print("Test")





audit_logging = signals._signals.signal("audit_logging")


def audit_log(*args, **kwargs):
    print("Customer signal 1")


audit_logging.connect(audit_log)
