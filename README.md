Тестовый сценарий:

1.Перейдите в директорию project и выполните init.sh скрипт командой bash init.sh. Во время его исполнения вам будет необходимо ввести пароль для того, чтобы установить необходимые пакеты python, flask, mod_wsgi для третьей версии питона и выполнить остальные команды скрипта для развертывания приложения.

2.После исполнения данного скрипта вы можете получить html страницу с возможностью загрузки файла на сервер двумя способами:
    по url http://127.0.0.1:80/upload
    по url http://gen.template:80/upload
    
3.Допускается загружать файлы формата txt, doc, xlsx. Вы можете выбрать один из файлов на вашей машине и после загрузки найти его в папке /var/www/FlaskApp/FlaskApp/uploads
