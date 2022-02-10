import gym
# from render_browser import render_browser

# @render_browser
def test_policy():
    env = gym.make('Humanoid-v2')
    from gym import envs
    print(envs.registry.all())    # print the available environments

    print(env.action_space)
    print(env.observation_space)
    print(env.observation_space.high)
    print(env.observation_space.low)
    episode = 0
    reward = None
    for i_episode in range(20000000):
        episode+=1
        observation = env.reset()
        print("Episode:", episode, "Reward", reward)
        for t in range(100):
            env.render()
            # yield env.render(mode='rgb_array')
            # print(observation)
            action = env.action_space.sample()    # take a random action
            observation, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(t+1))
                break
    env.close()

test_policy()
