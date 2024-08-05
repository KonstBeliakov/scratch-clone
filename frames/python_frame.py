from frames.code_frame import CodeFrame


class PythonFrame(CodeFrame):
    def __init__(self, app):
        values = ['if(condition):\n    # actions if True\nelse:\n    # actions if false',
                  'while(condition):\n    # actions',
                  'for i in range(n):\n    # actions, repeating n times',
                  'match(expression):\n    case value1:\n        # action 1\n    case value2:\n        #action 2']
        super().__init__(app, values)
