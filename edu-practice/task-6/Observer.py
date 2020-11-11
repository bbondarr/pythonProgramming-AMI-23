from Validation import Validation as v

class Observer:
    listeners = dict()

    @staticmethod
    def attach(key, method):
        Observer.listeners[key] = method

    # Not using it in code, but in case of emergency...
    @staticmethod
    def detach(key):
        Observer.listeners.pop(key)


class Event:
    @staticmethod
    def update(key, former, pos, result=None):
        for l in Observer.listeners:
            if key == l:
                if result is not None:
                    Observer.listeners[l](former, pos, result)
                else:
                    Observer.listeners[l](former, pos)
                break

