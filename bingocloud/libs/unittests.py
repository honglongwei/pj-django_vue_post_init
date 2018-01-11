#encoding: utf-8
from django.http import HttpResponse
import simplejson
import random

def Ujsonify(*args, **kwargs):
    """
    通用返回json
    """
    return HttpResponse(
        simplejson.dumps(dict(*args, **kwargs), ensure_ascii = False),
        content_type = "application/json;charset = utf-8"
    )

