import random
from random import randint
import time
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator

class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        # TODO: Initialize any additional variables here

        # Initialize variables for Q-learning <s, a, r, s'>
        self.state = None
        self.action = None
        self.reward = None
        self.default_Q = 2 # change to lower
        self.last_state = None
        self.last_action = None
        self.last_reward = None
        self.alpha = 1
        self.gamma = .1
        
        self.Q = {} # Q dictionary

    def reset(self, destination=None):
        self.planner.route_to(destination)
        # TODO: Prepare for a new trip; reset any variables here, if required
        self.state = None
        self.action = None
        self.reward = None
        self.last_state = None
        self.last_action = None
        self.last_reward = None
        self.next_waypoint = None

    def update(self, t):
        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)

        # TODO: Update state
        inputs["Waypoint"] = self.next_waypoint
        del inputs['right'] #important for right forward if the is something
        self.state = inputs
        state = tuple(inputs.values())


        # TODO: Select action according to your policy

        #Random Action
        posible_actions = [None, 'forward', 'left', 'right']
    
        #action = random.choice(posible_actions)

        # Execute action and get reward
        reward = self.env.act(self, None)
        best_action = None

        # Set the best action to that which has the best reward
        #for element in posible_actions:
        #    if reward < self.env.act(self, element):
        #        best_action = element
        #        reward = self.env.act(self, element)

        # Initialize all Q values for the state
        Q_vals = []
        for action in posible_actions:
            if (state, action) not in self.Q.keys():
                self.Q[(state, action)] = self.default_Q
            Q_vals.append(self.Q[(state, action)])

        #Find the best action
        # Find max Q value for a particular state. Make into a function. Check highest Q value corresponding to that state
        # that also takes in state

        # USe the state to pick the best action> Initialize best action with some random action
        best_actions = []
        max_Q_val = max(Q_vals)
        for i, val in enumerate(Q_vals):
            if val == max_Q_val:
                best_actions.append(posible_actions[i])

        i = randint(0, len(best_actions) - 1)     
        best_action = best_actions[i]
        Q_val = Q_vals[i]
        #action = best_action
        reward = self.env.act(self, action)

        # TODO: Learn policy based on state, action, reward
       # print "\n The Last : " + str(self.last_state) + "\n"

        if self.last_state != None and self.last_action != None: 
       #     self.Q[ (self.last_state, self.last_action) ] = (1-self.alpha) 
            self.Q[(self.last_state, self.last_action)] = (1-self.alpha) * self.Q[(self.last_state, self.last_action)] + self.alpha * (self.last_reward + self.gamma * (self.Q[(state, action)]))


        self.last_state =  state
        self.last_action = action
        self.last_reward = reward

        print "LearningAgent.update(): deadline = {}, inputs = {}, action = {}, reward = {}".format(deadline, inputs, action, reward)  # [debug]


def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track
    # NOTE: You can set enforce_deadline=False while debugging to allow longer trials

    # Now simulate it
    sim = Simulator(e, update_delay=0, display=False)  # create simulator (uses pygame when display=True, if available)
    # NOTE: To speed up simulation, reduce update_delay and/or set display=False

    sim.run(n_trials=100)  # run for a specified number of trials
    # NOTE: To quit midway, press Esc or close pygame window, or hit Ctrl+C on the command-line


if __name__ == '__main__':
    run()
