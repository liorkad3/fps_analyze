import datetime
import random
from FileFormat import FileFormat
import os.path as osp

fmt = "%H-%M-%S-%f"

data_dir = 'data'

avg_per_frame = 4
std_per_frame = 1.5

latency = 20   #ms
avg_time_face = 100  #ms
std_time_face = 3  #ms

avg_break = 100  #frames
std_break = 1   #frames

avg_brk_time = 1500
std_brk_time = 200

curr = datetime.datetime.now()
end_exp = curr + datetime.timedelta(minutes=1)

conc_frames=0
while curr < end_exp:
    num_frames = int(random.gauss(avg_break, std_break))
    num_frames = max(5, num_frames)
    brk_time = random.gauss(avg_brk_time, std_brk_time)

    for i in range(num_frames):
        num_faces = int(random.gauss(avg_per_frame, std_per_frame))
        num_faces = max(1, num_faces)
        for n in range(num_faces):
            ff = FileFormat(curr, n).to_string()
            path = osp.join(data_dir, ff)
            open(path, 'x')
        face_time = max(10, int(random.gauss(avg_time_face, std_time_face)))
        delta = latency + face_time * num_faces
        curr = curr + datetime.timedelta(milliseconds=delta)

    curr = curr + datetime.timedelta(milliseconds=brk_time)




