import math, queue
from collections import Counter

####### Problem 1 #######

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))



    
def get_frequencies(fname):
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    
    for c in f.keys():
        p.put(TreeNode(None, None, (f[c], c)))

    while p.qsize() > 1:

        x = p.get()
        y = p.get()

        z = TreeNode(left=x, right=y, data=(x.data[0] + y.data[0], ""))

        p.put(z)

    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):

    if node.left is None and node.right is None:
        code[node.data[1]] = prefix  
    else:

        if node.left:
            get_code(node.left, prefix + "0", code)

        if node.right:
            get_code(node.right, prefix + "1", code)
    
    return code  


# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(char_freq_dict):
    unique_char_count = len(char_freq_dict)
    if unique_char_count == 0:
        return 0  
    bits_per_char = math.ceil(math.log2(unique_char_count))
    encoding_cost = sum(frequency * bits_per_char for character, frequency in char_freq_dict.items())
    return encoding_cost

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    total_cost = 0
    for char, encoding in C.items():

        if char in f:
            frequency = f[char]
            cost = frequency * len(encoding)
            total_cost += cost

    return total_cost

file_path = 'asyoulik.txt'
f = get_frequencies(file_path )

print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))



file_path = 'f1.txt'
f = get_frequencies(file_path )
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))


file_path = 'alice29.txt'
f = get_frequencies(file_path )
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))


file_path = 'grammar.lsp'
f = get_frequencies(file_path )
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))


file_path = 'fields.c'
f = get_frequencies(file_path )
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))

