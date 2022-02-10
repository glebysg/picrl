from gym.envs.registration import register

register(
    id='assembly-v0',
    entry_point='humanoid_assembly.envs:HumanoidAssemblyEnv',
)
