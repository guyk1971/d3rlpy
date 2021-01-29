import pytest
import numpy as np

from d3rlpy.algos.awr import AWR, DiscreteAWR
from tests import performance_test
from .algo_test import algo_tester, algo_update_tester
from .algo_test import algo_pendulum_tester, algo_cartpole_tester


@pytest.mark.parametrize("observation_shape", [(100,), (4, 84, 84)])
@pytest.mark.parametrize("action_size", [2])
@pytest.mark.parametrize("scaler", [None, "min_max"])
@pytest.mark.parametrize("action_scaler", [None, "min_max"])
def test_awr(observation_shape, action_size, scaler, action_scaler):
    awr = AWR(
        batch_size=100,
        batch_size_per_update=20,
        scaler=scaler,
        action_scaler=action_scaler,
    )
    algo_tester(awr, observation_shape, state_value=True)
    algo_update_tester(awr, observation_shape, action_size)


@performance_test
def test_awr_performance():
    awr = AWR()
    algo_pendulum_tester(awr, n_trials=3)


@pytest.mark.parametrize("observation_shape", [(100,), (4, 84, 84)])
@pytest.mark.parametrize("action_size", [2])
@pytest.mark.parametrize("scaler", [None, "min_max"])
def test_discrete_awr(observation_shape, action_size, scaler):
    awr = DiscreteAWR(batch_size=100, batch_size_per_update=20, scaler=scaler)
    algo_tester(awr, observation_shape, state_value=True)
    algo_update_tester(awr, observation_shape, action_size, True)


@performance_test
def test_discrete_awr_performance():
    awr = DiscreteAWR()
    algo_cartpole_tester(awr, n_trials=3)
