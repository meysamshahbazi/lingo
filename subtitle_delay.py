import sys


def main(argv):
    file = argv[1]
    print("openeing file: ",file)
    with open(file) as f:
        lines = f.readlines()

    with open(file[:-4]+"_DELAYED.srt","w") as f:
        for l in lines:
            if "-->" in l:
                end = l.split(" --> ")[1][:-1]
                end_second = int(end.split(',')[0].split(":")[2])
                new_line = end+" --> "+end[:6]+str(end_second+2)+"\n"
            else:
                new_line = l
            f.write(new_line)


if __name__ == "__main__":
   main(sys.argv)
