import datetime
from threading import Timer
from niceprint import SetInterval

class TimerRunningError(Exception):
    """Is thrown when a timer is already running"""
    
    def __init__(self, *args):
        super().__init__("Timer already running")
        pass
    
class Time:
    """
    Creates a time object limited to days, hours, minutes and seconds.
    """

    def __init__(self, second=0, minute=0, hour=0, day=0):
        self.second = second
        self.minute = minute
        self.hour = hour
        self.day = day
        self._timers = []
        self._tick_timer = None
        self.rework_time()

    def __del__(self):
        for tm in self._timers:
            if isinstance(tm, Timer):
                try:
                    tm.cancel()
                except:
                    pass

    def tick(self, keep=False, func=None):
        if isinstance(self._tick_timer, SetInterval):
            return

        def _tick(self):
            self.second += 1
        if keep:
            tm = SetInterval(1, _tick, [self])
            self._tick_timer = tm
            self._timers.append(tm)
            if func is not None:
                func()
        else:
            self.second += 1
            self.rework_time()

    def to_datetime(self):
        return datetime.time(self.hour, self.minute, self.second)

    def to_seconds(self):
        ts = self.second + \
            (self.minute * 60) + \
            (self.hour * 60 * 60) + \
            (self.day * 24 * 60 * 60)
        return ts

    def rework_time(self):
        seconds = self.to_seconds()
        self.day = seconds//(24*60*60)
        self.hour = seconds//(60*60) % 24
        self.minute = (seconds//60) % 60
        self.second = seconds % 60

    @staticmethod
    def now():
        return Time.from_datetime(datetime.datetime.now())

    @staticmethod
    def from_seconds(seconds: int):
        day = int(seconds//(24*60*60))
        hour = int(seconds//(60*60) % 24)
        mins = int((seconds//60) % 60)
        secs = int(seconds % 60)
        return Time(secs, mins, hour, day)

    @staticmethod
    def from_datetime(date: datetime.datetime):
        "Does not contain month or year.. So only the day is returned"
        day = datetime.datetime.now().timetuple().tm_yday - date.timetuple().tm_yday
        return Time(date.second, date.minute, date.hour, day)

    def __gt__(self, obj):
        return self.to_seconds() > obj.to_seconds()
        
    def __ge__(self, obj):
        return self.to_seconds() >= obj.to_seconds()
        
    def __lt__(self, obj):
        return self.to_seconds() < obj.to_seconds()
    def __le__(self, obj):
        return self.to_seconds() <= obj.to_seconds()

    def __add__(self, obj):
        secs = self.to_seconds() + obj.to_seconds()
        return Time.from_seconds(secs)

    def __sub__(self, obj):
        secs = self.to_seconds() - obj.to_seconds()
        return Time.from_seconds(secs)

    def __str__(self, *args):
        return f"{self.day} day{ 's' if self.day < 1 or self.days > 1 else ''}, {str(self.hour).rjust(2, '0')}:{str(self.minute).rjust(2, '0')}:{str(self.second).rjust(2, '0')}\n"

    def __div__(self, num):
        if type(num) != int:
            raise ValueError
        else:
            return Time.from_seconds(self.to_seconds()/num)
            
if __name__ == "__main__":
    print(Time.now())