from flask import Blueprint, jsonify
from flask.templating import render_template
from flask_babel import gettext as _

root_view = Blueprint('root', __name__)


@root_view.route('/health', methods=('GET',))
def health_get():
    data = {'message': _('Health is OK')}
    return jsonify(data)


@root_view.route('/admin/', methods=('GET',))
def admin_get_index():
    return render_template('/admin/index.html')


@root_view.route('/admin/<path:url_path>', methods=('GET',))
def admin_get(url_path):
    return render_template('/admin/' + url_path)
