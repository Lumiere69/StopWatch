import time

print('Нажмите клавишу Enter, чтобы начать. После этого нажмите клавишу Enter, чтобы "нажать" на секундомер.')
input()
print('Начали.')
startTime = time.time() 
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Круг #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nГотово.')