import numpy as np
import numpy.random as rn


class SimulatedAnnealing:
    def __init__(self, bound, cost_function, max_iterations):
        self.interval = bound
        self.objective_fn = cost_function
        self.max_iterations = max_iterations

    def random_start(self):
        a, b = self.interval
        return a + (b - a) * rn.random_sample()

    def take_step_in_neighborhood(self, x, fraction):
        amplitude = (max(self.interval) - min(self.interval)) * fraction / 10
        delta = (-amplitude / 2.) + amplitude * rn.random_sample()
        return self.clip(x + delta)

    def acceptance_probability(self, cost, new_cost, value):
        if new_cost < cost:
            return 1
        else:
            p = np.exp(-(new_cost - cost) / value)
            return p

    def value(self, fraction):
        return max(0.01, min(1, 1 - fraction))

    def clip(self, x):
        a, b = self.interval
        return max(min(x, b), a)

    def annealing(self, debug=True):

        state = self.random_start()
        cost = self.objective_fn(state)
        states, costs = [state], [cost]

        for _ in range(self.max_iterations):
            # Take a step
            f = _ / float(self.max_iterations)
            V = self.value(f)
            new_state = self.take_step_in_neighborhood(state, f)
            new_cost = self.objective_fn(new_state)
            # evaluate candidate state
            if debug:
                print("Step #{:>2}/{:>2} : T = {:>4.3g}, state = {:>4.3g}, cost = {:>4.3g}"
                      ", new_state = {:>4.3g}, new_cost = {:>4.3g} ...".format(
                    _, self.max_iterations, V, state, cost, new_state, new_cost))
            if self.acceptance_probability(cost, new_cost, V) > rn.random():
                state, cost = new_state, new_cost
                states.append(state)
                costs.append(cost)

        return state, self.objective_fn(state), states, costs


if __name__ == '__main__':
    bound = [-10, 10]


    def objective_function(x):
        return x ** 2


    sim = SimulatedAnnealing(bound, objective_function, 30)
    sim.annealing()
