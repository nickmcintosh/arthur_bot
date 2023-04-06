# import discord
# import csv
# import random
# import bs4
# import requests
#
#
# def read_arthur_data():
#     with open('episode_guide.csv', newline='') as arthur_data:
#         reader = csv.reader(arthur_data)
#         full_arthur_set = [row for row in reader]
#     return full_arthur_set
#
# def trivia_retrieval(x):
#     trivia_request = requests.get(x)
#     trivia_soup = bs4.BeautifulSoup(trivia_request.text, 'lxml')
#     trivia_header = trivia_soup.find('span', id='Trivia')
#     trivia_section = trivia_header.find_parent('h2')
#     trivia_contents = []
#     for sibling in trivia_section.find_next_siblings():
#         if sibling.name == 'h2':
#             break
#         elif sibling == 'Episode connections' or 'Cultural references' or 'Errors' or 'Production notes':
#             break
#         else
#             trivia_contents.append(sibling.text)
#     trivia_return = trivia_contents.split('\n')
#     return trivia_return
#
#
#
#
#
# def new_arthur_fact():
#     full_arthur_set = read_arthur_data()
#     episode_data = random.choice(full_arthur_set)
#     img_url = episode_data[5]
#     #Retrieve the trivia
#     trivia_element = trivia_retrieval(episode_data[6])
#     fact_string = ''
#     fact_string += f'**This Arthur fact is from {episode_data[0]}, which is episode {episode_data[2]} from season {episode_data[1]}.\n\n**'
#     fact_string += f'[link to episode page]{episode_data[6]}'
#     fact_string += '\n\nHere are some cool ass Arthur facts \n'
#     fact_string += '- ' + random.choice(trivia_element) + '\n'
#     embed = discord.Embed(description=fact_string, color=discord.Color.brand_green())
#     embed.set_image(url=img_url, position=1)
#     return embed




test = ['lkjasdlf\n', 'aksl;dfjd', 'aksdl;fjd']

new = ''.join(test)
new = new.replace("\n", "wow")
print(new)


