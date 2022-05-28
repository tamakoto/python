audio_formats = ['MP3', 'MPG', 'AU', 'WMA' ]

input_formats = ['MP4', 'MP3', 'AVI', 'MKV', 'MPG', 'AU', 'MPEG',
'APE', 'MKA', 'TTA', 'MPE', 'M2P', 'M1V', 'M2V',
'VOB', 'DAT', 'WMA']

movies = ['Титаник', 'Назад в будущее', 'Бэтмен', 'Аватар',
'Начало', 'Рокки', 'Завтрак у Тиффани', 'Терминатор',
'Джуманджи', 'Хатико' ] 

formats = []
for f in input_formats:
    if f not in audio_formats:
        formats.append(f)
        
movies.sort()

for i in range(len(formats)):
    if len(movies) > i:
        film_file = f"{movies[i]}.{formats[i]}"
    else:
        film_file = 'Untitled'
    print(film_file)
