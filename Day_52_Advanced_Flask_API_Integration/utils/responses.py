from flask import jsonify  # pyright: ignore[reportMissingImports]


def success_response(message, data=None, status_code=200):
    return jsonify({
        "success": True,
        "message": message,
        "data": data
    }), status_code


def error_response(message, status_code):
    return jsonify({
        "success": False,
        "error": message
    }), status_code