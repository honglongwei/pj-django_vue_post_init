#encoding: utf-8
import simplejson as json
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
import uuid

class ClientTest(Client):
    """
    Http客户端实现 用于单元测试
    """
    def _parse_json(self, response, **extra):
        """
        django自带的有问题,重写之
        """
        if "application/json" not in response.get("Content-Type"):
            raise ValueError(
                """Content-Type header is "{0}", not "application/json" """
                .format(response.get("Content-Type"))
            )
        return json.loads(response.content.decode(encoding = "utf-8"), **extra)
    

class BaseTestCase(TestCase):
    """
    单元测试基类
    """
    pass