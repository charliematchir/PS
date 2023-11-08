class MyCalendar(object):

    def __init__(self):
        self.bookings = []

    def book(self, start, end):
        l, r = 0, len(self.bookings)
        while l < r:
            mid = (l + r) // 2
            if self.bookings[mid][0] <= start:
                l = mid + 1
            else:
                r = mid

        if self.intersect(l, start, end):
            return False
        else:
            self.bookings.insert(l, [start, end])

        return True

    def intersect(self, i, start, end):
        return (self.bookings[i - 1][1] > start if i >= 1 else False) or (
            self.bookings[i][0] < end if i < len(self.bookings) else False)