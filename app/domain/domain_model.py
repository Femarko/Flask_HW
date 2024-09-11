import typing


class StorageInterface(typing.Protocol):
    def add(self, *args, **kwargs) -> int | dict:
        pass
        # raise NotImplementedError

    # def update(self):
    #     pass
    #
    # def get_sample(self):
    #     pass
    #
    # def get_all(self):
    #     pass
    #
    # def delete(self):
    #     pass


class Filter(typing.Protocol):
    def get_filter(self):
        pass


class Advertisement:
    def __init__(self, storage_repository: StorageInterface):
        self.storage_repository = storage_repository

    def add_new(self, params: dict):
        return self.storage_repository.add(params)

    def update(self):
        return self.storage_repository.update()

    def get_sample(self, filter_param):
        return self.storage_repository.get_sample()

    def get_all(self):
        return self.storage_repository.get_all()

    def delete(self):
        return self.storage_repository.delete()

