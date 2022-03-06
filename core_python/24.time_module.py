import time
initial = time.time()

print(initial)

k = 0
while(k<45):
    print('---')
    k=k+1

    # print('while loop time',time.time()-initial,'seconds')
    mytime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(initial))
    print('mytime',mytime)