import numpy as np
import random


GAMMA = 0.8
ALPHA = 0.01
num_steps = 100000
SIZE = 6
R = np.asarray([[-1, -1, -1, -1, 0,-1],
                [-1, -1, -1, 0, -1,100],
                [-1, -1, -1, 0, -1,-1],
                [-1, 0, 0, -1, 0,-1],
                [0, -1, -1, 0, -1,100],
                [-1,0,-1,-1,0,100]])
Q = np.zeros([SIZE, SIZE], np.float32)


def getMaxQ(statex, statey):
    state = []
    state.append(Q[statey])
    state = np.concatenate(state, axis=0)
    return max(state)
  #  state = []
  #  if statex > 0:
  #      state.append(Q[statex-1, statey])
  #  if statey > 0:
  #      state.append(Q[statex, statey-1])
  #  if statex < SIZE-1:
  #      state.append(Q[statex+1, statey])
  #  if statey < SIZE-1:
  #      state.append(Q[statex, statey+1])
  #  return max(state[:])


def QLearning():
    for statex in range(SIZE):
        for statey in range(SIZE):
            if( R[statex, statey] != -1):
                Q[statex, statey] = Q[statex, statey] + ALPHA* (R[statex, statey]+GAMMA * getMaxQ(statex, statey)-Q[statex,statey])
            # Q[statex, statey] = R[statex, statey] + GAMMA * getMaxQ(statex, statey)
            #这两个公式基本等价，最后收敛的Q是一样的

Q[1,5] = (1-ALPHA)*Q[1,5] + ALPHA* (R[1,5]+GAMMA * getMaxQ(1,5))
print(Q[1,5])

#input()
print("====================")
print("map:")
print(R)
count = 0    
while count < num_steps:
    QLearning()
    count += 1

print(Q)  



# 验证

for i in range(10):
    print("第{}次验证".format(i + 1))
    state = random.randint(0, 5)
    print('机器人处于{}'.format(state))
    count = 0
    while state != 5:
        if count > 20:
            print('fail')
            break
        # 选择最大的q_max
        q_max = Q[state].max()

        q_max_action = []
        for action in range(6):
            if Q[state, action] == q_max:
                q_max_action.append(action)

        next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
        print("the robot goes to " + str(next_state) + '.')
        state = next_state
        count += 1

