states={
    "start":{"forward":("forest",0)},
    "forest":{"forward":("cave",5)},
    "cave":{"forward":("treasure",10)},
    "treasure":()
}

gamma=0.9

V = {state: 0 for state in states}

def compute_value():
    reverse_state=list(states.keys())[::-1]
    for state in reverse_state:
        if state=="treasure":
            V[state]=0
        else:
            action="forward"
            next_state,reward=states[state][action]
            V[state]=reward+gamma*V[next_state]

compute_value()
print("=== Bellman Equation Demo ===")
for state, value in V.items():
    print(f"V({state}) = {value:.2f}")