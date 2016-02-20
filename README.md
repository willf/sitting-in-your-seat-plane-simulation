# sitting-in-your-seat-plane-simulation
Simulation of 538 "Will Someone Be Sitting In Your Seat On The Plane?" riddle

The Riddle:

There’s an airplane with 100 seats, and there are 100 ticketed passengers each with an assigned seat. 
They line up to board in some random order. However, the first person to board is the worst person alive, 
and just sits in a random seat, without even looking at his boarding pass. Each subsequent passenger 
sits in his or her own assigned seat if it’s empty, but sits in a random open seat 
if the assigned seat is occupied. What is the probability that you, 
the hundredth passenger to board, finds your seat unoccupied?

Based on lots of runs, it's around 3%.

If there are _n_ seats, it looks like the liklihood follows a power law falloff, base on running
the numbers from 1 to 100 seats.
