
# coding: utf-8

# In[5]:

# Student_Name:  Justin R. Locke
#email:  justinrlocke@gmail.com
#Date: April 15, 2015    
# --------------------------- #
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

example_input ="John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.Bryant is connected to Olive, Ollie, Freda, Mercedes.Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.Mercedes is connected to Walter, Robin, Bryant.Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.Olive is connected to John, Ollie.Olive likes to play The Legend of Corgi, Starfleet Commander.Debra is connected to Walter, Levi, Jennie, Robin.Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.Walter is connected to John, Levi, Bryant.Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.Levi is connected to Ollie, John, Walter.Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.Ollie is connected to Mercedes, Freda, Bryant.Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.Jennie is connected to Levi, John, Freda, Robin.Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.Robin is connected to Ollie.Robin likes to play Call of Arms, Dwarves and Swords.Freda is connected to Olive, John, Debra.Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures.Tester is connected to.Tester likes to play."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a dictionary. 
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   Assume that for all the test cases string input contains  
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
#
# Sample ouput:
#   >>> {
#   >>> 'Freda': (['Olive', 'John', 'Debra'], ['Starfleet Commander', 'Ninja Hamsters', 'Seahorse Adventures']),
#   >>> 'Tester': ([], []), 
#   >>> 'Ollie': (['Mercedes', 'Freda', 'Bryant'], ['Call of Arms', 'Dwarves and Swords', 'The Movie: The Game']), 'Debra': (['Walter', 'Levi', 'Jennie', 'Robin'],
#   >>> ...
#   >>>}

def create_data_structure(string_input):
    network = {}
    # Use 'break_up_string()' procedure to breakup the string 
    # and store in a structured list
    structured_list = breakup_string(string_input)
    #initialize language around string input
    connection_language = "is connected to"
    connection_language_length = len(connection_language)
    game_language = "likes to play"
    game_language_length = len(game_language)
    # For each entry in structure list find User and User's friend
    for block in structured_list:
        
        ########Stores the User from string##########
        # finds the language 'is connected to'
        #block[0] refers too the friend portion of structured list
        connection_location = block[0].find(connection_language)  
        user_name = block[0][:connection_location-1]  # stores user_name

        ########Stores the user's friends from string#########
        # find the portion of string that stores friends
        friend_portion_of_string_start = connection_location+connection_language_length+1        
        friends = block[0][friend_portion_of_string_start:]       
        # if User has friends then parse friends via comma_parse()
        if friends: 
            friends = comma_parse(friends)
        else:   # otherwise store friends as an empty list
            friends = []       
        network[user_name] = friends  # store the friends in name network 
        
        ########Create the User's favorite Games' from string ##########
        ##  block[1] refers too the games portion of structured list
        # find the portion of string that stores games
        game_location = block[1].find(game_language) 
        game_portion_of_string_start = game_location+game_language_length+1
        game = block[1][game_portion_of_string_start:]
        # if User has liked games, then parse games via comma_parse()
        if game:   
             game = comma_parse(game)
        else:
            game = []   # otherwise store friends as an empty list
        network[user_name] = friends,game
    return network


# ----------------------------------------------------------------------------- 
# breakup_string(string_input): 
#   This procedure is used in conjunction with create_data_structure() & comma_parse().
#   It does the initial parsing of a block of text (such as the one above).
#   "breakup_string" takes the initial string and puts into easier to use lists
# 
# Arguments: 
#   string_input: block of text containing the network information
#
# Return: A set of list [ 1 for each user].
#   For each user, their list contain two elements: 
#         the first relates to friends,
#         the second relates to games
# 
#Sample Output:
#   >>> breakup_string(example_input)
#   >>> [['John is connected to Bryant, Debra, Walter',
#   >>> 'John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner'],
#   >>> ['Bryant is connected to Olive, Ollie, Freda, Mercedes',
#   >>> 'Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man'],
#   >>> ....


def breakup_string(string_input):  
    # initialize result list
    result = []
    # initialize a count variable to assist with appending to result
    n = 0
    # as long as a period is period is present continue loop 
    while string_input.find('.') != -1:  
        #finds the first period in the strings
        first_period = string_input.find('.')
        # trims the input string
        first_statement = string_input[:first_period]  
        # puts the first sentence in the list 
        result.append([first_statement]) 
        
        #finds the 2nd period
        second_period = string_input.find('.',first_period+1)
        # puts the 2nd sentence in list
        second_statement = string_input[first_period+1:second_period]
        # appends second statement to the 'nth' entry
        result[n].append(second_statement)
        n += 1
        # trims the string input for the next loop
        string_input = string_input[second_period+1:]
    return result

# ----------------------------------------------------------------------------- 
# comma_parse(string_input): 
#   This procedure is used in conjunction with create_data_structure() & breakup_string().
#   Use this procedure to parse names (or games) from a string that lists friends (or games) with commas as separatorss
# 
# Arguments: 
#   string_input: a string listing friends (or games) with commas as separators
#   Sample input: "Bryant, Debra, Walter"
#
# Return: 
#   Outputs a list of either Friends or games
# 
#Sample Output:
#   >>> comma_parse(Bryant, Debra, Walter)
#   >>> ['Bryant', 'Debra', 'Walter']

