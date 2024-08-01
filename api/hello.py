import json
import os
import django
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIHandler

# Set the DJANGO_SETTINGS_MODULE environment variable to your project's settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Initialize Django
django.setup()

# Create an instance of the Django WSGI application
application = WSGIHandler()

def handler(event, context):
    # This is a simplified example. You may need to adapt this to your specific use case
    path = event.get('path', '/')
    method = event.get('httpMethod', 'GET')
    body = event.get('body', '')

    if method == 'GET':
        response = JsonResponse({"message": "Hello, World!"})
    elif method == 'POST':
        response_data = json.loads(body) if body else {}
        response = JsonResponse({"message": "Data received", "data": response_data})
    else:
        response = JsonResponse({"message": f"Method {method} not allowed"}, status=405)

    # Convert Django HttpResponse to Lambda compatible response
    return {
        "statusCode": response.status_code,
        "headers": dict(response.items()),
        "body": response.content.decode('utf-8')
    }
