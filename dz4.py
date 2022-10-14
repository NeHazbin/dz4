class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.memory = 128
class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "4k"
class CPU:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.processor = "Qualcomm Snapdragon 888"
class Camera:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolutionofcamera = "7680 x 4320 8K UHD"

class Android:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.version = "Android 12"
class Battery:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.batterycapacity = "4500mag"
class SmartPhone(Display, Computer, CPU,Camera,Android,Battery):
    def print_info(self):
        print(self.model)
        print(self.batterycapacity)
        print(self.version)
        print(self.resolutionofcamera)
        print(self.processor)
        print(self.resolution)
        print(self.memory)
iphone = SmartPhone(model = "Last")
iphone.print_info()