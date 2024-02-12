В данном мини-проекте я попробовал парсить новости из уже скачанного датасета "lenta.ru":
1) Реализовал механику автоматической конвертации данных вида .json (из "downloaded dataset") в .txt ("dataset");
2) Далее я убирал стоп-слова из каждого файла .txt в подпапках (прим. названия подпапки: "15.02.2014") из директории "dataset", а также нормализовал все данные, чтобы привести все слова к одной форме;
3) Уже нормализованные слова (из каждого файла .txt в подпапках (прим. названия подпапки: "15.02.2014")) я перебрасывал в подпапки с тем же названием, но уже в итоговую директорию - "normalized dataset";
4) Далее я реализовал механику преобразования всех слов из "normalized dataset" в wordcloud, чтобы увидеть частоту использования всех слов - чем чаще было использовано то или иное слово, тем больше оно смотрелось в wordcloud.

Примечание: код "main.py" может не работать, так как писал я его давно и использовал старую версию Pyhton (для корректной работы библиотек) 
