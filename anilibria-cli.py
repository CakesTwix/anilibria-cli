import click
import requests
import os


def get_ru_en_name(item):
    return item['names']['ru'] + ' | ' + item['names']['en']


def show_titles_list(url, desc):
    # Generate separator line, if desc is True
    if desc:
        # Get rows and columns of terminal
        # Rows is unneeded value
        _, columns = os.popen('stty size', 'r').read().split()
        # Generate separator line
        separator_line = '━' * int(columns)
    response = requests.get(url)
    data = response.json()
    for item in data:
        click.echo('* ' + get_ru_en_name(item))
        if desc:
            click.echo(item['description'])
            click.echo(separator_line)
    return response


@click.group()
def cli():
    """..%%%%...%%..%%..%%%%%%..%%......%%%%%%..%%%%%...%%%%%...%%%%%%...%%%%..
.%%..%%..%%%.%%....%%....%%........%%....%%..%%..%%..%%....%%....%%..%%.
.%%%%%%..%%.%%%....%%....%%........%%....%%%%%...%%%%%.....%%....%%%%%%.
.%%..%%..%%..%%....%%....%%........%%....%%..%%..%%..%%....%%....%%..%%.
.%%..%%..%%..%%..%%%%%%..%%%%%%..%%%%%%..%%%%%...%%..%%..%%%%%%..%%..%%.
........................AniLibria-cli от Тортика........................
........................................................................"""


@click.command()
@click.option('--title', help='Информация об тайтле')
@click.option('--desc', is_flag=True, help='Вывести описание тайтла')
def findtitle(title, desc):
    show_titles_list('https://api.anilibria.tv/v2/searchTitles?search=' + title, desc)


cli.add_command(findtitle)


@click.command()
@click.option('--desc', is_flag=True, help='Вывести описание тайтла')
def updates(desc):
    show_titles_list('https://api.anilibria.tv/v2/getUpdates', desc)


cli.add_command(updates)


@click.command()
@click.option('--desc', is_flag=True, help='Вывести описание тайтла')
def randomtitle(desc):
    response = requests.get('https://api.anilibria.tv/v2/getRandomTitle')
    name = response.json()
    click.echo(get_ru_en_name(name))
    if desc:
        click.echo(name['description'])


cli.add_command(randomtitle)


@click.command()
def schedule():
    days = {0: "Понедельник",
            1: "Вторник",
            2: "Среда",
            3: "Четверг",
            4: "Пятница",
            5: "Суббота",
            6: "Воскресенье"}

    response = requests.get('https://api.anilibria.tv/v2/getSchedule')
    name = response.json()
    for daysItem in name:
        click.echo(days.get(daysItem["day"]))
        for listTitle in daysItem["list"]:
            click.echo('* '+get_ru_en_name(listTitle))



cli.add_command(schedule)

if __name__ == '__main__':
    cli()
