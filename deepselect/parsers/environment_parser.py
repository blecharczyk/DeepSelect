from deepselect.environment import Environment

class EnvironmentParser:
    def __init__(self):
        pass

    def read_file(self, file_name):
        with open(file_name) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        return content

    def make_environment(self, file_name):
        file = self.read_file(file_name)
        number_of_nodes = file[0]
        file.pop(0)
        env = Environment(int(number_of_nodes))
        for f in file:
            print(f)
            env.add_edge(int(f[0]), int(f[2]))
        return env