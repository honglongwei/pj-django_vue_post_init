#encoding: utf-8
from django.conf import settings
from apps.engine import engine
from datetime import datetime
import time


@engine.task
def execute(task):
    """
    任务执行
    """
    time.sleep(30)

    task_status = 1
    breakpoint = {
        "step_id": None,
        "node_id": None,
        "step_index": None
    }
    fail_servers = []
    success_servers = []

    return {
        "status": True if task_status == 1 else False,
        "breakpoint": breakpoint,
        "servers": {
            "success": success_servers,
            "fail": fail_servers
        }
    }

execute = execute if settings.UNITTEST else execute.delay