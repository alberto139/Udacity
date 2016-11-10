import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator
from collections import defaultdict

class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'black'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        self.valid_actions = Environment.valid_actions

        # Intializing previous action, state, reward.
        self.prev_action = None
        self.prev_state = None
        self.prev_reward = None
        
        #initialize the Q_table
        self.Q = {}

        #Parameters for Q-Learning
        self.alpha = 0.85  #learning rate
        self.gamma = 0.45  # discount rate
        self.epsilon = 0.001 #exploration rate
        self.default_Q = 10

    def reset(self, destination=None):
        self.planner.route_to(destination)
        # TODO: Prepare for a new trip; reset any variables here, if required
        self.state = None
        self.next_waypoint = None
        self.prev_action = None
        self.prev_state = None
        self.prev_reward = None

    def update(self, t):
        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)

        #Update inputs to include all relevant variables (next_waypoint, status, light, left)
        inputs['waypoint'] = self.next_waypoint
        del inputs['right']

        #Convert dictionary values of inputs into tuple to reflect state
        self.state = inputs
        state = tuple(inputs.values())
        
        # TODO: Select action according to your policy
        best_action = None
        
        #Exploration
        if random.random() <= self.epsilon: # If random is less than 0.001
            best_action = random.choice(self.valid_actions)
            if (state, best_action) not in self.Q.keys():
                self.Q[(state, best_action)] = self.default_Q
            Q_value = self.Q[(state, best_action)] # Set the q values of the state to
        
        else:
            Q_values = []
            for action in self.valid_actions:
                if (state, action) not in self.Q.keys():
                    self.Q[(state, action)] = self.default_Q
                Q_values.append(self.Q[(state, action)])

            #Find best_action and Q_value
            max_Q = max(Q_values)
            index = []
            for i, x in enumerate(Q_values):
                if x == max(Q_values):
                    index.append(i)
            i = random.choice(index)
            best_action = self.valid_actions[i]
            Q_value = Q_values[i]

        # Execute action and get reward
        action = best_action
        reward = self.env.act(self, action)

        # TODO: Learn policy based on state, action, reward
        if self.prev_state != None:
            self.Q[(self.prev_state,self.prev_action)] = (1-self.alpha)*self.Q[(self.prev_state,self.prev_action)] + self.alpha*(self.prev_reward + self.gamma*(self.Q[(state, action)]))

        #Update previous state, action, and reward
        self.prev_action = action
        self.prev_state = state
        self.prev_reward = reward

        print "LearningAgent.update(): deadline = {}, inputs = {}, action = {}, reward = {}".format(deadline, inputs, action, reward)  # [debug]


def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track
    # NOTE: You can set enforce_deadline=False while debugging to allow longer trials

    # Now simulate it
    sim = Simulator(e, update_delay=0.0000001, display=True)  # create simulator (uses pygame when display=True, if available)
    # NOTE: To speed up simulation, reduce update_delay and/or set display=False

    sim.run(n_trials=1)  # run for a specified number of trials
    # NOTE: To quit midway, press Esc or close pygame window, or hit Ctrl+C on the command-line




if __name__ == '__main__':
    run()

