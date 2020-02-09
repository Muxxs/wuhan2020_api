#coding=utf-8
from flask import Blueprint, jsonify, request
from model.type import FailResp, SuccessResp
from db.select import select

read = Blueprint('read', __name__)

@read.route("/api/read", methods=['GET'])
def index():
    city = request.args.get('city')
    if city == "":
        return jsonify(FailResp())
    data = select(city)
    return jsonify(SuccessResp(data))


