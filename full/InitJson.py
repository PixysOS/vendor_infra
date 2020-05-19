from PIL import Image

# Get the size of wallpaper
def getRes(fname):
    image = Image.open("{0}.png".format(fname))
    w, h = image.size
    return "{0}x{1}".format(w,h)


# Create an initial JSON file from the provided images.
# TODO: Add categories too.(Team discussion required)
if __name__ == "__main__":
    json = open("wallpapers.json", "w")
    json.write("{\n    \"wallpapers\": [\n")
    for id in range(0,17):
        json.write("        {\n")
        json.write("            \"id\": {0},\n".format(id))
        json.write("            \"urlFull\": \"https://raw.githubusercontent.com/PixysOS/vendor_infra/master/full/{0}.png\",\n".format(id))
        json.write("            \"urlPreview\": \"https://raw.githubusercontent.com/PixysOS/vendor_infra/master/small/{0}.png\",\n".format(id))
        json.write("            \"category\": \"\",\n")
        json.write("            \"resolution\": \"{0}\"\n".format(getRes(id)))
        json.write("        }")
        if id != 16:
            json.write(",\n")
        else:
            json.write("\n")
    json.write("    ]\n}")
    json.close()
