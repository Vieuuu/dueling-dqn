import matplotlib.pyplot as plt

def read_log(path: str) -> dict:
    with open(path, 'r') as file:
        logs = file.read().splitlines()
    res = {
        'timestep': [],
        'reward': [],
    }
    for line in logs:
        _, timestep, reward = line.split()
        res['timestep'].append(int(timestep))
        res['reward'].append(float(reward))
    return res

dqn = read_log('rewards_d.txt')
dueling = read_log('rewards_dueling.txt')

plt.figure(figsize=(10, 5))
plt.plot(dqn['timestep'], dqn['reward'], label='DQN')
plt.plot(dueling['timestep'], dueling['reward'], label='Dueling DQN')
plt.xlabel('Timestep')
plt.ylabel('Episode Reward')
plt.legend()
plt.grid(ls='--')
plt.show()