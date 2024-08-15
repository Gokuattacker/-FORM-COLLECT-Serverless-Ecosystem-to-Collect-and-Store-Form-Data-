from models.data_model import DataModel

class GoogleSheetApiResponse(DataModel):

    def __init__(self, status, message="", google_sheet=""):
        self.status = status
        self.message = message
        self.google_sheet = google_sheet

    @property
    def data(self):
        return {
            'status': self.status,
            'msg': self.message,
            'spread_sheet_name': self.google_sheet
        }

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        