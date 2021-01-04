import datetime

class FileFormat:
    fmt = "%H-%M-%S-%f"

    def __init__(self, time, id_face, name='unknown'):
        self.time = time
        self.s_time = self.time.strftime(FileFormat.fmt)
        self.name = name
        self.id_face = id_face
    
    def to_string(self):
        return f'{self.s_time}_{self.name}_{self.id_face}.json'

    @classmethod
    def from_string(cls, s):
        data = s.split('_')
        t = datetime.datetime.strptime(data[0], FileFormat.fmt)
        return FileFormat(t, data[2], data[1])