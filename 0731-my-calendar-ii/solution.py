from sortedcontainers import SortedDict

class MyCalendarTwo:
    def __init__(self):
        # SortedDict maintains keys in sorted order
        # Keys represent time points, values represent the change in number of bookings
        # Positive value: booking starts, Negative value: booking ends
        self.booking_events = SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:
        """
        Attempts to book a time slot from startTime to endTime.
        Returns True if booking is successful (no triple booking), False otherwise.

        Args:
            startTime: The start time of the booking (inclusive)
            endTime: The end time of the booking (exclusive)

        Returns:
            bool: True if booking successful, False if it would cause triple booking
        """
        # Add the new booking tentatively
        # Increment counter at start time (booking begins)
        self.booking_events[startTime] = self.booking_events.get(startTime, 0) + 1
        # Decrement counter at end time (booking ends)
        self.booking_events[endTime] = self.booking_events.get(endTime, 0) - 1

        # Check if this causes triple booking by scanning through all time points
        current_bookings = 0
        for booking_change in self.booking_events.values():
            current_bookings += booking_change

            # If at any point we have more than 2 concurrent bookings
            if current_bookings > 2:
                # Revert the tentative booking
                self.booking_events[startTime] -= 1
                self.booking_events[endTime] += 1

                # Clean up: remove entries with 0 value to keep dictionary clean
                if self.booking_events[startTime] == 0:
                    del self.booking_events[startTime]
                if self.booking_events[endTime] == 0:
                    del self.booking_events[endTime]

                return False

        # Booking successful - no triple booking detected
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime, endTime)
