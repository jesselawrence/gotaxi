import scipy.io as sio

road_data = sio.loadmat('road_all.mat')
road_index = []
index_file = open('index','r')

for i in index_file:
    i.strip()
    road_index.append(eval(i))

index_file.close()
