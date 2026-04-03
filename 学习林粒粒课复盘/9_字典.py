wagnluo_liuxxixn = {"DeepSeek深度求索":"表达对知识和真理的深入追求",
                    "村咖":"指代乡村的咖啡文化",
                    "来财":"表达对财富的期待"
                    }
wagnluo_liuxxixn["谷子"] = "是英文单词goods的音译，本义为商品，流行语中特指动漫、游戏等二次元文化的衍生产品"
wagnluo_liuxxixn["具身智能"] = "指具有物理载体的智能体，最典型的例子就是人形机器人。具身智能的出现，标志着人工智能进入了一个新的发展阶段"
wagnluo_liuxxixn["敬自己一杯"] = "在短视频平台上，年轻人以举杯仪式，分享人生酸甜、自嘲过往经历。它打破传统，将致敬焦点转向自我，是对努力与平凡的接纳，更是当代年轻人缓解压力、实现自我和解与价值认同的温柔表达"
wagnluo_liuxxixn["助我破鼎"] = "源自动画电影《哪吒之魔童闹海》中哪吒与敖丙合力击碎法器“天元鼎”时的经典台词。网友们以此为自己鼓劲打气，展现自己在面对困难时积极应对、不言放弃的决心"

while True:
    user_input = input("请问你想要的流行语：")
    if user_input in wagnluo_liuxxixn:
        print("你要的流行语是",user_input,"含义如下")
        print(wagnluo_liuxxixn[user_input])
    else:
        print("你要的流行语未收入")
        print("当前本词典收留词条数为："+str(len(wagnluo_liuxxixn))+"条\n如下")
        print(wagnluo_liuxxixn)