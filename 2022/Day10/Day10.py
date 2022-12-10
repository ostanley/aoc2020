from core.reader import read_line


class Display:
    def __init__(self):
        self.signal = 1
        self.iter = 0

    def draw_signal(self):
        sprite = self.iter % 40
        if self.signal in range(sprite - 1, sprite + 2):
            print("#", end="")
        else:
            print(".", end="")
        if (sprite + 1) % 40 == 0:
            print("\n", end="")

    def check_return(self):
        if (self.iter - 20) % 40 == 0:
            return_signal = self.signal * self.iter
            return return_signal
        else:
            return 0

    def run_iter(self, return_signal):
        self.draw_signal()
        self.iter += 1
        return max(return_signal, self.check_return())

    def process_buffer(self, line):
        return_signal = 0

        if line == "noop":
            self.run_iter(return_signal)
        else:
            for _ in range(2):
                self.run_iter(return_signal)
            self.signal += int(line.split(" ")[-1])
        return return_signal


if __name__ == "__main__":
    file = "Day10/Day10input.txt"
    display = Display()
    print(f"total signal strength: {read_line(file, display.process_buffer)}")
