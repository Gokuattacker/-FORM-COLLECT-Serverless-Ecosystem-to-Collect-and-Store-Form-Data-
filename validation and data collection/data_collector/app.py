from data_processor import AtlanDataCollector

def lambda_handler(event, context):
    atlan_data_collector = AtlanDataCollector()
    atlan_data_collector.process_event(event)