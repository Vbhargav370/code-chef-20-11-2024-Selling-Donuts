"""
https://www.codechef.com/START161D/problems/DONUTSELL

Selling Donuts
Chef owns a donut shop that sells N different types of donuts, numbered from 1 to N.
Today, Chef baked A[i] donuts of the i-th type.
M customers will visit the shop. The i-th customer wants to buy exactly one donut of type B[i]. If Chef has no remaining donuts of type B[i], the i-th customer will become sad.
Your task is to determine how many customers will become sad.
Input Format
1. The first line of input contains a single integer T, denoting the number of test cases.
2. Each test case consists of three lines:
   - The first line contains two space-separated integers N and M:
      * N: the number of donut types.
      * M: the number of customers.
   - The second line contains N space-separated integers A[1], A[2], ..., A[N], where A[i] represents the number of donuts Chef has of type i.
   - The third line contains M space-separated integers B[1], B[2], ..., B[M], where B[i] represents the type of donut the i-th customer wants to buy.

"""


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sad_customers = 0

    for customer_type in B:
        index = customer_type - 1
        if A[index] > 0:
            A[index] -= 1
        else:
            sad_customers += 1

    print(sad_customers)
