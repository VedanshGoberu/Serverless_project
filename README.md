The Daily Weather Notification System is a cloud-based, serverless application designed to send daily weather updates via SMS to users. It uses the OpenWeatherMap API to fetch real-time weather data and AWS services like Lambda, SNS, and EventBridge to automate the entire process without the need for any manual action or server management.

🧠 How It Works:
EventBridge triggers the Lambda function automatically at a scheduled time each day (e.g., 7:00 AM).

The Lambda function fetches the current weather data of a specified city from the OpenWeatherMap API.

It formats this information into a message like:
“Good morning! Weather in Hyderabad: clear sky, Temp: 28°C”.

The message is sent as an SMS to a user's phone using Amazon SNS.

All components are integrated seamlessly and run in a fully automated, cost-efficient way using the pay-as-you-go model of AWS.

🎯 Usefulness:
Keeps users informed of daily weather without needing to check apps or websites.

Especially helpful for students, commuters, farmers, delivery services, or anyone planning their day.

It’s automated, scalable, and lightweight, running on a schedule without human intervention.

Great example of applying serverless cloud architecture for a real-world, useful utility.
