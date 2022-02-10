from gym.envs.registration import register

register(id='HumanoidAssembly-v0',
        entry_point='humanoid_assembly.envs:HumanoidAssemblyEnv',
)
