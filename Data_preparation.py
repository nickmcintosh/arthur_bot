import csv
import bs4
import requests


# Requesting Episodes Reference List
res = requests.get('https://arthur.fandom.com/wiki/List_of_episodes')
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Initial space to add entries
wiki_directory = soup.select('tbody tr')
wiki_entries = []

# text extraction into one list
for item in wiki_directory[28:-17]:
    if item.text.startswith('\nScreenshot'):
        pass
    elif 'air date' in item.text:
        pass
    elif item.text.startswith('\n1'):
        pass
    else:
        corrected_text = item.text.replace('\n\n\n', '')
        wiki_entries.append(corrected_text)

# comprehension into sublists. The following step renders this obselete, but I'm leaving it as is.
wiki_list_comp = [wiki_entries[i:i + 2] for i in range(0, len(wiki_entries), 2)]

# image grabber
image_list = []
image_finder = soup.select('tbody .image')

for image in image_finder:
    href = image.get('href')
    image_list.append(href)
missing_penultimate_image = 'https://static.wikia.nocookie.net/arthur/images/c/cb/Blabbermouth_main_image.jpg/revision/latest/scale-to-width-down/140?cb=20220222234927'
image_list.insert(-1, missing_penultimate_image)

# this fixes the sublists by episode. 'Modified sublists' will house all the data: [0] Title [1] Ep. Number [2] Air_date [3] Synopsis
modified_sublists = []
for sublist in wiki_list_comp:
    # this line strips out each piece. '\n'.join(sublist) joins them, whereas .split(\n) then creates the items individually
    parts = [s.strip() for s in '\n'.join(sublist).split('\n') if s.strip()]
    title = parts[0]
    episode_number = parts[2]
    air_date = parts[3]
    synopsis = parts[4]
    modified_sublist = [title, episode_number, air_date, synopsis]
    modified_sublists.append(modified_sublist)

# Appends image URL to modified sublists
for i, episode_data in enumerate(modified_sublists):
    episode_data.append(image_list[i])

# Finds link to individual episode page
link_finder = soup.select('b > a')
link_list_setup = []
link_list = []

for item in link_finder[22:]:
    href = item.get('href')
    full_link = 'https://arthur.fandom.com' + href
    link_list_setup.append(full_link)


# Writes modified_sublists to CSV

#Note that this required a bit of manual manipulation in Excel. I added Seasons manually because it was easier that way.
# I also reformatted inconsistent dates, moved the columns to be easier to work with, and a few other things.


def csv_writer():
    with open('episode_guide.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Episode', 'Hyperlink'])

        for i, item in enumerate(modified_sublists):
            row = [item[0], '']
            if i < len(link_list_setup):
                row[1] = link_list_setup[i]

            writer.writerow(row)

#Everything from here was then saved as 'episode_guide.csv' and manipulated from there