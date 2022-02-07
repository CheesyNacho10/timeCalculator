def add_time(start, duration, weekday=None):
  new_time = list()
  start = convertTo24Format(start).split(':')
  duration = duration.split(':')

  sum_minutes = start[1] + duration[1]
  sum_hours = start[0] + duration[0]
  days = (sum_hours + (sum_minutes / 60)) / 24

  new_time.append(int((sum_hours + (sum_minutes / 60)) % 24))
  new_time.append(int(sum_minutes % 60))
  new_time = map(str, new_time)
  new_time = convertTo12Format(':'.join(new_time))

  return new_time

def convertTo24Format(time):
  time = time.split()
  hour = time[0].split(':')
  if (time[1] == 'PM'):
    hour[0] = str(int(hour[0]) + 12)
  return ':'.join(hour)

def convertTo12Format(time):
  time = time.split(':')
  if (int(time[0]) > 12) :
    time[0] = int(time[0]) - 12
    additional_format = 'PM'
  else:
    additional_format = 'AM'
  return twoDigits(time) + ' ' + additional_format

def twoDigits(time):
  if (int(time[1]) < 10): return time[0] + ':' + '0' + time[1]
  else: return time[0] + ':' + time[1]
