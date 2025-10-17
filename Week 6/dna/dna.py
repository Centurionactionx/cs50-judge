import csv
import sys


def main():

    # TODO: Check for command-line usage
    n = input()
    locs = [c for c in n.split(" ")]

    # TODO: Read database file into a variable
    import csv

    rows = []
    with open(locs[0]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    keys = [k for k in list(rows[0].keys())[1:] ]

    # TODO: Read DNA sequence file into a variable

    f = open(locs[1], "r")
    seq = f.read()
    f.close()
    # TODO: Find longest match of each STR in DNA sequence

    dna_counts = {}
    for dna in keys:
        dna_counts[dna] = str(longest_match(seq, dna))

    # TODO: Check database for matching profiles
    for dic in rows:
        keys_left = list(dic.keys())[1:]
        sub_dic = {}
        for key in keys_left:
            sub_dic[key] = dic[key]

        if sub_dic == dna_counts:
            print(dic[list(dic.keys())[0]])
            return
    print("No match")
    return

# cs50 helper function
def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
