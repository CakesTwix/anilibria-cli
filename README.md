# Anilinria-cli

# Зависимости

 - requests 
 - click

# Примеры использования

    python anilibria-cli.py --help                

> Usage: anilibria-cli.py [OPTIONS] COMMAND [ARGS]...
> 
> Options:   --help  Show this message and exit.
> 
> Commands:   findtitle

    python anilibria-cli.py findtitle --help

> Usage: anilibria-cli.py findtitle [OPTIONS]
> 
> Options:   --title TEXT  Информация об тайтле   --desc        Вывести
> описание тайтла   --series      Ссылки на скачивание   --help       
> Show this message and exit.


    python anilibria-cli.py findtitle --title 'Нет игры' --desc
> Без игры — нет жизни | No Game No Life История «No Game, No Life»
> фокусируется на Соре и Широ, брате и сестре, ...

# Доступные команды

- findtitle
- randomtitle
- updates
- schedule

# Дополнительно

Используется API v2: https://github.com/anilibria/docs/blob/master/api_v2.md

