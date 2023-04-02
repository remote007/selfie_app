# import opencv-python
from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from functools import partial
from kivy.clock import Clock

class app_selfie(App):
    def build(self):
        self.obj_camera = Camera()
        self.obj_camera.play = True
        self.obj_camera.resolution = (800,800)
        obj_button = Button(text="Click!!")
        obj_button.size_hint = (.5,.2)
        obj_button.pos_hint = {'x':.25,'y':.25}
        obj_button.bind(on_press=self.selfie_take)
        obj_layout = BoxLayout()
        obj_layout.add_widget(self.obj_camera)
        obj_layout.add_widget(obj_button)
        return obj_layout
    
    def selfie_take(self,*args):
        print("selfie successfull")
        Clock.schedule_once(partial(self.obj_camera.export_to_png, 'selfie.png') )
        # self.obj_camera.export_to_png("./demoselfie.png")

if __name__=='__main__':
    app_selfie().run()




