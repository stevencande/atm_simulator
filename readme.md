#ATM Simulator

#The problem is about designing an ATM simulator that handles deposits and withdrawals using 5 banknote denominations: $20, $50, $100, $200, and $500. The ATM must always prioritize larger denominations first when withdrawing money. If it can't fulfill the exact amount using that strategy, it rejects the withdrawal entirely.

You have to implement:

A method to deposit banknotes,

A method to withdraw a given amount, returning the exact combination of banknotes used, or [-1] if it's not possible.

The challenge lies in simulating real-world ATM behavior where greedy choices (largest denominations first) can prevent withdrawals even when enough smaller bills exist — because the machine doesn't backtrack.

The ATM uses a greedy algorithm — it always picks the largest available denomination first. If that choice leads to a dead end, it doesn’t try smaller combinations (i.e., it doesn’t backtrack or optimize for alternative solutions).

