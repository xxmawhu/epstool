import subprocess
import sys
def getBound(fileName):
    commands=['gs', '-dNOPAUSE', '-dBATCH', '-q', '-sDEVICE=bbox']
    commands.append(fileName)
    pr = subprocess.Popen(commands, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    out, err = pr.communicate()
    output = err
    try:
        return output.decode()
    except Expection:
        print("decode fail")
        return output

def changeBound(fileName, newBound=''):
    s=''
    for line in open(fileName, 'r').readlines():
        if "HiResBoundingBox" in line:
            continue
        if "BoundingBox" in line and not "HiResBoundingBox" in line:
            s += newBound
            continue
        s += line
    return s

def main(fileName):
    bound = getBound(fileName)
    s = changeBound(fileName, bound)
    f = open(fileName, 'w')
    f.write(s)
    f.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the eps file:")
        exit(1)
    fileName = sys.argv[1]
    main(fileName)
