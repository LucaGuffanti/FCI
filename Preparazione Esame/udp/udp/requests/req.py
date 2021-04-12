import requests
from matplotlib import pyplot as plt

time = []
average = []
url = ['http://www.google.com', 'http://www.youtube.com', 'http://www.amazon.com']


plt.figure('Tempo di risposta')
plt.title('tempi di risposta di google')
plt.xlabel('tentativo')
plt.ylabel('risposta(ms)')


# number = 1
for name in url:
    for i in range(0, 10):
        r = requests.get(name)
        time.append(r.elapsed.microseconds/1000)
        average.append(sum(time)/len(time))
    # plt.subplot(1, len(url), number)
    plt.plot(time)
    plt.plot(average)
    time.clear()
    average.clear()
    # number+=1

# plt.show()

