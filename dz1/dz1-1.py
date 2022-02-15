def convert_time(duration: int) -> str:
    if duration < 60:
        pertime = (duration, 'сек')
    elif duration < 3600:
        pertime = (duration // 60, 'мин', duration % 60, 'сек')
    elif duration < 86400:
        pertime = (duration // 3600, 'час', duration % 3600 // 60, 'мин', duration % 3600 % 60, 'сек')
    elif duration < 31536000:
        pertime = (duration // 86400, 'дн', duration % 86400 // 3600, 'час', duration % 86400 % 3600 // 60, 'мин', duration % 86400 % 3600 % 60, 'сек')
    elif duration > 31536000:
        pertime = 'больше 1 года'
    return pertime

duration = 400153
result = convert_time(duration)
print(result)
