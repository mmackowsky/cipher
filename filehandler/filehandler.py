class Buffer:
    def __init__(self) -> None:
        self.buffer = []

    def show_buffer(self):
        for val in self.buffer:
            print(val)
