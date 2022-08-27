'''
SHA-256
'''
'''
첫번째풀이
'''
import hashlib

def solution():
    result = hashlib.sha256(input().encode())
    print(result.hexdigest())
solution()
