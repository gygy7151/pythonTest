'''
트리순회
'''
'''
두번째풀이 - 트리를 dict으로 표현 {A : [B,C]}
'''
N = int(input())
bst = {}

for _ in range(N):
    v, left, right = map(str, input().split())
    bst[v] = [left, right]

def pre_order(v):
    if v != '.':
        print(v, end='')
        pre_order(bst[v][0])
        pre_order(bst[v][1])

def in_order(v):
    if v != '.':
        in_order(bst[v][0])
        print(v, end='')
        in_order(bst[v][1])

def post_order(v):
    if v != '.':
        post_order(bst[v][0])
        post_order(bst[v][1])
        print(v, end='')

pre_order('A')
print()
in_order('A')
print()
post_order('A')
'''
첫번째풀이 - 타입에러
'''
# class Node(object):
#     def __init__(self, v):
#         self.v = v
#         self.left = self.right = None

# class BinarySearchTree(object):
#     def __init__(self):
#         self.root = None
    
#     def insert(self, v):
#         self.root = self._insert_value(self.root, v)
#         return self.root is not None
    
#     def _insert_value(self, parent, v):
#         if parent is None:
#             parent = Node(parent)
#         else:
#             if parent <= parent.v:
#                 parent.left = self._insert_value(parent.left, v)
#             else:
#                 parent.right = self._insert_value(parent.right, v)
#         return parent

#     def pre_order(self,v):
#         global pre_temp
#         if v != None:
#             pre_temp += pre_temp + self.key
#             pre_order(v.left)
#             pre_order(v.right)
        
#     def in_order(self,v):
#         global in_temp
#         if v != None:
#             in_order(v.left)
#             in_temp += in_temp + self.key
#             in_order(v.right)
    
#     def post_order(self,v):
#         global post_temp
#         if v != None:
#             post_order(v.left)
#             post_order(v.right)
#             post_temp += post_temp + self.key

# N = int(input())
# bst = BinarySearchTree()
# first_node = []
# for _ in range(N):
#     node_key, node_left, node_right = map(str, input().split())
#     Node(node_key)
#     bst.insert(node_key)
#     first_node.append(node_key)
# pre_temp = ''
# in_temp = ''
# post_temp = ''
# bst.pre_order(first_node[0])
# bst.in_order(first_node[0])
# bst.post_order(first_node[0])