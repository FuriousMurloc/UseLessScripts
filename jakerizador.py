from PIL import Image
#list of input files
fotos = ["Random.jpg"]
#path to output directory
outPath = "Pictures/"
for foto in fotos:
    with Image.open(foto) as IMG:
        print foto
        pixels = IMG.load()
        w,h = IMG.size
        size = (w,h)
        negre = (0,0,0)
        verd = (0,255,0)
        for i in range(w):
            for j in range(h):
                coord = (i,j)
                R,G,B = pixels[i,j]
                if R < 50 or G < 50 or B < 50:
                    IMG.putpixel(coord,verd)
                else:
                    IMG.putpixel(coord,negre)
        IMG.save(outPath+foto)
