#From codereview.stackexchange.com                    
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

# This is a helper function that will fetch all of the available partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

# total = []
# for item in (get_partitions({'Louis': 45, 'Milkshake': 75, 'Muscles': 65, 'Horns': 50, 'Miss Bella': 15, 'Lotus': 10, 'MooMoo': 85, 'Patches': 60, 'Clover': 5, 'Polaris': 20})):
    # total.append(item)
# print(total)
