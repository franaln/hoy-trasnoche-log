import pandas as pd
import yaml


df = pd.read_csv('episodes.csv')

movies_db = yaml.safe_load(open('pelis.yml', 'r'))

def get_duration_min(ms):
    return int(round(ms / 1000 / 60, 0))


txt = """hoy-trasnoche-log
=================


"""

ep_counter = len(df)

for ix, ep in df.iterrows():

    name = ep['name']
    date = ep['release_date'].replace('-', '.')
    dur = get_duration_min(ep['duration_ms'])
    desc = ep['description']
    url = ep['url']

    print(name)

    movies = None
    if name in movies_db:
        movies = movies_db[name]

    spc = '\n\n'

    txt += f"## [{ep_counter}] - {date} - {name} ({dur}m) [spotify]({url}){spc}"
    if movies is not None:
        print(movies)
        for movie in movies:
            txt += f'* {movie}{spc}'
    txt += f'{desc}{spc}'

    ep_counter -= 1


with open('README.md', 'w+') as f:
    f.write(txt)
