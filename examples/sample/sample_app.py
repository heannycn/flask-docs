#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Program:
    Sample app
Version:
    0.3.2
History:
    Created on 2018/05/20
    Last modified on 2021/08/17
Author:
    kwkw
"""

from flask import Blueprint, Flask, jsonify, render_template

from flask_docs import ApiDoc

app = Flask(__name__)

# Using CDN
# app.config["API_DOC_CDN"] = True

# Disable document pages
# app.config["API_DOC_ENABLE"] = False

# Methods allowed to be displayed
# app.config["API_DOC_METHODS_LIST"] = ["GET", "POST", "PUT", "DELETE", "PATCH"]

# Custom url_prefix
app.config["API_DOC_URL_PREFIX"] = "/docs"

# 显示根目录下的html路径分类
app.config["API_DOC_TEMP"] = True

# 使用自定义名
# app.config["API_DOC_MEMBER_NAME"] = True
# app.config["API_DOC_MEMBER"] = {"api": "API接口", "platform": "platform 接口"}

# Api Document needs to be displayed
app.config["API_DOC_MEMBER"] = ["api", "platform"]

ApiDoc(
    app,
    title="Sample App",
    version="1.0.0",
    description="A simple app API",
)

api = Blueprint("api", __name__)
platform = Blueprint("platform", __name__)


@app.route('/index.html')
def index_html():
    return render_template('index.html')

@app.route('/demo.html')
def demo_html():
    return render_template('demo.html')


@api.route("/add_data", methods=["POST"])
def add_data():
    """Add some data

    @@@
    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    | title |  false   |    body      | str  | blog title    |
    | name  |  false   |    body      | str  | person's name |

    ### request
    ```json
    {"title": "xxx", "name": "xxx"}
    ```

    ### return
    ```json
    {"code": xxxx, "msg": "xxx", "data": null}
    ```
    @@@
    """
    return jsonify({"api": "add data"})


@api.route("/delete_data", methods=["GET"])
def delete_data():
    """Delete some data

    @@@
    ### args
    |  args  | nullable | request type | type |  remarks     |
    |--------|----------|--------------|------|--------------|
    |  id    |  true    |    query     |  str | blog id    |
    |  name  |  false   |    query     |  str | person's name |

    ### request
    ```
    http://127.0.0.1:5000/api/delete_data?name=xxx
    ```

    ### return
    ```json
    {"code": xxxx, "msg": "xxx", "data": null}
    ```
    @@@
    """

    return jsonify({"api": "delete data"})


@platform.route("/get_something", methods=["GET"])
def get_something():
    """Get some data

    @@@
    ### request example
    ```python
    import requests
    url="http://127.0.0.1:5000/platform/get_something"
    try:
        print(requests.get(url).text)
    except:
        pass
    ```

    ### return
    ```json
    {"code": xxxx, "msg": "xxx", "data": null}
    ```
    @@@
    """

    return jsonify({"platform": "get something"})


app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(platform, url_prefix="/platform")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
