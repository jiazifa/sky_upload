import os
import logging


root_dir = os.path.abspath((os.path.dirname(__file__)))


class Config:
    # 开启跨站请求伪造防护
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)

    """配置上传文件相关"""

    UPLOAD_FOLDER = os.environ.get("UPLOAD_DEST") or os.path.abspath(
        os.path.join(os.getcwd(), "disk")
    )
    ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif"])

    """Flask Uploads 配置"""
    UPLOADED_PHOTOS_DEST = UPLOAD_FOLDER
    UPLOADS_DEFAULT_DEST = UPLOAD_FOLDER
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024

    """ Logging 设置 """
    LOGGING_FORMATTER = "%(levelname)s - %(asctime)s - process: %(process)d - %(filename)s - %(name)s - %(lineno)d - %(module)s - %(message)s"  # 每条日志输出格式
    LOGGING_DATE_FORMATTER = "%a %d %b %Y %H:%M:%S"
    LOGGING_DIR = os.path.join(root_dir, "logs")
    LOG_LEVEL = "DEBUG"  # 日志输出等级
    LOG_ENABLE = True  # 是否开启日志

    @classmethod
    def init_app(app, *args, **kwargs):
        pass
