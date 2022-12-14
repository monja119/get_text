import os


class Cutter:
    def __init__(self, name, image, col, row):
        # path
        # creation un nouveau chémin
        cd = "cd {}".format(os.getcwd())
        new_dir = name
        make_dir = "mkdir {}".format(new_dir)

        # image source
        type = image.split(".")[-1]
        splitting = "{} {}".format(col, row)
        larges = "--load-large-images"

        # commanding
        copy = "copy {} {}".format(image, new_dir)
        cmd = [cd, make_dir, copy, "cd {} & rename {} {}.{}  & split-image {}.{} {} {}".format(new_dir, image, name, type, name, type, splitting, larges)]

        # launching
        for i in range(1, len(cmd)):
            print(os.system(cmd[i]))

        print(os.getcwd())


