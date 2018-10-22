"""Module including Dataset Class"""
import pickle

from app.helper import UserFilesManager
from app.models import Dataset


class DatasetManager:
    def __init__(self, dataset_id):
        self.dataset = self.get_dataset(dataset_id)

    @staticmethod
    def get_dataset(dataset_id):
        return Dataset.query.get(dataset_id)

    def is_dataset(self):
        return self.dataset.filter_id

    def is_owner(self, user_id):
        return self.dataset.user_id == user_id

    def read(self):
        file = UserFilesManager(self.dataset.user_id)
        with open(file.get_serialized_file_path(self.dataset.file_id), 'rb') as source:
            data = pickle.load(source)
        if self.dataset.included_rows:
            dataset = data.iloc[self.dataset.included_rows]
            return dataset
        return data

    def apply_filter(self):
        pass

    def delete(self):
        pass

    def append(self, indexes):
        return self.dataset.included_rows.append(indexes)

    def remove(self, indexes):
        return [
            self.dataset.included_rows.remove(idx)
            for idx in indexes
            if idx in self.dataset.included_rows
        ]
