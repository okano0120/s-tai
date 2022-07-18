import random

def create_lap():
  return str(random.randrange(18948, 22456) / 1000)

def create_recoerd(number):
  record = []
  record.append(str(number))
  record.append(str(random.randrange(18948, 22456) / 1000))
  record.append(str(random.randrange(18948, 22456) / 1000))

  return record

init_record = ['1', '21.895', '19.945', '19.975', '21.265']

sec_count = 0
print(init_record)
for i in range(500):

  if (random.randrange(2) == 0):
    init_record[sec_count + 1] = create_lap()
    sec_count = (sec_count + 1) % 4

    if sec_count == 0:
      init_record[0] = str(int(init_record[0]) + 1)
  print(init_record)
