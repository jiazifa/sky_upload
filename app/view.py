# -*- coding: utf-8 -*-

from typing import Optional, Any, Dict, List, Union
import os
from uuid import uuid4
from flask import request, Blueprint, jsonify, current_app
from werkzeug import secure_filename
from werkzeug.datastructures import FileStorage

api = Blueprint("/", __name__)

@api.route("/", methods=["POST"])
def upload():
    files: List[FileStorage] = []
    tf: Optional[FileStorage] = request.files["file"]
    tfs: Optional[List[FileStorage]] = request.files.getlist("files")
    payload :List[Dict[str, str]] = []
    if tf:
        # 单个文件
        files.append(tf)
    if tfs:
        files.extend(tfs)
    
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
        payload.append({
            "source": filename,
            "target": target_file,
            "target_url": url,
        })
    return jsonify(payload)