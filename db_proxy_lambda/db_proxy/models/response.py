from models.data_model import DataModel

class DbProxyBaseResponse(DataModel):

    def __init__(self, status, message=""):
        self.status = status
        self.message = message

    @property
    def data(self):
        return {
            'status': self.status,
            'msg': self.message
        }

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class DbProxySelectResponse(DataModel):
    def __init__(self, status, object_name, message=""):
        self.status = status
        self.message = message
        self.object_name = object_name

    @property
    def data(self):
        return {
            'status': self.status,
            'object_name': self.object_name,
            'msg': self.message
        }

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

        