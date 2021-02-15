from strategies.Strategy import Strategy

class ReadFileStrategy(Strategy):
    def __init__(self):
        pass

    def execute(self, lst, pos, fn):
        with open(fn) as file:
            lstString = file.readline()

        lstString = lstString.split(' ')
        subLst = []
        try: 
            for num in lstString:
                subLst.append(int(num))
        except ValueError:
            raise ValueError('Invalid data in read file')

        for i in range(pos, pos+len(subLst)):
            lst.insert(i, subLst[i-pos])

        return lst

    def getName(self):
        return 'readfile'   