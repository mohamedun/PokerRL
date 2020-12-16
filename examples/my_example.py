from DriverBase import DriverBase
class MyDriver(DriverBase):
    def __init__(self, t_prof, eval_methods, chief_cls, n_iterations):
        super().init(t_prof, eval_methods, chief_cls, n_iterations)
        pass
    def run(self):
        pass
    def load_checkpoint(self):
        pass
    def checkpoint(self):
        pass

ctrl = MyDriver(t_prof=None,
                  eval_methods={},
                  chief_cls=None,
                  n_iterations=2)

