def poisson_process(rate, time_duration):
    num_events = np.random.poisson(rate * time_duration)
    event_times = np.cumsum(np.random.uniform(0, 2/rate, num_events))
    N_t = {}
    for i in range(num_events):
        N_t.update({event_times[i]:i+1})
    return event_times

def ESTRISK(u, c, lambd, mu, T, M):
    ruin_count = 0
    
    for _ in range(M):
        Nt_times = poisson_process(lambd, T)
        Y = np.random.exponential(mu, len(Nt_times))
        aggregate_claims = np.cumsum(Y)
        
        for i in range(len(Nt_times)):
            Xt = u + c * Nt_times[i] - aggregate_claims[i]
            if Xt < 0:
                ruin_count += 1
                break

    ruin_probability = ruin_count / M
    return ruin_probability

def FUN(R, dt, N):
    times = np.zeros(N)
    i = 0
    while i < N:
        x = 0
        y = 0
        t = 0
        while x**2 + y**2 <= R**2:
            x += np.random.normal(0, 1) * np.sqrt(dt)
            y += np.random.normal(0, 1) * np.sqrt(dt)
            t += dt
        if y > 0:
            
            continue
        else:
            times[i] = t
            i += 1
    return np.sum(times) / N

def GEN(N):
    us = np.random.rand(N)
    samples = np.ceil(us/(1-us))
    return samples

sample = GEN(10**2)

plt.figure(figsize=(15,9))
sns.histplot(sample, discrete=True, stat="probability",bins=10000)
xs = np.linspace(1,50,50)
plt.scatter(xs, pmf(xs),c="red")
ax = plt.gca()
ax.set_xlim([0, 50])
plt.show()
