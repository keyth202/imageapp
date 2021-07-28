import os


directory = r'./img/'
folder = ''
images =[]

def imageWalk():
    for filename in os.listdir(directory+folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            print(os.path.join(directory, filename))
            images.append( os.path.join(directory, filename))
        else:
            continue

    return images


