import lightgbm as lgb

def train_model(X, y, group, params):
    dataset = lgb.Dataset(X, label=y, group=group)

    model = lgb.train(
        params,
        dataset,
        num_boost_round=300
    )

    return model