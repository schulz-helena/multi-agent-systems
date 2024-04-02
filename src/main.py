from model import MyModel

if __name__ == '__main__':
    model = MyModel(2)
    for _ in range(4):
        model.step()