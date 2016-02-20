import collections
import random


class Passenger(object):
    """
    A Passenger has a ticketed seat, a rank, and the seat they are in
    """
    def __init__(self, ticketed, rank):
        self.ticketed = ticketed
        self.rank = rank
        self.seat = None


def make_passengers(n=100):
    tickets = [i for i in range(1,n+1)]
    random.shuffle(tickets)
    return [Passenger(ticket, rank) for rank, ticket in enumerate(tickets)]


def choose_random_seat(seats):
    (seat,) = random.sample(seats, 1)
    seats.remove(seat)
    return seat


def simulate(passengers):
    n = len(passengers)
    seats = set([i for i in range(1, n+1)])
    for index, passenger in enumerate(passengers):
        if passenger.rank == 1:
            passenger.seat = choose_random_seat(seats)
        else:
            if passenger.ticketed in seats:
                passenger.seat = passenger.ticketed
            else:
                passenger.seat = choose_random_seat(seats)
    last_passenger = passengers[-1]
    return last_passenger.seat == last_passenger.ticketed


def main():
    sims = 1000
    for i in range(1,101):
        c = collections.Counter()
        for j in range(0,sims):
            passengers = make_passengers(i)
            result = simulate(passengers)
            c[result] += 1
        print(c[False]*1.0/sims)


if __name__ == "__main__":
    main()
