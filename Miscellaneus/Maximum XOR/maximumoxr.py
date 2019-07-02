# Following: https://www.hackerrank.com/challenges/maximum-xor/forum
def to_binary_str(number):
    return bin(number)[2:]


def build_trie(numbers_array, max_len):
    trie = {}

    for number in numbers_array:
        trie_pos = trie
        binary_number = to_binary_str(number)
        # pad the string with 0's to be the size of the largest number
        # this way we don't have to deal with leftover bits from the query
        # or the number.
        padded_number = binary_number.zfill(max_len)

        for bit in padded_number:
            if not bit in trie_pos:
                trie_pos[bit] = {}
            trie_pos = trie_pos[bit]

    return trie


def maxXor(arr, queries):
    # get the largest number so we can extra it's length
    # take into account the query and the numbers.
    max_number = max(arr + queries)
    max_number_bin = to_binary_str(max_number)
    max_number_len = len(max_number_bin)
    opposites = {'0': '1', '1': '0'}
    max_xors = []

    trie_max = build_trie(arr, max_number_len)

    for query in queries:
        binary_query = to_binary_str(query)
        padded_query = binary_query.zfill(max_number_len)
        trie_position = trie_max
        xor_string = ''

        for query_bit in padded_query:
            opposite = opposites[query_bit]

            if opposite in trie_position:
                xor_string += '1'
                trie_position = trie_position[opposite]
            elif query_bit in trie_position:
                xor_string += '0'
                trie_position = trie_position[query_bit]

        integer_max = int(xor_string, 2)
        max_xors.append(integer_max)

    return max_xors

# Less time efficient solution
# Complete the maxXor function below.
# def maxXor(arr, queries):
#     # solve here
#     tmparr = []
#     maxval = []
#     for i in queries:
#         for j in arr:
#             tmp = j^i
#             tmparr.append(tmp)
#         maxval.append(max(tmparr))
#         tmparr.clear()
#     return maxval
