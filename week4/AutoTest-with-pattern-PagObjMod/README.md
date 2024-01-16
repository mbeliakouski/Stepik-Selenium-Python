# AutoTest-with-pattern-PagObjMod
Module №4

Link on module #4 https://stepik.org/lesson/199980/step/1?unit=174035

Кланируем проект:

git clone https://github.com/mbeliakouski/AutoTest-with-pattern-PagObjMod.git
git clone git@github.com:mbeliakouski/AutoTest-with-pattern-PagObjMod.git

Создание виртуального окружения:

python3 -m pip install pip
sudo apt-get install -y python3.7-venv
python3 -m venv selenium_env

Активируем окружение:
source selenium_env/bin/activate


Установка пакетов:
pip install -r requirements.txt

Пример команды запуска тестов:
pytest -s -v -m exemple --tb=line --language=en test_main_page.py

-s - чтобы увидеть текст, который выводится командой print()
-v - подробрный,в отчёт добавится дополнительная информация со списком тестов и статусом их прохождения
-m - запуск маркированных тестов
--tb=line - которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста.
--langueage=en созданный кастомный параметр 
test_xx_xx.py запуск файла в котором находятся тесты

Запустк тестов с меткой need_review для проверки финального задания:
pytest -v --tb=line --language=en -m need_review

Выйти из нашего окружения:
deactivate