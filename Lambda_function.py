import boto3
import requests
import os

def lambda_handler(event, context):
    city = os.environ['CITY']
    phone = os.environ['PHONE_NUMBER']
    api_key = os.environ['WEATHER_API_KEY']

    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        weather_data = requests.get(url).json()

        description = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        msg = f"Good morning! Weather in {city}: {description}, Temp: {temp}°C"

        sns = boto3.client('sns')
        sns.publish(
            PhoneNumber=phone,
            Message=msg
        )

        return {
            'statusCode': 200,
            'body': 'Weather SMS sent!'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
