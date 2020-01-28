import imageio
images = []
filenames = ["pic1.png", "pic2.png"]
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave("animate.gif", images, duration=0.5)