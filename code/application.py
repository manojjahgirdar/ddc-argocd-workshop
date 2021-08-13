# Python flask application to serve the webapp.

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import logging as logger
import os

application = Flask(__name__)
application.config['SECRET_KEY'] = 'supersecretkey'
storeTitle = "The Medical Store"
offerDetails = [
    "10% discount on bulk orders",
    "50% off on 3 ply masks",
    "20% off on Face Shields",
    "Free Delivery Service",
    "10% off on Hand Sanitizers",
    "5% extra discount for members"
]

@application.route('/')
def index():
    # details = {
    #     "machine": platform.machine(),
    #     "platform": platform.platform(),
    #     "processor": platform.processor(),
    #     "python_version": platform.python_version(),
    #     "release": platform.release(),
    #     "system": platform.system(),
    #     "version": platform.version()
    # }
    return render_template('index.html', storeTitle=storeTitle, offers=offerDetails)

port = os.getenv('VCAP_APP_PORT', '8080')
if __name__ == "__main__":
    logger.debug("Starting the Application")
    application.secret_key = os.urandom(12)
    application.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)