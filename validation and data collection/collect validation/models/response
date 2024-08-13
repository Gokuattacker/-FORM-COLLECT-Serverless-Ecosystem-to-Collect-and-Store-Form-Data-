from models.data_model import DataModel

class ValidationApiResponse(DataModel):

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
        