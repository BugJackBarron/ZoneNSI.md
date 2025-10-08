import imageio
filenames = ['P1.png']*2
filenames +=[f'P{i}.png' for i in range(1,15)]
filenames += ['P14.png']*2
with imageio.get_writer('triInsertion.gif', mode='i', duration=1) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)