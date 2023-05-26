"""Implementation of randomized sample-based Apriori.
"""

"""Implementation of the Apriori algorithm for frequent item set mining.
"""

def apriori_main_memory(data: list[str], t: int) -> dict[frozenset[str], int]:
    """Execute the apriori algorithm on a list of strings where each string represents a basket IN MEMORY.

    Args:
        data (list[str]): The input data as a list where each entry represents a basket in which each item is separated by a space.
        t (int): Frequency threshold t, item sets with a lower freq will be discarded.

    Returns:
        dict[frozenset[str], int]: A dictionary that has the frequent item sets as keys 
            with their frequencies as values.
    """
    passes: list[dict] = [] # empty list where the results of each pass are stored
    set_size: int = 1 # current size of the candidate sets
    output: dict[frozenset[str], int] = {}

    # keep doing passes as long as we find new frequent item (sets)
    while True:
            counts: dict[frozenset[str], int] = {}
                
            # the first pass consists merely of collecting the counts of all individual items
            if set_size <= 1:
        
                # iterate over each basket
                for i, line in enumerate(data):
                    parsed_row: list[str] = line.split()
                    
                    # now insert the items into the counting dictionary
                    for item in parsed_row:
                        single_item_set: frozenset[str] = frozenset([item])
                        if single_item_set not in counts.keys():
                            counts[single_item_set] = 1
                        else:
                            counts[single_item_set] += 1

            # in subsequent passes, the candidates are generated from the last pass
            else:
                # generate candidates
                candidates: set[frozenset[str]] = set()
                for A in passes[set_size-2].keys():
                    for B in passes[set_size-2].keys():
                        union = frozenset(A.union(B))
                        if len(union) == set_size and A != B:
                            candidates.add(union)

                # and then go over the file and count the occurrences
                for i, line in enumerate(data):
                    parsed_row: set[str] = set(line.split())

                    # check for each candidate in the row and update the counters
                    for candidate in candidates:
                        if candidate.issubset(parsed_row):
                            if candidate not in counts.keys():
                                counts[candidate] = 1
                            else:
                                counts[candidate] += 1

            # and then filter the items such that the non-frequent ones are discarded
            for key in list(counts):
                if counts[key] < t: 
                    del counts[key]

            # update the output dictionary
            output.update(counts)

            # append the result of the iteration to the list of passes in case we found frequent item sets
            if len(counts) > 0:
                passes.append(counts)
                print(f'Pass {set_size} finished.')
                set_size += 1

            # if no more frequent item sets are found, output the frequent item sets
            else:
                return output