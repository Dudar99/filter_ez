"""
Module include FilterApplier class.
"""
import copy
from app.helper import DataSetPandas
from app.models import Filter


class FilterApplier:
    """
    FilterApplier class is used to apply filter to selected DataSet(File)
    """
    def __init__(self, dataset_id, filter_id):
        self.dataset_id = dataset_id
        self.filter_id = filter_id
        self.result = DataSetPandas()
        self.filters = self.get_filter()
        self.amount = self.get_amount()

    def get_amount(self):
        """Returns amount of filtering result"""
        filters = self.get_filter()
        amount = 0
        for val in filters.values():
            amount += val['params']['quantity']
        return amount

    def get_filter(self):
        """Returns params of given filter"""
        filters = Filter.query.get(self.filter_id)
        return filters.params

    def filter_apply(self):
        """
        Apply filter to DataFrame formed from given DataSet.
        Returns list of DataFrame indexes of selected rows.
        """
        data = DataSetPandas(self.dataset_id)
        data.actualize()
        self.filter_iterator(data, self.filters, self.amount)
        return self.result.content_indexes()

    def filter_iterator(self, data, filters, amount):
        """
        Filtration Iterator is used recursively to iterate over all filter tree branches.
        It applies all filters on each step before get the deepest filtration level, after
        that it makes sample from last DataFrame on branch.
        :param data: filtration level DataFrame
        :param filters: filtration level filter
        :param amount: total amount of items in result
        :return:Sample from last filtration level by applying needed amount of items
        """
        lack = amount
        for val in filters.values():
            result_df = copy.deepcopy(data)
            if val.get('child'):
                result_df.filter_set(val['params'])
                data.exclude(result_df.dataframe)
                lack -= val['params']['quantity']
                next_df = copy.deepcopy(result_df)
                self.filter_iterator(next_df, val['child'], val['params']['quantity'])
            else:
                result_df.filter_set(val['params'])
                data.exclude(result_df.dataframe)
                lack -= val['params']['quantity']
                sample = result_df.sample(val['params']['quantity'])
                self.result.append_df(sample)
        self.result.append_df(data.sample(lack))
