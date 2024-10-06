import datetime, asyncio
from threading import Timer

class TimerRunningError(Exception):
    """Is thrown when a timer is already running"""
    def __init__(self, *args):
        super().__init__("Timer already running")
        pass

class InvalidType(TypeError):
    "Raised if object type is not a valid Time Instance"
    def __init__(self, *args):
        super().__init__("Invalid type")
        pass
    

class SetInterval:
    def __init__(self, interval: int, function):
        self.ticks = 0
        self.interval = interval
        self.function = function
        self._timer: Timer = None
        self.is_cancelled = False
    
    def begin(self):
        if not self._timer is None: raise TimerRunningError()
        self.start_internal_counter()

    def start_internal_counter(self):
        self.function()
        self._timer = Timer(self.interval, self.start_internal_counter)
        self.ticks = self.ticks + 1
        self._timer.start()

    def cancel(self):
        if self._timer is None: return
        self.ticks = 0
        self._timer.cancel()
        self._timer = None
    
    def __del__(self):
        self.cancel()

class Time:
    """
    Creates a time object limited to days, hours, minutes and seconds.
    """

    def __init__(self, second=0, minute=0, hour=0, day=0):
        self.second = second
        self.minute = minute
        self.hour = hour
        self.day = day
        self._tick_timer = None
        self.rework_time()
        self.end_tick()

    def tick(self, keep=False, func=None, *args, **kwargs):
        if isinstance(self._tick_timer, SetInterval): return
        def _tick():
            self.second += 1
            if func is not None: func(*args, **kwargs)

        if keep:
            self._tick_timer = SetInterval(1, _tick)
            self._tick_timer.begin()
            
        else:
            self.second += 1
            self.rework_time()
    
    def end_tick(self):
        if isinstance(self._tick_timer, SetInterval):
            self._tick_timer.cancel()
            self._tick_timer = None

    def to_time(self) -> datetime.time:
        return datetime.time(self.hour, self.minute, self.second)

    def to_seconds(self):
        ts = self.second + \
            (self.minute * 60) + \
            (self.hour * 60 * 60) + \
            (self.day * 24 * 60 * 60)
        return ts
    
    def to_minutes(self):
        return self.to_seconds() // 60

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
        "Does not contain support for month or year.. So only the day is returned"
        day = datetime.datetime.now().timetuple().tm_yday - date.timetuple().tm_yday
        return Time(date.second, date.minute, date.hour, day)

    def __gt__(self, target):
        if isinstance(target, int): return self.to_seconds() > target
        if isinstance(target, Time): return self.to_seconds() > target.to_seconds()
        raise InvalidType()
        
        
    def __ge__(self, target):
        if isinstance(target, int): return self.to_seconds() >= target
        if isinstance(target, Time): return self.to_seconds() >= target.to_seconds()
        raise InvalidType()
        
    def __lt__(self, target):
        if isinstance(target, int): return self.to_seconds() < target
        if isinstance(target, Time): return self.to_seconds() < target.to_seconds()
        raise InvalidType()
    
    def __le__(self, target):
        if isinstance(target, int): return self.to_seconds() <= target
        if isinstance(target, Time): return self.to_seconds() <= target.to_seconds()
        raise InvalidType()

    def __add__(self, target):
        if isinstance(target, int): return Time.from_seconds(self.to_seconds() + target)
        if isinstance(target, Time): return Time.from_seconds(self.to_seconds() + target.to_seconds())
        raise InvalidType()

    def __sub__(self, target):
        if isinstance(target, int): return Time.from_seconds(self.to_seconds() - target)
        if isinstance(target, Time): return Time.from_seconds(self.to_seconds() - target.to_seconds())
        else:raise InvalidType()
    
    def __eq__(self, target) -> bool:
        if isinstance(target, int): return self.to_seconds() == target
        if isinstance(target, Time): return self.to_seconds() == target.to_seconds()
        raise InvalidType()

    def __str__(self, *args):
        return f"{self.day} day{ 's' if self.day < 1 or self.day > 1 else ''}, {str(self.hour).rjust(2, '0')}:{str(self.minute).rjust(2, '0')}:{str(self.second).rjust(2, '0')}\n"

    def __div__(self, num):
        if isinstance(num, Time):
            Time.from_seconds(self.to_seconds()/num)
        elif isinstance(num, int):
            return Time.from_seconds(self.to_seconds()/num)
        else: raise ValueError
            
if __name__ == "__main__":
    print(Time.now())