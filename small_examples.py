from typing import List


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    new_guests = 0
    S.append(N + 1)
    seats = sorted(S)
    prev_seat = 0
    for seat in seats:
        available_seats = seat - prev_seat - 1
        prev_seat = seat
        for i in range(available_seats):
            if available_seats >= K + K + 1:
                new_guests += 1
                available_seats -= 1
                i += K
            else:
                break
    return new_guests
