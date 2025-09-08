import requests

def get_posts():
    """Получение и вывод первых 5 постов из JSONPlaceholder"""
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        # Отправляем GET-запрос
        response = requests.get(url)
        response.raise_for_status()  # Проверяем на ошибки
        
        # Получаем данные в формате JSON
        posts = response.json()
        
        # Выводим первые 5 постов
        print("=" * 60)
        print("ПЕРВЫЕ 5 ПОСТОВ:")
        print("=" * 60)
        
        for i, post in enumerate(posts[:5], 1):
            print(f"\nПост #{i}")
            print(f"Заголовок: {post['title']}")
            print(f"Текст: {post['body'][:100]}...")  # Первые 100 символов
            print("-" * 40)
            
        print(f"\nВсего получено постов: {len(posts)}")
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
    except ValueError as e:
        print(f"Ошибка при обработке JSON: {e}")

# Запуск функции
if __name__ == "__main__":
    get_posts()


def get_weather():
    """Получение данных о погоде для указанного города"""
    
    # API ключ (нужно заменить на свой)
    API_KEY = "your_api_key_here"  # Получите на https://home.openweathermap.org/api_keys
    
    # Если ключ не установлен, просим пользователя ввести
    if API_KEY == "your_api_key_here":
        API_KEY = input("Введите ваш OpenWeather API ключ: ").strip()
    
    # Получаем город от пользователя
    city = input("Введите название города: ").strip()
    
    if not city:
        print("Ошибка: Не указан город")
        return
    
    # URL для запроса
    url = f"http://api.openweathermap.org/data/2.5/weather"
    
    # Параметры запроса
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',  # метрическая система (градусы Цельсия)
        'lang': 'ru'        # русский язык для описания погоды
    }
    
    try:
        # Отправляем GET-запрос
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        # Получаем данные
        data = response.json()
        
        # Извлекаем нужную информацию
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        city_name = data['name']
        country = data['sys']['country']
        
        # Выводим результат
        print("\n" + "=" * 40)
        print(f"ПОГОДА В {city_name.upper()}, {country}")
        print("=" * 40)
        print(f"Температура: {temperature}°C")
        print(f"Описание: {weather_description.capitalize()}")
        print(f"Влажность: {humidity}%")
        print(f"Скорость ветра: {wind_speed} м/с")
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
    except KeyError as e:
        print(f"Ошибка: Не удалось найти данные для города '{city}'")
        print("Проверьте правильность написания названия города")
    except ValueError as e:
        print(f"Ошибка при обработке данных: {e}")