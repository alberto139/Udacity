#--------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#
# For students who have subscribed to the course,
# please read the submission instructions in the Instructor Notes below.
# ----------------------------------------------------------------------------- 

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
# 
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
# 
# Note that each sentence will be separated from the next by only a period. There will 
# not be whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not 
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure
def create_data_structure(string_input):            
    dot_position = string_input.find('.')
    network = {}
    start = 0
    while dot_position != -1:
        connections = string_input[start:dot_position]
        likes = string_input[dot_position+1:string_input.find('.', dot_position+1)]
        # Connections and likes are extracted and separated from the string_input
        put_in_network(network, connections, likes) 
        # put_in_network is a helper function that update dictionary
        start = string_input.find('.', dot_position+1) + 1
        # Update start to be after the current dot_position
        dot_position = string_input.find('.', start+1)
        # Update dot_position to be after the new start position.
    return network

# Helper function that takes the connections and likes strings from create_data_structure(string_input)
# and further extracts the useful information such as the name of the users and games, then
# puts them in the dictionary network
def put_in_network(network, connections, likes):    

    user = connections[0:connections.find(' ')]
    connections = connections[connections.find(' to ')+len(' to '):].split(', ')
    # connections is assigned the part of the string after ' to ', we must add the length of ' to '
    # in order to get the position at the end of ' to ' instead of the beginning of it 
    likes = likes[likes.find(' play ')+len(' play '):].split(', ')
    # similarly to what was done in connections, we must do the same but with the string ' play '
    
    network[user] = (connections, likes)
    return network

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(network, user):  
    if user not in network:
        return None               
    return network[user][0]

# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user):   
    if user not in network:
        return None               
    return network[user][1]

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):  
    if user_A not in network or user_B not in network:
        return False
    
    connection_list = get_connections(network, user_A)
    if user_A in network and user_B in network:
        if user_B in connection_list:
            return network
        else:
            connection_list.append(user_B)
            
    return network


# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#             ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):             
    if user in network:
        return network
    else:
        network[user] = ([],games)  
    return network
        
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):       
    secondary_connections = []
    connection_list = get_connections(network, user)
    if user not in network:
        return None
    elif not network[user][0]:
        return []
    # If the user has no connections then and empty list is returned
    
    else: 
        for connection in connection_list:
        # Goes trough each connection for the given user
            for secondary in network[connection][0]:
            # Goes trough each connection (secondary) for the connection of the given user
                if secondary not in secondary_connections:
                    secondary_connections.append(secondary)
                  
    return secondary_connections

# -----------------------------------------------------------------------------     
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def connections_in_common(network, user_A, user_B): 
    if user_A not in network or user_B not in network:
        return False
    connection_list_A = get_connections(network, user_A)
    connection_list_B = get_connections(network, user_B)
    result = 0
    for connection in connection_list_A:    # For each connection in user_A
        if connection in connection_list_B: # check if the connection is in user_B
            result += 1                      # if so, increment result by one
    return result

# ----------------------------------------------------------------------------- 
# path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.
def path_to_friend(network, user_A, user_B):
    checked = []                                        #checked will be used to keep track of users already 
    return find_path(network, user_A, user_B, checked)  # by the recursive helper function

# find_path(network, user_A, user_B, checked): is a helper function that does what
# is described for path_to_friend but takes and extra argument checked
def find_path(network, user_A, user_B, checked):
    if user_A not in network or user_B not in network:
        return None  
    result = [user_A]
    connection_list = get_connections(network, user_A)
    for connection in connection_list:               # For each connection in the given user
        if connection == user_B:                        # check if it is the user we are looking for
            result.append(connection)                   # If it is, append to result and return it
            return result
        elif connection not in checked:                             # If the connection is a checked user the loop will continue
            checked.append(connection)                              # to check the next connection for the given user
            path = find_path(network, connection, user_B, checked)  # If the user is not in checked, it will be added to checked
            if path != None:                                        # and the function will be called recursively with connection as the starting user
                return result + path             # If path which a given connection return None, then the loop should continue with the next connection in user
    return None                                         # If there are no more connections to loop, the path does not exist, None is returned

            
            


# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# liked_list(network): 
# Takes the network created by create_data_structure(string_input) then 
# calculates how many likes each game has and returns an ordered list of each game and
# how many people in the network like it.

def liked_list(network):
    # The games will be stored as keys in the dictionary games_list and the values will be the number
    # of users that like the game
    games_list = {}
    like_list = get_games_liked(network, user_A)
    #Go through every user in the given network
    for user in network:
        #Go through every game in every user
        for game in like_list:
            if game not in games_list:
            # If the game is not in the games_list dictionary, it is appearing for the first time,
            # so it is added to the dictionary with value 1 (as in one like)
                games_list[game] = 1
            else:
            # If the game is in the games_list dictionary then the value of the game is increased by one
                games_list[game] += 1
    # The built-in function sorted() will be used to make a new list form the elements in games_list
    sorted_list = sorted(games_list.items(), key=lambda games_list:games_list[1], reverse = True)
    return sorted_list

network = create_data_structure(example_input)