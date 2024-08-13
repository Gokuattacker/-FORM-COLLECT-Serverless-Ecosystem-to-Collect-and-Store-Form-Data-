import json

class FormSQSModel():
    def __init__(self, form_common_model, form_specific_model, flag_list):
        self.form_common_model = form_common_model
        self.form_specific_model = form_specific_model
        self.flag_list = flag_list
    
    def get_message_body(self):
        message_body_dict = {}
        message_body_dict.update({"flag_list": self.flag_list})
        message_body_dict.update({"form_common_attributes": json.dumps(self.form_common_model.data)})
        message_body_dict.update({"form_specific_attributes": json.dumps(self.form_specific_model.data)})

        return json.dumps(message_body_dict)

        