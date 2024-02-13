
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

from kivy.lang.builder import Builder
from kivy.core.text import LabelBase
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.properties import ObjectProperty

import random

kv_design = """
#:import chex kivy.utils.get_color_from_hex

MainWindow:
	
	heart1 : heart1
	heart2 : heart2
	lyrics : lyrics
	
	canvas.before:
		Color:
			rgba : chex("#FFFCED")
		Rectangle:
			pos : self.pos
			size : self.size
	
	MDBoxLayout:
		size_hint : 1 , 0.21
		pos_hint : { "x" : 0 , "y" : 0 }
		md_bg_color : chex("#9AA7B8")
	
	Image:
		source : "couple_backround_remove.gif"
		size_hint : 0.5, 1
		pos_hint : { "x" : 0 , "y" : 0 }
		allow_stretch : True
		anim_delay :  1 / 20
	
	Image:
		id : heart1
		source : "heart.png"
		size_hint : 0.1 , 0.05
		allow_stretch : True
		opacity : 0
	
	Image:
		id : heart2
		source : "heart.png"
		size_hint : 0.1 , 0.05
		allow_stretch : True
		opacity : 0
	
	MDRaisedButton:
		size_hint : 0.3 , 0.1
		text : "Click Here If You Love Me"
		pos_hint : { "center_x" : 0.75 , "center_y" : 0.23 }
		font_name : "reg_font"
		font_size : min(self.size) * 0.4
		md_bg_color : chex("#333C47")
		
		on_release:
			root.startAnimation(self)
	
	Label:
		id : lyrics
		size_hint : 0.45 , 0.4
		pos_hint : { "center_x" : 0.75 , "center_y" : 0.6 }
		font_name : "reg_font"
		font_size : min(self.size) * 0.2
		text : "Wag mo naman gawing tanga, alam namang andito na"
		text_size : self.width  , None
		halign : "center"
		color : "black"
	
"""


class MainWindow(MDFloatLayout):
	but_anim : Animation = None
	flower_anim : Animation = None
	sound = None
	
	heart1 : Image = ObjectProperty()
	heart2 : Image = ObjectProperty()
	lyrics : Label = ObjectProperty()
		
	
	def loadNeeded(self , *args):
		self.sound = SoundLoader.load("delulu_cutted.mp3")
	
	def startAnimation(self , button : object):
		def on_start_activity(*args):
			button.disabled = True
		
		self.but_anim = Animation( opacity = 0 , duration = .25)
		self.but_anim.bind(
			on_start = on_start_activity,
			on_complete = self.mainAcitivity
		)	
		self.but_anim.start(button)
	
	def mainAcitivity(self , *args):
		
		def on_complete(*args):
			self.heart1.opacity = 0
			self.heart2.opacity = 0
		
		

class GiftApp(MDApp):
	
#	def on_start(self , *arhs):
#		Clock.schedule_once(self.root.loadNeeded)
#		
	
	def build(self):
		return Builder.load_string(kv_design)

LabelBase.register(name = "reg_font" , fn_regular="AbrilFatface-Regular.ttf")
GiftApp().run()