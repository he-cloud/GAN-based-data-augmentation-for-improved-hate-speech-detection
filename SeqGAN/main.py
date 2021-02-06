import numpy as np
from SeqGAN.train import Trainer
from SeqGAN.get_config import get_config

# 加载配置文件
config = get_config('config.ini')

# 构造训练器
trainer = Trainer(config["batch_size"],
                config["max_length"],
                config["g_e"],
                config["g_h"],
                config["d_e"],
                config["d_h"],
                config["d_dropout"],
                path_pos=config["path_pos"],
                path_neg=config["path_neg"],
                g_lr=config["g_lr"],
                d_lr=config["d_lr"],
                n_sample=config["n_sample"],
                generate_samples=config["generate_samples"])


# Pretraining for adversarial training 对抗训练的pretrain
trainer.pre_train(g_epochs=config["g_pre_epochs"],
                d_epochs=config["d_pre_epochs"],
                g_pre_path=config["g_pre_weights_path"],
                d_pre_path=config["d_pre_weights_path"],
                g_lr=config["g_pre_lr"],
                d_lr=config["d_pre_lr"])


trainer.load_pre_train(config["g_pre_weights_path"], config["d_pre_weights_path"])
trainer.reflect_pre_train()

# 开始训练
trainer.train(steps=1,
            g_steps=1,
            head=10,
            g_weights_path=config["g_weights_path"],
            d_weights_path=config["d_weights_path"])
# 保存模型参数
trainer.save(config["g_weights_path"], config["d_weights_path"])

# 加载模型参数
trainer.load(config["g_weights_path"], config["d_weights_path"])

#测试数据
trainer.test()

# 输出测试文件
trainer.generate_txt(config["g_test_path"], config["generate_samples"])

