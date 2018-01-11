#encoding: utf-8

from django.conf import settings
from django.core.exceptions import FieldError
from django.http import HttpResponse
from libs import unittests
import simplejson as json
import zlib

def jsonify(*args, **kwargs):
    """
    通用返回json
    """
    if kwargs.has_key("test"):
        del kwargs["test"]

    return HttpResponse(
        json.dumps(dict(*args, **kwargs), ensure_ascii = False),
        content_type = "application/json;charset = utf-8"
    )

def compress(str):
    """
    字符串压缩
    """
    str = str.strip()

    if str:
        if isinstance(str, unicode):
            return zlib.compress(str.encode("utf-8"), 9)
    
        return zlib.compress(str, 9)

    return ""

def dcompress(zstr):
    """
    字符串解压缩
    """
    if zstr:
        try:
            return zlib.decompress(zstr).strip()
        except Exception:
            return ""

    return ""

def isCharset(str, charset = "utf-8"):
    """
    判断字符编码
    """
    return True

def humanReadableDate(datetime):
    """
    通用日期格式化
    """
    if not datetime:
        return ""
        
    format = "%Y-%m-%d %H:%M:%S"
    return datetime.strftime(format)

jsonify = unittests.Ujsonify if settings.UNITTEST else jsonify
