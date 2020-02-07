#coding=utf-8
from flask import Blueprint, jsonify
from model.type import FailResp, SuccessResp
from sql.select import select

read = Blueprint('read', __name__)

@read.route("/api/read/<city>", methods=['GET'])
def index(city=""):
    if city == "":
        return jsonify(FailResp())
    data = select(city)
    return jsonify(SuccessResp(data))


