import json
import datetime
import random
def lambda_handler(event, context):
    # Generate sample weather data
    weather_data = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "temperature": round(random.uniform(20, 35), 1),  # Random temp between 20-35°C
        "humidity": random.randint(40, 90),  # Random humidity between 40-90%
        "location": "Bangalore"
    }   
    return {
        "statusCode": 200,
        "body": json.dumps(weather_data)
    }
