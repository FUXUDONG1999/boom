import os
import sys

from loguru import logger

# 终端日志输出格式
stdout_fmt = '{level.icon}  <cyan>{time:HH:mm:ss,SSS}</cyan> ' \
             '[<level>{level}</level>] ' \
             '<cyan>{thread.name}</cyan> ' \
             '<blue>{module}</blue>:<cyan>{line}</cyan> - ' \
             '<level>{message}</level>'

logfile_fmt = '<light-green>{time:YYYY-MM-DD HH:mm:ss,SSS}</light-green> ' \
              '[<level>{level}</level>] ' \
              '<blue>{module}</blue>.<blue>{function}</blue>:' \
              '<blue>{line}</blue> - <level>{message}</level>'

logger.remove()

if not os.environ.get('PYTHONIOENCODING'):  # 设置编码
    os.environ['PYTHONIOENCODING'] = 'utf-8'

logger.add(sys.stderr, level='INFO', format=stdout_fmt, enqueue=True)
