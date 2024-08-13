from models.data_model import DataModel
from models.form_response_enum import FormCommonEnum


class FormCommonModel(DataModel):
    def __init__(self, response_id, response_family_id, user_id, username, location ,submitted_time, synced_time, last_modified_time):
        self.response_id = response_id
        self.response_family_id = response_family_id
        self.user_id = user_id
        self.username = username
        self.location = location
        self.submitted_time = submitted_time
        self.synced_time = synced_time
        self.last_modified_time = last_modified_time
    
    @property
    def data(self):
          return {
            FormCommonEnum.RESPONSE_ID.value: self.response_id,
            FormCommonEnum.RESPONSE_FAMILY_ID.value: self.response_family_id,
            FormCommonEnum.USER_ID.value: self.user_id,
            FormCommonEnum.USERNAME.value: self.username,
            FormCommonEnum.LOCATION.value: self.location,
            FormCommonEnum.SUBMITTED_TIME.value: self.submitted_time,
            FormCommonEnum.SYNCED_TIME.value: self.synced_time,
            FormCommonEnum.LAST_MODIFIED_TIME.value: self.last_modified_time
        }
        