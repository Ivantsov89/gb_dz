def convert_time(duration: int) -> str:
    seconds = duration % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    str_out = f"вы указали {hour} часов  {minutes} минут  {seconds} секунд"
    return str_out
duration = 400153
result = convert_time(duration)
print(result)
