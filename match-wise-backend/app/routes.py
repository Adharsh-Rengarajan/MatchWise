from flask import Blueprint, jsonify, request

routes=Blueprint("main", __name__)

@routes.route('/',methods=["GET"])
def home():
    return "Welcome to home"
