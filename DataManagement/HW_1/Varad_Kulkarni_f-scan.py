import sys
def closest_to_head(head, requests_originals):
    minimum = sys.maxint
    return_val = sys.maxint
    for x in requests_originals:
        if abs(head - x) < minimum:
            minimum = abs(head - x)
            return_val = x
        if abs(head - x) == minimum:
            return_val = min(x, return_val)
    return return_val

def scan(head, requests_original, start, end):

    number_of_req = len(requests_original)
    dif1 = abs(max(requests_original) - end)
    dif2 = abs(min(requests_original) - start)
    wait_time = 0
    schedules = []
    first  = closest_to_head(head, requests_original)
    if first >= head:
        for x in range(first, end+1):
            if x in requests_original:
                schedules.append(x)
                wait_time+=abs(head-x)
                head = x
                requests_original.remove(x)

        if len(schedules) == number_of_req:

            '''
            print(','.join([str(x) for x in schedules]))
            print wait_time
            print str(schedules[len(schedules) - 1]) + "," + str(wait_time)
            '''
            return head, wait_time

        else:
            wait_time+= dif1
            head = end
            loop = end
            while(loop>=0):
                if loop in requests_original:
                    schedules.append(loop)
                    wait_time+=abs(head-loop)
                    head = loop
                    requests_original.remove(loop)
                loop = loop-1
            '''
            print(','.join([str(x) for x in schedules]))
            print wait_time
            print str(schedules[len(schedules)-1])+","+str(wait_time)
            '''
            return head, wait_time
    else:
        for x in xrange(first, start, -1):
            if x in requests_original:
                schedules.append(x)
                wait_time += abs(head - x)
                head = x
                requests_original.remove(x)

        if len(schedules) == number_of_req:
            '''
            print(','.join([str(x) for x in schedules]))
            print wait_time
            print str(schedules[len(schedules) - 1]) + "," + str(wait_time)
            '''
            return head, wait_time

        else:
            wait_time += dif2
            head = start
            loop = start
            while (loop <= end):
                if loop in requests_original:
                    schedules.append(loop)
                    wait_time += abs(head - loop)
                    head = loop
                    requests_original.remove(loop)
                loop = loop + 1
            '''
            print(','.join([str(x) for x in schedules]))
            print wait_time
            print str(schedules[len(schedules) - 1]) + "," + str(wait_time)
            '''
            return head,wait_time

start = 0
end   = 199
input_file = open(sys.argv[1], 'r')
head, requests = input_file.readlines()
head = int(head)
requests = requests.split(',')
requests = [int(x) for x in requests]
q1,q2=[],[]
wait_time = 0
if len(requests) <= 10:
    q1 = requests[:]
    head, wait_time = scan(head, q1, start, end)
    print head, wait_time
else:
    q1 = requests[:10]
    requests = requests[10:]
    while(q1):
        result = scan(head, q1, start, end)
        head = result[0]
        wait_time += result[1]
        if len(requests) <= 10:
            q2 = requests[:]
        else:
            q2 = requests[:10]
        requests = requests[10:]
        del q1[:]
        q1 = q2[:]
        del q2[:]
    print head, wait_time