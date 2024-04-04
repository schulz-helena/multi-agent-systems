from model import MyModel

if __name__ == '__main__':
    model = MyModel(2)
    while any(model.positions):
        model.step()