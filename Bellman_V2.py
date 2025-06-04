states=[]
values={}

num_states=int(input("enter how many number of state:"))
for i in range(num_states):
    state_name=input(f"Enter state name {i+1}:")
    states.append(state_name)
    values[state_name]=0

terminal_state=input("Enter terminal state eg 'cave':")

transition={}
for state in states:
    if state==terminal_state:
        continue
    print(f"\n form state '{state}'to")
    next_state=input(" the naxt state:- ")
    reward=float(input("Enter the reward of that states:-"))
    transition[state]=(next_state,reward)
    
gamma=float(input("Enter the discount factor:-"))

iteration=int(input("Enter how many iteration:-"))
for state in states:
        if state == terminal_state:
            values[state] = 0  # Always 0 for terminal
        else:
            next_state, reward = transition[state]
            values[state] = reward + gamma * values[next_state]

print("\n--- Final State Values ---")
for state in states:
    print(f"Value of {state} = {values[state]:.2f}")
