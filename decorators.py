# coding:UTF-8

from time import sleep
from functools import wraps
import logging

logging.basicConfig()
log = logging.getLogger("retry")


def retry():
	@wraps(f)
	def wrapped_f(*args, **kwargs):
		MAX_ATTEMPTS = 5
		for attempt in range(1, MAX
