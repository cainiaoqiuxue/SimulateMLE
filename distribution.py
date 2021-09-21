from scipy import stats
from base_module import SimulateMLE


class Poisson(SimulateMLE):
    def __init__(self, theta_0, thetas):
        super(Poisson, self).__init__(theta_0, thetas)
        self.name = "Poisson"

    def get_rv_function(self):
        return stats.poisson.rvs

    def get_rv_probability(self):
        return stats.poisson.pmf

    def get_rv_ppf(self):
        return stats.poisson.ppf


class Bernoulli(SimulateMLE):
    def __init__(self, theta_0, thetas):
        super(Bernoulli, self).__init__(theta_0, thetas)
        self.name = "Bernoulli"

    def get_rv_function(self):
        return stats.bernoulli.rvs

    def get_rv_probability(self):
        return stats.bernoulli.pmf

    def get_rv_ppf(self):
        return stats.bernoulli.ppf


class Fatiguelife(SimulateMLE):
    def __init__(self, theta_0, thetas):
        super(Fatiguelife, self).__init__(theta_0, thetas)
        self.name = "Fatiguelife"

    def get_rv_function(self):
        return stats.fatiguelife.rvs

    def get_rv_probability(self):
        return stats.fatiguelife.pdf

    def get_rv_ppf(self):
        return stats.fatiguelife.ppf


class Bradford(SimulateMLE):
    def __init__(self, theta_0, thetas):
        super(Bradford, self).__init__(theta_0, thetas)
        self.name = "Bradford"

    def get_rv_function(self):
        return stats.bradford.rvs

    def get_rv_probability(self):
        return stats.bradford.pdf

    def get_rv_ppf(self):
        return stats.bradford.ppf


class Dgamma(SimulateMLE):
    def __init__(self, theta_0, thetas):
        super(Dgamma, self).__init__(theta_0, thetas)
        self.name = "Dgamma"

    def get_rv_function(self):
        return stats.dgamma.rvs

    def get_rv_probability(self):
        return stats.dgamma.pdf

    def get_rv_ppf(self):
        return stats.dgamma.ppf


class Dweibull(SimulateMLE):
    def __init__(self, theta_0, thetas):
        super(Dweibull, self).__init__(theta_0, thetas)
        self.name = "Dweibull"

    def get_rv_function(self):
        return stats.dweibull.rvs

    def get_rv_probability(self):
        return stats.dweibull.pdf

    def get_rv_ppf(self):
        return stats.dweibull.ppf
