def turn_on_light(room):
    print(f"Turned on light in {room}")

def set_temperature(temp):
    print(f"Set temperature to {temp}")

def play_music(music):
    print(f"Playing {music}")

class Actions:
    def __init__(self,func,*args):
        self.func = func
        self.args = args
    
    def execute(self):
        self.func(*self.args)

class Scene:
    def __init__(self):
        self.actions = []
    
    def add_action(self,action):
        self.actions.append(action)
    
    def run(self):
        for action in self.actions:
            action.execute()

action1 = Actions(turn_on_light, "Living Room")
action2 = Actions(set_temperature, 24)
action3 = Actions(play_music, "Relaxing Jazz")

scene1 = Scene()
scene1.add_action(action1)
scene1.add_action(action2)
scene1.add_action(action3)

scene1.run()
