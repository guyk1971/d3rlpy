import pytest

from d3rlpy.dynamics.torch.mopo_impl import MOPOImpl
from d3rlpy.models.optimizers import AdamFactory
from d3rlpy.models.encoders import DefaultEncoderFactory
from tests.algos.algo_test import DummyScaler, DummyActionScaler
from tests.dynamics.dynamics_test import torch_impl_tester


@pytest.mark.parametrize("observation_shape", [(100,)])
@pytest.mark.parametrize("action_size", [2])
@pytest.mark.parametrize("learning_rate", [1e-3])
@pytest.mark.parametrize("optim_factory", [AdamFactory()])
@pytest.mark.parametrize("encoder_factory", [DefaultEncoderFactory()])
@pytest.mark.parametrize("n_ensembles", [5])
@pytest.mark.parametrize("lam", [1.0])
@pytest.mark.parametrize("discrete_action", [False, True])
@pytest.mark.parametrize("scaler", [None, DummyScaler()])
@pytest.mark.parametrize("action_scaler", [None, DummyActionScaler()])
def test_mopo_impl(
    observation_shape,
    action_size,
    learning_rate,
    optim_factory,
    encoder_factory,
    n_ensembles,
    lam,
    discrete_action,
    scaler,
    action_scaler,
):
    impl = MOPOImpl(
        observation_shape,
        action_size,
        learning_rate,
        optim_factory,
        encoder_factory,
        n_ensembles,
        lam,
        discrete_action,
        use_gpu=False,
        scaler=scaler,
        action_scaler=action_scaler if not discrete_action else None,
    )
    impl.build()
    torch_impl_tester(impl, discrete=discrete_action)
