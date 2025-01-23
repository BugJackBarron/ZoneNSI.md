import imageio
filenames = ['P1.png']*2
filenames += [f'P{i}.png' for i in range(1,17)]
filenames += ['P16.png']*2
with imageio.get_writer('triSelection.gif', mode='i', duration=0.75) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)