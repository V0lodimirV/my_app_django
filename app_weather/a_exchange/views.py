from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import requests # импортируем requests
"""
что бы всё работало как положено, нам нужен API с котировками валют,
его можно взять на сайте exchangerate, там кроме даты и времени апдейта
есть нужный нам СЛОВАРЬ "rates" с котировками валют разных стран
"""

def exchange(request):#создаем функцию
#что бы достать нужный словарь с котировками делаем запрос к API

    response = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
    currencies = response.get('rates')#сохраняем полученый словарь в переменную
    """теперь нам нужно передать возможные для конвертации валюты
    выподающие списки в нашей форме"""

    if request.method == 'GET':
        # если метод запроса = "GET"

        #тогда отправляем полученый словарь на шаблон
        context = {
            'currencies': currencies#словарь в котором ключами выступают валюты
                                    #а значения - сконвертированная сумма к 1$
        }


        return render(request=request, template_name='exchange/index_exchange.html', context=context)

    if request.method == 'POST':#если метод = "POST"
        from_amount = (request.POST.get('from-amount'))#то извлекаем сначала число
        from_curr = request.POST.get('from-curr')#а затем из какой валюты конвертируем
        to_curr = request.POST.get('to-curr')#и в какую валюту конвертируем
        """выполним конвертацию,разделим значение валюты которую хотим получить,
        на значение валюты которую мы меняем и умножаем на переданное количество,
         приведённое к дробному числу, обернём всё в функцию round(округляет число
         с плавающей точкой,до цифры которую мы задаём, у нас 2)"""
        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * float(from_amount), 2)

        """сформируем словарь с данными для передачи на шаблон
        добавляем список с валютами и сконвертированное значение
        что бы введённые значения не сбрасывались передаём в словарь
        значения полей"""
        context = {
            'from_curr': from_curr,
            'to_curr': to_curr,
            'from_amount': from_amount,
            'currencies': currencies,
            'converted_amount': converted_amount
        }

    return render(request, 'exchange/index_exchange.html', context=context)



