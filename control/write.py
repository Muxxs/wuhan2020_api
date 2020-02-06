#coding=utf-8
from flask import Blueprint,request

write = Blueprint('write', __name__)

@write.route('/api/write', methods=['POST'])
def index():
    return 'write'