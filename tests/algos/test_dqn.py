import pytest

from d3rlpy.algos.dqn import DQN, DoubleDQN
from tests import performance_test
from .algo_test import algo_tester, algo_update_tester, algo_cartpole_tester


@pytest.mark.parametrize("observation_shape", [(100,), (4, 84, 84)])
@pytest.mark.parametrize("action_size", [2])
@pytest.mark.parametrize("q_func_factory", ["mean", "qr", "iqn", "fqf"])
@pytest.mark.parametrize("scaler", [None, "min_max"])
def test_dqn(observation_shape, action_size, q_func_factory, scaler):
    dqn = DQN(q_func_factory=q_func_factory, scaler=scaler)
    algo_tester(dqn, observation_shape)
    algo_update_tester(dqn, observation_shape, action_size, discrete=True)


@performance_test
@pytest.mark.parametrize("q_func_factory", ["mean", "qr", "iqn", "fqf"])
def test_dqn_performance(q_func_factory):
    dqn = DQN(q_func_factory=q_func_factory)
    algo_cartpole_tester(dqn)


@pytest.mark.parametrize("observation_shape", [(100,), (4, 84, 84)])
@pytest.mark.parametrize("action_size", [2])
@pytest.mark.parametrize("q_func_factory", ["mean", "qr", "iqn", "fqf"])
@pytest.mark.parametrize("scaler", [None, "min_max"])
def test_double_dqn(observation_shape, action_size, q_func_factory, scaler):
    double_dqn = DoubleDQN(q_func_factory=q_func_factory, scaler=scaler)
    algo_tester(double_dqn, observation_shape)
    algo_update_tester(double_dqn, observation_shape, action_size, True)


@performance_test
@pytest.mark.parametrize("q_func_factory", ["mean", "qr", "iqn", "fqf"])
def test_double_dqn_performance(q_func_factory):
    double_dqn = DoubleDQN(q_func_factory=q_func_factory)
    algo_cartpole_tester(double_dqn)
