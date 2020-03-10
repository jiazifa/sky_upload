# -*- coding: utf-8 -*-

from typing import Optional, Any, Dict, List, Union
import os
from uuid import uuid4
from flask import Flask, request, Blueprint, jsonify, current_app
from werkzeug import secure_filename
from werkzeug.datastructures import FileStorage, MultiDict

api = Blueprint("/", __name__)


def upload():
    files: List[FileStorage] = []
    file_dict: MultiDict = request.files
    if "files" in file_dict:
        tfs: Optional[List[FileStorage]] = file_dict.getlist("files")
        files.extend(tfs)
    elif "file" in file_dict:
        tf: Optional[FileStorage] = file_dict.get("file", None)
        files.append(tf)
    payload: List[Dict[str, str]] = []
    dest: str = current_app.config["UPLOAD_FOLDER"]
    if not os.path.exists(dest):
        os.mkdir(dest)
    for file in files:
        filename: str = secure_filename(file.filename)
        # 拓展名
        extension = filename.split(".")[-1].lower()
        # uuid
        identifier = str(uuid4()).replace("-", "")
        target_file = ".".join([identifier, extension])
        file.save(os.path.join(dest, target_file))
        url = "/".join(["/shared", target_file])
        payload.append(
            {"source": filename, "target": target_file, "target_url": url,}
        )
    return jsonify(payload)


def init_app(app: Flask):
    api.add_url_rule("/upload", view_func=upload, methods=["POST"])
    app.register_blueprint(api, url_prefix="/")
