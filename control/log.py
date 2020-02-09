from flask import Blueprint, jsonify, request
from model.type import FailResp, SuccessResp
from db.log import seekByTime
read = Blueprint('log', __name__)

@read.route("/api/log/uploader", methods=['GET'])
def index():
    limit = request.args.get('limit', type=int, default=10)
    if limit > 99:
        limit = 99
    return jsonify(SuccessResp(seekByTime(limit)))