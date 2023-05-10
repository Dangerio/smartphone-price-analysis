Содержание работы:
1) Файл Analysis1.ipynb содержит следующие пункты анализа: Обратка данных (включая удаление выбросов), Multicollinearity, 	Heteroskedasticity, Спецификация модели, Функциональная форма. Для запуска используется 'PhonesDF_years.csv' и последовательно 	обрабатывается.
2) Файл Analysis2.ipynb содержит следующие пункты анализа: Эндогенность
3) AllLinearModels.ipynb.ipynb содержит продолжаение анализа, рассмотрение 4х разлчиных спецификаций модели. (3 модели с 1 объсяеющей 	переменной, одна с полной спецификацией, рассмотренной в Analysis1.ipynb и Analysis2.ipynb)
4) Файл QuantileRegression&Forecasts_v2.ipynb содержит следующие пункты анализа: Квантильная регрессия, осуществление пронозов
5) Файл PreparingData.py содержит вторичную обработку данных, которая также реализована в Analysis1.ipynb
6) Файл initial_preparation.py содержит раскрытипе колонки 'specs' и первичную обработку данных
7) Файл Getting datas for phones.ipynb содержит парсер для получение "YEAR OF RELEASE"

Данные:
1) PhonesPriceInKenya_v2 - изначальный датасет, используется в файле 'initial_preparation.py' для получение обработного файла
	с новыми данными, нахоядщимися в признаке 'specs'
2) PhonesDF.csv - файл, полученный после обрабокти PhonesPriceInKenya_v2 в initial_preparation.py, содержит извлеченные признаки из SPECS
3) PhonesDF_years.csv - файл, полученный после добавление нового признака "YEAR OF RELEASE" к 'PhonesDF.csv' c помощью парсера в файле 	'Getting datas for phones.ipynb'
4) PhonesDFUndroppedV2.csv - файл после обработки  'PhonesDF_years.csv', полученный на основе удаление выбросов с помощью стьюдентизированных 	остатков, а также добавление дамми переменных на основе категориальных признаков (получен в Analysis1.ipynb)
5) PhonesDF_years_corrected_v2.csv - файл после обработки 'PhonesDFUndroppedV2.csv' после всего 'Analysis1.ipynb', то есть добавления 	признаков, их удаления из-за мультколлинеарности и т.д.

Файлы, в которых происходит анализ (по очереди): 
1) Analysis1.ipynb - требует датасет PhonesDF_years.csv (и в итоге обрабатывает до файла PhonesDF_years_corrected_v2.csv)
2) Analysis2.ipynb - требует датасет PhonesDF_years_corrected_v2.csv и PhonesPriceInKenya_v2.csv. Первый как итоговый после Analysis1.ipynb 
	для дальнейшего анализа моделей, второй как изначальный файл, в котором содержится инструментальная перменная Specs Score'
3) AllLinearModels.ipynb.ipynb - требует датасет PhonesDF_years_corrected_v2.csv. Продолжение анализа, в котором рассмотрение 4х разлчиных спецификаций модели. (3 модели с 1 объсяеющей 	переменной, одна с полной спецификацией)
4) QuantileRegression&Forecasts_v2.ipynb содержит следующие пункты анализа: Квантильная регрессия, осуществление пронозов
