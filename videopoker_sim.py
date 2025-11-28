from itertools import combinations
from collections import Counter
import math
import time

# -------------------------------------------------
# 1. Paytable (9/6 Jacks or Better)
# -------------------------------------------------
paytable = {
    "royal_flush":       800,
    "straight_flush":     50,
    "four_kind":          25,
    "full_house":          9,
    "flush":               6,
    "straight":            4,
    "three_kind":          3,
    "two_pair":            2,
    "jacks_or_better":     1,
    "nothing":             0,
}

# -------------------------------------------------
# 2. Rank mapping
# -------------------------------------------------
rank_map = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14
}

# -------------------------------------------------
# 3. Full deck
# -------------------------------------------------
ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
suits = ["d","h","c","s"]
deck = [r + s for r in ranks for s in suits]

# -------------------------------------------------
# 4. Hand evaluator (returns payout)
# -------------------------------------------------
def evaluate_five(cards):
    ranks = [rank_map[c[:-1]] for c in cards]
    suits_list = [c[-1] for c in cards]
    rank_counts = Counter(ranks)
    count_values = sorted(rank_counts.values(), reverse=True)
    sorted_ranks = sorted(ranks, reverse=True)

    is_flush = len(set(suits_list)) == 1
    is_straight = (max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5) or \
                  set(ranks) == {14, 5, 4, 3, 2}

    if is_flush and set(ranks) == {14, 13, 12, 11, 10}:
        return 800
    if is_flush and is_straight:
        return 50
    if count_values == [4, 1]:
        return 25
    if count_values == [3, 2]:
        return 9
    if is_flush:
        return 6
    if is_straight:
        return 4
    if count_values == [3, 1, 1]:
        return 3
    if count_values == [2, 2, 1]:
        return 2
    if count_values == [2, 1, 1, 1]:
        for r, cnt in rank_counts.items():
            if cnt == 2 and r >= 11:
                return 1
    return 0

# -------------------------------------------------
# 5. PRECOMPUTE ALL 2,598,960 HANDS
# -------------------------------------------------
print("Precomputing all 2,598,960 hands...")
start = time.time()

all_hands = list(combinations(deck, 5))
hand_to_payout = {}

for hand in all_hands:
    payout = evaluate_five(list(hand))
    hand_tuple = tuple(sorted(hand))  # canonical form
    hand_to_payout[hand_tuple] = payout

print(f"Precompute done in {time.time() - start:.1f} seconds.")
print(f"Unique hands stored: {len(hand_to_payout):,}")

# -------------------------------------------------
# 6. Precompute draw combinations per hold count
# -------------------------------------------------
draw_combos = [math.comb(47, 5 - held) for held in range(6)]  # index = held count

# -------------------------------------------------
# 7. Best strategy using LOOKUP (WOO style)
# -------------------------------------------------
def best_strategy_woo(hand, remaining):
    best_ev = 0.0
    best_held = []

    for mask in range(1, 32):  # skip hold 0
        held = [hand[i] for i in range(5) if (mask & (1 << i))]
        held_count = len(held)
        to_draw = 5 - held_count

        if to_draw == 0:
            ev = evaluate_five(hand)
        else:
            total_pay = 0
            combos = 0
            for draw in combinations(remaining, to_draw):
                final_hand = tuple(sorted(held + list(draw)))
                total_pay += hand_to_payout.get(final_hand, 0)
                combos += 1
            ev = total_pay / draw_combos[held_count]

        if ev > best_ev:
            best_ev = ev
            best_held = held

    return best_held, best_ev

# -------------------------------------------------
# 8. MAIN: Fast simulation
# -------------------------------------------------
NUM_DEALS = 100
total_ev = 0.0

print(f"\nSimulating {NUM_DEALS} deals...\n")

for deal in range(NUM_DEALS):
    # Fresh deck
    from random import shuffle
    fresh_deck = deck[:]
    shuffle(fresh_deck)
    hand = fresh_deck[:5]
    remaining = fresh_deck[5:]

    hold_cards, ev = best_strategy_woo(hand, remaining)
    total_ev += ev

    if deal < 10:
        print(f"Deal {deal+1:3}: Hand {hand}  →  Hold {hold_cards}  EV = {ev:.4f}")

print("\n" + "="*60)
print(f"Average EV over {NUM_DEALS} deals: {total_ev / NUM_DEALS:.6f}")
print(f"Time: {time.time() - start:.1f} seconds total")
print("="*60)