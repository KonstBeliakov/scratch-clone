from frames.code_frame import CodeFrame


class LookFrame(CodeFrame):
    def __init__(self, app):
        values = ['Sprite.hide()',
                  'Sprite.show()',
                  'Sprite.set_color(color)',
                  'Sprite.draw(screen)']
        super().__init__(app, values)
