import json
from app import app, db

from flask import session
from flask_login import login_required
from app.models import File, Dataset
from app.services.utils import user_dir, ext_free, delete_files_from_dir


@app.route('/api/delete_file/<int:file_id>')
@login_required
def delete_file(file_id):
    """
    Delete user files from DB and folder
    :param dataset_id:
    :param file_id: file id 
    :return:
    """
    user_id = session['user_id']

    dataset = Dataset.query.filter(Dataset.user_id == user_id).first()
    if not dataset:
        json.dumps({"message": 'dataset does not exist'}), 404
    file = File.query.filter(File.id == file_id).first()
    if not file:
        return json.dumps({'message': 'file does not exist'}), 404
    if not dataset.user_id:
        return json.dumps({'message': 'access forbidden'}), 403
    File.query.filter(File.id == file_id).delete()
    user_directory = user_dir(user_id)
    user_file = file.path
    delete_files_from_dir(user_directory, user_file)

    return json.dumps({'message': 'file successfully deleted'}), 200