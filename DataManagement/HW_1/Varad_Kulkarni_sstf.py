import sys
def find_next_request(head, requests):
    minimum = sys.maxint
    req = 0
    for x in requests:
        if abs(head-x) <= minimum and x<req:
            req = x
            minimum = abs(head-x)
    return req

def sstf(head, requests):
    wait_time = 0
    schedules = []
    while len(requests):
        next_process = find_next_request(head, requests)
        wait_time+= abs(head-next_process)
        schedules.append(next_process)
        requests.remove(next_process)
        head = next_process
    print(','.join([str(x) for x in schedules]))
    print wait_time
    print str(schedules[len(schedules)-1])+","+str(wait_time)

start = 0
end   = 199
input_file = open(sys.argv[1], 'r')
head, requests = input_file.readlines()
head = int(head)
requests = requests.split(',')
requests = [int(x) for x in requests]
sstf(head, requests)