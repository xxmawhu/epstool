import subprocess
import sys
import glob


def getBound(fileName):
    commands = ['gs', '-dNOPAUSE', '-dBATCH', '-q', '-sDEVICE=bbox']
    commands.append(fileName)
    pr = subprocess.Popen(commands, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    out, err = pr.communicate()
    output = err
    try:
        return output.decode()
    except Exception:
        print("decode fail {}".format(Exception))
        return output


def changeBound(fileName, newBound=''):
    # print("newBound {}".format(newBound))
    s = ''
    for line in open(fileName, 'r').readlines():
        if "HiResBoundingBox" in line:
            continue
        if "BoundingBox" in line and "HiResBoundingBox" not in line:
            try:
                s += newBound
            except UnicodeDecodeError as e:
                s += str(newBound)
            except Exception as e:
                print(e)
            continue
        s += line
    if "BoundingBox" not in s:
        output = ''
        for line, i in enumerate(s.splitlines()):
            if i == 1:
                try:
                    output += newBound
                except UnicodeDecodeError as e:
                    s += str(newBound)
                except Exception as e:
                    print(e)
                output += line
            else:
                output += line
        return output
    else:
        return s


def main(fileName):
    print("Process {}".format(fileName))
    bound = getBound(fileName)
    s = changeBound(fileName, bound)
    f = open(fileName, 'w')
    f.write(s)
    f.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the eps file:")
        exit(1)
    for fileName in sys.argv[1:]:
        for f in glob.glob(fileName):
            try:
                main(f)
            except Exception as e:
                print(e)
                continue
