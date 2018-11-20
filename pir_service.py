import datetime
import random


class PirService(object):
    def __init__(self):
        self.is_true = None
        self._previous_is_true = None
        self.true_count = 0
        self.false_count = 0
        self.true_from = None
        self.true_to = None
        self.false_from = None
        self.false_to = None

    def poll(self):
        self._previous_is_true = self.is_true
        if random.randint(0, 10) == 0:
            self.is_true = not self.is_true

        utcnow = datetime.datetime.utcnow()

        if self.is_true:
            self.true_to = utcnow
            self.true_count += 1
            if self._previous_is_true:
                # consequetive present
                pass
            else:
                # just entered
                self.false_to = utcnow
                self.true_from = utcnow
                self.false_count = 0
                pass

        else:
            self.false_to = utcnow
            self.false_count += 1
            if self._previous_is_true:
                # just left
                self.true_count = 0
                self.true_to = utcnow
                self.false_from = utcnow
            else:
                # consequetive gone
                pass

    def pir(self):
        self.poll()

        return self.__dict__
