class Tracker:
  def __init__(self, settings):
    self.settings = settings

  def track(self):
    print(self.settings.fetcher_type)
