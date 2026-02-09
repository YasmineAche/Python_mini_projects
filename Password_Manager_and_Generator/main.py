from view import View
from model import Model
from controller import Controller

if __name__ == '__main__':
    view = View()
    model = Model()
    controller = Controller(model, view)
    view.loop()
