import requests
from rest_framework.views import APIView
from rest_framework.response import Response




ALLOWED_CITIES = ['lahore', 'karachi', 'london', 'tokyo', 'new york']

API_KEY = 'api_key'

class WeatherAPIView(APIView):

    def get(self, request):
        
        city = request.GET.get('city')
        

        if not city:
            return Response({'error': 'City Name is Required!'})


        if city.lower() not in ALLOWED_CITIES:
            return Response ({'Error': f'Please Enter a Valid City Name!, You can Enter only one Of Following{ALLOWED_CITIES}'})
        
        
        url = (f'https://api.openweathermap.org/data/2.5/forecast'
        f'?q={city}&appid={API_KEY}&units=metric') 

        response = requests.get(url)
        data = response.json()



        current_weather = data['list'][0]['weather'][0]['description']
        wind_speed = data['list'][0]['wind']['speed']
        weather_1hour_ahead  = data['list'][1]['weather'][0]['description']


        result = {
        
                'city':city,
                'current_weather':current_weather,
                'wind_speed':wind_speed,
                'weather_1hour_ahead':weather_1hour_ahead

                }

        return Response(result)







