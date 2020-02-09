from flask import Blueprint, jsonify, request
from model.type import FailResp, SuccessResp
from db.log import seekByTime

logs = Blueprint('log', __name__)

@logs.route("/api/logs/uploader", methods=['GET'])
def uploader():
    limit = request.args.get('limit', type=int, default=10)
    return jsonify(SuccessResp(seekByTime(limit)))