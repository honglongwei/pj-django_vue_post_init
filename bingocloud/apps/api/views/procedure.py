#encoding: utf-8
from libs.common import jsonify, json, humanReadableDate, dcompress
from apps.engine.tasks import execute
#from apps.task.services import  do_createTask

def run(request):
    """
    流程执行
    """
    # project_id = request.formdata.get("project_id")
#    task = do_createTask()
#    ret = execute(task = task)
    data = [
            {"host": "8.8.8.8", "os": u'Linux' , "owner": u"张三", "desc": u"我是张三"},
            {"host": "9.9.9.9", "os": u'Windows' , "owner": u"李四", "desc": u"我是李四"},
            {"host": "7.7.7.7", "os": u'Windows' , "owner": u"王五", "desc": u"我是王五"}
    ]

    return jsonify(test = {"code": 4}, success = True, data = data)

