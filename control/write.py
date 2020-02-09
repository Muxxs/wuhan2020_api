#coding=utf-8
import datetime
from flask import Blueprint, request, json, jsonify
from model.type import FailResp,SuccessResp, createArchive, SubLog
from db.insert import insert
from db.log import logInsert

write = Blueprint('write', __name__)

@write.route('/api/add', methods=['POST'])
def index():
    upload = request.json
    if type(upload).__name__  != "dict":
        return jsonify(FailResp("type errors"))

    if not insert(createArchive(upload)):
        return jsonify(FailResp("existed or errors"))
    # 提交日志
    logInsert(
        subLog(
            ip = request.remote_addr,
            time = datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S"),
            uploader = upload.get("uploader", "unknown"),
            province = upload.get("province", "unknown"),
            city = upload.get("city", "unknown")
            )
        )
    return jsonify(SuccessResp(None))