def comma_parse(string_of_names):
    # initialize result list
    names = []
    # find the first comma
    comma_location = string_of_names.find(',')
    # if no commas exist then it's either 0 or 1 name/game, so return the inputted string_of_names
    if string_of_names.find(',') == -1:  
        return [string_of_names]         
    # if commas are found then for each comma store the name and append to 'names' output list
    while string_of_names.find(',') != -1:
        name = string_of_names[:comma_location]  # stores a name up to comma location
        names.append(name)   # appends to output list
        string_of_names = string_of_names[comma_location+2:]  # trims the list to next portion of string
        comma_location = string_of_names.find(',')     # finds the next comma
    name = string_of_names[comma_location+1:]  # finds the last name in the list
    names.append(name) # appends to output list
    return names



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
    # This procedure gets the friends of the inputted user
    # Test to see if User is  not in Network
    if user not in network:
        return None
    else:
        return network[user][0]  # returns the list of friends from name_network

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
    # This procedure gets the games that an inputted user likes
    #Test to see if User is in Network 
    if user not in network:
        return None
    return network[user][1] # returns the list of friends from name_network

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
    # Test to see if Users are in Network
    if user_A not in network or user_B not in network:
        return False
    # Pull from friend list of User_A
    friend_list = get_connections(network, user_A)
    games_liked = get_games_liked(network, user_A)
    # if an existing connection with user_B is NOT found in friendlist  
    if user_B not in friend_list:
        #then add the friend to the friend_list
        friend_list.append(user_B)
        # and update the network and return the result 
        network[user_A] = friend_list, games_liked
        return network
    #otherwise the connection already exists, so do nothing and return network
    else:
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
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)


def add_new_user(network, user, games):
    # If User is already in Network then do nothing (return Network unchanged)
    if user in network:
        return network
    # otherwise update network with no friends and list of games liked
    else:
        network[user] = [],games
        return network
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the user we are interested in 
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
    # initialize result list
    result = []
    # Test to see if User is in Network
    if user not in network:
        return None
    # Find immediate friends to user
    friend_list = get_connections(network, user)    
    # Then find secondary connections (i.e. acquaintances) to user
    for friend in friend_list:
        acquaintance_list = get_connections(network, friend)
        # for each acquaintance, 
        for acquaintance in acquaintance_list:
            #check to see if is not already in result 
            if acquaintance not in result:
                # then append acquitance to result
                result.append(acquaintance)
    return result

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
    # initialize result list
    result = []
    # Test to see if Users are in Network
    if user_A not in network or user_B not in network:
        return False
    # Find User's Connections
    user_A_connections = get_connections(network,user_A)
    user_B_connections = get_connections(network,user_B)
    # Test if User A's connections is in User B's Connection
    for user_A_friend in user_A_connections:
        if user_A_friend in user_B_connections:
            result.append(user_A_friend)
    # return number of connections in integer
    return len(result)

# ----------------------------------------------------------------------------- 
# path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B (is not necessarilyt the shortest path)
#  *Note procedures used within path_to_friends are procedures:
#       1) recursive_dfs()
#       2) find_previous_node()
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

def path_to_friend(network, user_A, user_B, visited = None):
    # test default parameter, if None then set empty, otherwise use visited from recursive case
    if visited == None:
        visited = []
    # test to see if both User_A and User_B are in network
    if user_B in network and user_A in network:
        #find the friends of User_A
        friends = get_connections(network, user_A)
        # keep track of nodes visited 
        visited.append(user_A) 
        # set the path starting from User_A
        path = [user_A]
        ##### BASE  case ############ 
        # if User_B is in User_A's friend append to result and return
        if user_B in friends:
            path.append(user_B)
            return path
        ##### RECURSIVE case  ############
        else:
            for friend in friends: # for each friend in User_A's friend list
                if friend not in visited:  # if friend hasn't already been visited
                    # do recusive call storing in 'recursed_path'
                    recursed_path = path_to_friend(network, friend, user_B, visited)
                    # if Recursed_path has contents in it then update and return path 
                    if recursed_path: 
                        path = path + recursed_path
                        return path   
                    # otherwise if recursed_path is empty then continue through for loop until either result or none is found        
            return None # No connection was found between users
    return None # one of the users not in network

    
# Make-Your-Own-Procedure (MYOP)
# game_popularity_tally
# ----------------------------------------------------------------------------- 
# This procedure tallies the total count of games liked in the network.
# This procedure allows individuals to see most popular and least popular games
# in the network
#
# Arguments:
#   network: The network you created with create_data_structure. 
# Return:
#   A dictionary showing all games liked in the network (displayed as a key), 
#  along with a value indicating the number of times the game was like
#
# Sample output:
#   >>> print game_popularity_tally(net)
#   >>> {'Call of Arms': 3,
#   >>>'City Comptroller: The Fiscal Dilemma': 2,
#   >>>'Dinosaur Diner': 2,
#   >>>'Dwarves and Swords': 3,
#   >>>'Ninja Hamsters': 2,
#   >>>'Pirates in Java Island': 2,
#   >>>'Seahorse Adventures': 3,
#   >>>'Seven Schemers': 2,
#   >>>'Starfleet Commander': 2,
#   >>>'Super Mushroom Man': 3,
#   >>>'The Legend of Corgi': 4,
#   >>>'The Movie: The Game': 2}
#   This implies 'The Lengend of Corgi' is the most popular game

def game_popularity_tally(network):
    # Initialize variables for final result
    game_popularity_tally = {}
    for user in network:
        user_games = get_games_liked(network,user)
        for game in user_games:
            if game not in game_popularity_tally:
                game_popularity_tally[game] = 1
            else:
                game_popularity_tally[game] = game_popularity_tally[game] + 1
    return game_popularity_tally



# In[ ]:




# In[ ]:



