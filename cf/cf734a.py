import sys

input = sys.stdin.readline


n = int(input())
s = input().strip()
anton = s.count("A")
danik = n - anton

print(anton > danik and "Anton" or (anton < danik and "Danik" or "Friendship"))
