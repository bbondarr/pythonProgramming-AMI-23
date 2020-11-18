from LinkedList import LinkedList

class FileLogger:
    fn = 'log.txt'
   
    @staticmethod
    def logAdd(former, pos, result):
        with open(FileLogger.fn, 'a') as file:
            file.write('Former LinkedList:'+str(former)+
                    '\nPosition of adding:'+str(pos)+
                    '\nLinkedList with newly added elements:'+str(result)+'\n\n')

    @staticmethod
    def logRemove(former, pos, result):
        with open(FileLogger.fn, 'a') as file:
            if isinstance(pos, list):
                file.write('Former LinkedList:'+str(former)+
                        '\nRange of removing:'+str(pos)+
                        '\nLinkedList with deleted elements:'+str(result)+'\n\n')
            else:
                file.write('Former LinkedList:'+str(former)+
                        '\nPosition of deletion:'+str(pos)+
                        '\nLinkedList without '+str(pos)+'th element:'+str(result)+'\n\n')

    @staticmethod
    def logMethodExecution(former, result):
        with open(FileLogger.fn, 'a') as file:
            file.write('Former LinkedList:'+str(former)+
                    '\nLinkedList after reversing alternations:'+str(result)+'\n\n')

    @staticmethod
    def log(method, former, pos, result=None):
        with open(FileLogger.fn, 'a') as file:
            if method == 'method' and result is None:
                file.write('Former LinkedList:'+str(former)+
                    '\nLinkedList after reversing alternations:'+str(result)+'\n\n')

            elif method == 'remove':
                if isinstance(pos, list):
                    file.write('Former LinkedList:'+str(former)+
                            '\nRange of removing:'+str(pos)+
                            '\nLinkedList with deleted elements:'+str(result)+'\n\n')
                else:
                    file.write('Former LinkedList:'+str(former)+
                            '\nPosition of deletion:'+str(pos)+
                            '\nLinkedList without '+str(pos)+'th element:'+str(result)+'\n\n')

            elif method == 'add':
                file.write('Former LinkedList:'+str(former)+
                        '\nPosition of adding:'+str(pos)+
                        '\nLinkedList with newly added elements:'+str(result)+'\n\n')


