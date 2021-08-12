# Python flask application to serve the webapp.

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import logging as logger
import os
import platform

application = Flask(__name__)
application.config['SECRET_KEY'] = 'supersecretkey'

@application.route('/')
def index():
    details = {
        "machine": platform.machine(),
        "platform": platform.platform(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "release": platform.release(),
        "system": platform.system(),
        "version": platform.version()
    }
    return render_template('index.html', details=details)

port = os.getenv('VCAP_APP_PORT', '8080')
if __name__ == "__main__":
    logger.debug("Starting the Application")
    application.secret_key = os.urandom(12)
    application.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)