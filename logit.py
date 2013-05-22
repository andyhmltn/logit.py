import os
import datetime

class Logit:
	def __init__(self, app_name='Application'):
		self.application = {
			'name'      : app_name,
			'safe_name' : app_name.lower().replace(' ','-'),
			'logit_path': '%s/.logit' % (os.path.expanduser("~")),
		}

		self.application['log_file'] = "%s/%s.log" % (self.application['logit_path'], self.application['safe_name'])

		if not os.path.exists(self.application['logit_path']): 
			os.makedirs(self.application['logit_path'])

		if not os.path.exists(self.application['log_file']):
			open(self.application['log_file'], 'w+')

	def record(self, item, message):
		item         = item.upper()
		
		now			 = datetime.datetime.now()
		current_time = now.strftime("%I:%M %p")
		current_date = now.strftime("%d/%m/%Y")

		full_log     = "[%s] [%s][%s] %s\n" % (item, current_time, current_date, message)

		with open(self.application['log_file'], "a+") as log_file:
			log_file.write(full_log)

