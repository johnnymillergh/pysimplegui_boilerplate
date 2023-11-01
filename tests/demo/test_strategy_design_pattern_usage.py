import pytest
from loguru import logger

from pysimplegui_boilerplate.demo.strategy_design_pattern_usage import BaseStrategy


@pytest.fixture(scope="session", autouse=True)
def setup() -> None:
    logger.info(f"Setting up tests for {__file__}")
    BaseStrategy.init()


def test_strategies_when_matches() -> None:
    BaseStrategy.iter_execute("Data for strategy one")
    BaseStrategy.iter_execute("Data for strategy two")


def test_strategies_when_not_matches() -> None:
    with pytest.raises(ValueError) as exc_info:
        BaseStrategy.iter_execute("Data that doesn't match strategy")
    assert exc_info is not None
    logger.warning(f"Expected exception: {exc_info.value}")


def test_base_strategy() -> None:
    strategy = BaseStrategy()
    strategy_name = strategy.strategy_name()
    assert strategy_name is not None
    assert strategy_name == BaseStrategy.__name__
    with pytest.raises(NotImplementedError) as exc_info_for_matches:
        strategy.matches("any")
    assert exc_info_for_matches is not None
    with pytest.raises(NotImplementedError) as exc_info_for_execute:
        strategy.execute("any")
    assert exc_info_for_execute is not None


def test_call_twice_init() -> None:
    try:
        BaseStrategy.init()
        BaseStrategy.init()
        strategies = BaseStrategy._strategies
        assert strategies is not None
        assert len(strategies) == 2
        logger.info(f"Strategies: {strategies}")
    except Exception as e:
        assert False, f"Unexpected exception raised: {e}"
