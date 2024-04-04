from model import MyModel
from animation import Animation

if __name__ == '__main__':
    model = MyModel(2)
    while any(model.positions):
        model.step()
    ani = Animation.map_animation(model.map, model.positions_all_timesteps)
    ani.save('animation.gif', writer='pillow', dpi = 600)