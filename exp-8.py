# -- Exp 8: Monkey Banana Problem 
# Aim: Write a Program to Implement the Monkey Banana Problem using Python. 
# Monkey Banana Problem 
# The Monkey Banana Problem is a classic AI problem where a monkey in a room wants to get a 
# bunch of bananas hanging from the ceiling. The monkey needs to use a chair to reach the 
# bananas by performing a sequence of actions. 
# Problem Statement 
# 1. A monkey is in a room. 
# 2. A chair is present in the room. 
# 3. Bananas are hanging from the ceiling, out of the monkey's reach. 
# 4. The monkey needs to:  
# o Move to the chair. 
# o Push the chair under the bananas. 
# o Climb onto the chair. 
# o Grab the bananas. 
# States and Actions 
# 1. Initial State – Monkey is at a certain location, bananas are hanging, chair is at another 
# location. 
# 2. Goal State – Monkey is holding the bananas. 
# 3. Possible Actions:  
# o Walk to the chair. 
# o Push the chair to the bananas. 
# o Climb onto the chair. 
# o Grab the bananas. 
# Algorithm (Using State Space Search) 
# 1. Define the possible states:  
# o Location of the monkey. 
# o Location of the chair. 
# o Whether the monkey is on the chair. 
# o Whether the monkey is holding the bananas. 
# 2. Define possible actions:  
# o Move 
# o Push 
# o Climb 
# o Grab 
# 3. Use Breadth-First Search (BFS) to explore all possible states. 
# 4. If the state where the monkey holds the bananas is reached → Success! 
# 5. If no state leads to success → Fail. 
 
# SOURCE CODE : 
#   -->
def monkey_banana_problem():
    # Initial state: (Monkey's Location, Chair's Position, Monkey's Position, Monkey's Status)
    initial_state = ('Far-Chair', 'Chair-Not-Under-Banana', 'Off-Chair', 'Empty')
    print(f"\nInitial state is {initial_state}")

    # Goal state
    goal_state = ('Near-Chair', 'Chair-Under-Banana', 'On-Chair', 'Holding')

    # Possible actions and their effects
    actions = {
        "Move to Chair": lambda state: ('Near-Chair', state[1], state[2], state[3])
        if state[0] != 'Near-Chair' else None,

        "Push Chair under Banana": lambda state: ('Near-Chair', 'Chair-Under-Banana', state[2], state[3])
        if state[0] == 'Near-Chair' and state[1] != 'Chair-Under-Banana' else None,

        "Climb Chair": lambda state: ('Near-Chair', 'Chair-Under-Banana', 'On-Chair', state[3])
        if state[0] == 'Near-Chair' and state[1] == 'Chair-Under-Banana' and state[2] != 'On-Chair' else None,

        "Grasp Banana": lambda state: ('Near-Chair', 'Chair-Under-Banana', 'On-Chair', 'Holding')
        if state[0] == 'Near-Chair' and state[1] == 'Chair-Under-Banana' and state[2] == 'On-Chair' and state[3] != 'Holding' else None
    }

    # BFS to explore states
    from collections import deque
    dq = deque([(initial_state, [])])  # Each element is (current_state, actions_taken)
    visited = set()

    while dq:
        current_state, actions_taken = dq.popleft()

        # Check if we've reached the goal
        if current_state == goal_state:
            print("\n✅ Solution Found!")
            print("Actions to achieve goal:")
            for action in actions_taken:
                print(action)
            print(f"Final State: {current_state}")
            return

        # Skip if already visited
        if current_state in visited:
            continue
        visited.add(current_state)

        # Try all possible actions
        for action_name, action_func in actions.items():
            next_state = action_func(current_state)
            if next_state and next_state not in visited:
                dq.append((next_state, actions_taken + [f"Action: {action_name}, Resulting State: {next_state}"]))

    print("❌ No solution found.")

# Run the program
monkey_banana_problem()

