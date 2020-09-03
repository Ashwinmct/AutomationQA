class ScreenShot(object):
	@classmethod
	def take_screen_shot(cls, driver, screen_shot_name):
		screen_shot_name = "./screen_shots/"+screen_shot_name+".png"
		driver.save_screenshot(screen_shot_name)
