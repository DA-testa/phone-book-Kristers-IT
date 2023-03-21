import time
import random 
import sys
import numpy as np

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if len(query[1]) > 7:   #or int(query[1][:1]) == 0
            print("wrong input")
            sys.exit()
        else:
            if self.type == 'add':

                try:
                    self.name = query[2]
                except IndexError:
                    print("wrong input")
                    sys.exit()

                if len(query[2]) >= 15 or query[2] == "not" and query[3] == "found":
                    print("wrong input")
                    sys.exit()

def read_queries():
    n = int(input())
    if n >= 1 and n <= 10^(5):
        return [Query(input().split()) for i in range(n)]
    else:
        print("wrong input")
        sys.exit()
        

def write_responses(result):
    print('\n'.join(result[1:]))

def process_queries(queries):
    start_time = time.time()
    result = ""
    contacts = {}
    m = 1
    index = random.randint(0, m-1)
    if index >= m:
        m = index + 1
    contacts[index] = index
    for cur_query in queries:
        if cur_query.type == 'add':
            if cur_query.name in queries:
                contacts[cur_query.number] = cur_query.name
            else:
                contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            if cur_query.number in contacts:
                del contacts[cur_query.number]
        elif cur_query.type == 'find':
            if cur_query.number in contacts:
                response = contacts[cur_query.number]
            else:
                response = "not found"
            result = np.append(result, response)
    print(time.time() - start_time)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
