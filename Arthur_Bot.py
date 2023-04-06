import _datetime
import discord
import csv
import random
import bs4
import requests
import re
import datetime


TOKEN = '__'
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


def read_arthur_data():
    with open('episode_guide.csv', newline='') as arthur_data:
        reader = csv.reader(arthur_data)
        full_arthur_set = [row for row in reader]
    return full_arthur_set

def trivia_retrieval(x):
    trivia_request = requests.get(x)
    trivia_soup = bs4.BeautifulSoup(trivia_request.text, 'lxml')
    trivia_header = trivia_soup.find('span', id='Trivia')
    trivia_section = trivia_header.find_parent('h2')
    trivia_contents = []
    for sibling in trivia_section.find_next_siblings():
        if sibling.name == 'h2':
            break
        else:
            trivia_contents.append(sibling.text)

    trivia_contents = ''.join(trivia_contents)
    removal_words = ['Episode connections','Cultural references','Errors', 'Production notes']
    for instance in removal_words:
        trivia_contents = trivia_contents.replace(instance, ' ')
    line_break_format = '\n'

    trivia_contents = [word.strip() for word in re.split(r'\. *\n| *\n', trivia_contents)]
    return trivia_contents





def new_arthur_fact():
    full_arthur_set = read_arthur_data()
    episode_data = random.choice(full_arthur_set)
    img_url = episode_data[5]
    # embed = discord.Embed()
    # embed.set_image(url=img)
    #Retrieve the trivia
    trivia_element = trivia_retrieval(episode_data[6])
    fact_string = ''
    fact_string += f'**This Arthur fact is from [{episode_data[0]}]({episode_data[6]}), which is episode {episode_data[2]} from season {episode_data[1]}.\n**'
    fact_string += '\n*Here is a cool ass Arthur fact:* \n\n'
    fact_string += random.choice(trivia_element) + '\n'
    embed = discord.Embed(description=fact_string, color=discord.Color.brand_green())
    embed.set_image(url=img_url)
    return embed


@client.event
async def on_ready():
    print("Who's ready to win and get their factual rewards?! {0.user} is in the chat! Type 'fact' to get started.".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    timestamp = _datetime.datetime.now()
    print(timestamp)

    if message.author == client.user:
        return

    if channel == 'arthur_facts':
        if user_message.lower() == 'fact':
            read_arthur_data()
            episode_data = new_arthur_fact()
            await message.channel.send(embed=episode_data)
            return
        else:
            await message.channel.send('To activate me, type "fact" into the chat.')
            return

def run(TOKEN):
    client.run(TOKEN)

if __name__ == '__main__':
    client.run(TOKEN)










