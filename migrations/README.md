Так как необходимые папки и файлы уже созданы и располагаются в проекте,
то нет и смысла выполнять команду `alembic init migration`.

В качестве СУБД используется `postgresql` и по этой причине перед осуществлением
миграции необходимо в pgAdmin создать пустую базу данных (буквально пустую. Без таблиц, процедур и т.п.)
с названием, какая указана в переменной DB_NAME в файле .env.

В файле alembic.ini раскомментирована строка с переменной file_template для большей информативности коммитов.
Так же была убрана переменная sqlalchemy.url, так как её значение и так задается в файле `migrations/env.py` на 16 строчке.
Еще было изменено значение переменной `prepend_sys_path` с `.` на `src/` потому что я просто не понимаю
как работают импорты в этом проклятом языке и каким-то чудом я смог сделать так, чтоб создание миграций и апгрейды
БД сопровождались без ручного изменения импортов в файлах `src` и их возвращения в исходное состояние после
работы с `alembic`. Система модулей в этом языке проклята.

В директории `migrations/versions` уже имеется коммит и для создания таблиц необходимо выполнить комманду `alembic upgrade heads`

Если вы внесли изменения в моделях, то их необходимо закоммитить коммандой `alembic revision --autogenerate -m "Описание коммита"`
и внести изменения в БД: `alembic upgrade heads`
