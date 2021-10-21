import os


directory = r'imageapp/static/img/'
folder = ''
images =[]

def imageWalk():
    for filename in os.listdir(directory+folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            #print(os.path.join(directory, filename))
            images.append( os.path.join(r'img/', filename))
            
        else:
            continue
    print(images[0])
    return images


