###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict

def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    def all_in(status):
        for i in range(len(status)):
            if (status[i] == 0):
                return False
        return True

    def summed(list, cows):
        sum = 0
        for i in cows:
            if i in list:
                sum = sum + cows[i]
        return sum
    
    all_trips = []
    cows_sort = sorted(cows.items(), key = lambda c:(c[1], c[0]), reverse = True)
    print(cows_sort)
    status = [0]*len(cows)

    while(not(all_in(status))):
        this_trip = []
        j = 0
        for i,k in cows_sort:
            if(status[j] == 0 and summed(this_trip, cows)<limit):
                if(cows[i] > limit):
                    status[j] = 2
                elif (cows[i] > limit - summed(this_trip, cows)):
                    status[j] = 0
                else:
                    status[j] = 1
                    this_trip.append(i)
            j = j + 1
        if not(len(this_trip) == 0):
            all_trips.append(this_trip)
            this_trip = []
    print(all_trips)
    return all_trips

def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:
    
    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    def isDescending(list):
        previous = list[0]
        for number in list:
            if number > previous:
                return False
            previous = number
        return True

    def summed(list, cows):
        sum = 0
        for i in cows:
            if i in list:
                sum = sum + cows[i]
        return sum
    
    universe = []
    for item in (get_partitions(cows)):
        universe.append(item)

    ideal_trip = []
    check = True
    j = 0
    for all_trips in universe:
        # print(j)
        j = j + 1
        # print(all_trips)
        check = True
        trip_weight = []
        for trip in all_trips:
            # print(trip)
            # print(summed(trip, cows))
            if (summed(trip, cows) > limit):
                check = False
                break
            trip_weight.append(summed(trip, cows))
        if not(check):
            universe.remove(all_trips)
            continue
        if (len(ideal_trip) == 0) or (len(ideal_trip[0]) > len(all_trips)):
            ideal_trip = []
            ideal_trip.append(all_trips)
            continue
        elif (len(ideal_trip[0]) < len(all_trips)):
            universe.remove(all_trips)
            continue
        else:
            ideal_trip.append(all_trips)
            continue
    return ideal_trip

def compare_cow_transport_algorithms(cows):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    greedy_cow_transport(cows)
    end = time.time()
    print(end - start)

    start = time.time()
    brute_force_cow_transport(cows)
    end = time.time()
    print(end - start)

"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows  = load_cows("ps1_cow_data.txt")
# print(cows)
compare_cow_transport_algorithms(cows)
# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))
