from frames.code_frame import CodeFrame


class SensingFrame(CodeFrame):
    def __init__(self, app):
        values = ['Sprite.touching(sprite2) (not working)',
                  'key_pressed(K_SPACE)']
        super().__init__(app, values)
