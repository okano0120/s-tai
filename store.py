import glob
import csv
import time

class Store:
  def __init__(self, controller_name):
    self.controller_name = controller_name
    self.current_file_number = self.get_current_file_number(controller_name)

    file_path = self.get_file_path()
    self.create_file(file_path)

  def create_file(self, file_path):
    f = open(file_path, 'w', newline="")
    writer = csv.writer(f)
    writer.writerows([])
    f.close()

  def add_record(self, record):
    file_path = self.get_file_path()
    f = open(file_path, 'a', newline="")
    writer = csv.writer(f)
    writer.writerow(record)
    f.close()

  def get_file_name(self):
    return self.make_file_name_by(self.current_file_number)

  def get_file_path(self):
    return './files/{file_name}'.format(file_name=self.get_file_name())

  def get_current_file_number(self, controller_name):
    i = 0
    file_name = self.make_file_name_by(i)

    while glob.glob('./files/{file_name}'.format(file_name=file_name)):
      i += 1
      file_name = self.make_file_name_by(i)
    return i
  
  def make_file_name_by(self, number):
    return '{controller_name}{number}.csv'.format(controller_name=self.controller_name, number=number)

def call():
  store = Store('html_tracker')
  store.add_record(['hoge', 'huga'])
  time.sleep(3)
  store.add_record(['hoge1', 'huga1'])
  time.sleep(3)
  store.add_record(['hoge2', 'huga2'])
  time.sleep(3)
  store.add_record(['hoge3', 'huga3'])
  time.sleep(3)
  store.add_record(['hoge4', 'huga4'])
  time.sleep(3)
  store.add_record(['hoge5', 'huga5'])
  time.sleep(3)
  store.add_record(['hoge6', 'huga6'])

# call()
