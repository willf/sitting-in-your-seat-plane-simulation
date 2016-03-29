import collections
import random


"""
There’s an airplane with 100 seats, and there are 100 ticketed passengers each
with an assigned seat. They line up to board in some random order. However, the
first person to board is the worst person alive, and just sits in a random
seat, without even looking at his boarding pass. Each subsequent passenger sits
in his or her own assigned seat if it’s empty, but sits in a random open seat
if the assigned seat is occupied. What is the probability that you, the
hundredth passenger to board, finds your seat unoccupied?
"""


class Passenger(object):
    """
    A Passenger has a ticketed seat, a rank, and the seat they are in
    """

    def __init__(self, ticketed, rank):
        self.ticketed = ticketed
        self.rank = rank
        self.seat = None

    def __repr__(self):
        return "Passenger: ticketed: %s, rank: %s, seat: %s" % (
            self.ticketed, self.rank, self.seat)


def make_passengers(n=100):
    tickets = [i for i in range(1, n + 1)]
    random.shuffle(tickets)
    return [Passenger(ticket, rank + 1) for rank, ticket in enumerate(tickets)]


def choose_random_seat(seats):
    (seat, ) = random.sample(seats, 1)
    new_seats = seats - set([seat])
    return (seat, new_seats)


def simulate(passengers):
    n = len(passengers)
    seats = set([i for i in range(1, n + 1)])
    for index, passenger in enumerate(passengers):
        if passenger.rank == 1:
            passenger.seat, seats = choose_random_seat(seats)
        else:
            if passenger.ticketed in seats:
                passenger.seat = passenger.ticketed
                seats = seats - set([passenger.seat])
            else:
                passenger.seat, seats = choose_random_seat(seats)
    last_passenger = passengers[-1]
    return last_passenger.seat == last_passenger.ticketed


def main():
    sims = 10000
    size = 100
    c = collections.Counter()
    for j in range(0, sims):
        passengers = make_passengers(size)
        result = simulate(passengers)
        c[result] += 1
    print(c[False] * 1.0 / sims)


if __name__ == "__main__":
    main()
