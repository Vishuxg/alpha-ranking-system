def test_backtest_runs():
    import pandas as pd
    from src.backtest import backtest

    df = pd.DataFrame({
        "date": ["2020-01-01","2020-01-02"],
        "asset": ["A","A"],
        "weight": [1,1],
        "target": [0.01,0.02]
    })

    r = backtest(df)
    assert len(r) > 0