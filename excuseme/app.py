from excuseme import app, controller

app.register_blueprint(controller.api, url_prefix='/v1')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
