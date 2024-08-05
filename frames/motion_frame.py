from frames.code_frame import CodeFrame


class MotionFrame(CodeFrame):
    def __init__(self, app):
        values = ['Sprite.go_to(x, y)',
                  'Sprite.go_to_random_position()',
                  'Sprite.move(steps)',
                  'Sprite.turn(degrees)',
                  'Sprite.set_direction(direction)',
                  'Sprite.if_on_edge_bounce() (not working)',]
        super().__init__(app, values)
