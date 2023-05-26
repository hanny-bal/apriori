"""Implementation of randomized sample-based Apriori.
"""
import random

def randomized_apriori(file_path: str, t: int, p: float, f: bool) -> dict[frozenset[str], int]:
    """Execute randomized apriori on the specified file using a frequency threshold t.

    Args:
        file_path (str): The input file containing one basket per line where each item is separated by a space.
        t (int): Frequency threshold t, item sets with a lower freq will be discarded.
        p (float): Sampling probability for each line of data.
        f (bool): If true, an extra pass over the data is performed to remove false positives.

    Returns:
        dict[frozenset[str], int]: A dictionary that has the frequent item sets as keys 
            with their frequencies as values.
    """
    # First, we create a sample of the data set: That is, we read the data set once, sample each basket with probability p
    # and append it to a list stored in main memory.
    sample: list[str] = 0

    with open(file_path) as file:
        for i, line in enumerate(file):
            if random.random() < p:
                sample.append(line)

    # now run apriori on the sample
    output: dict[frozenset[str], int] = apriori_main_memory(data=sample, t=t*p)

    # if f is true, perform an extra pass over the data and remove false positives
    if f:
        # keep a dictionary of true counts
        counts: dict[frozenset[str], int] = {}

        # iterate over the original file and count
        with open(file_path) as file:
            for i, line in enumerate(file):
                parsed_row: set[str] = set(line.split())

                # check for each candidate in the row and update the counters
                for candidate in output.keys():
                    if candidate.issubset(parsed_row):
                        if candidate not in counts.keys():
                            counts[candidate] = 1
                        else:
                            counts[candidate] += 1

        # and then filter the output such that the non-frequent ones are discarded
        for key in list(counts):
            if counts[key] < t: 
                del output[key]

    return output

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