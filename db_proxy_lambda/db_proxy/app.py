from db_processor import DbProcessor

def lambda_handler(event, context):
    db_processor = DbProcessor()
    return db_processor.process_event(event)