import pyautogui
import time
import random

def auto_type_and_send():
    # -------------------------- 可自定义配置区域 --------------------------
    # 1. 待随机输入的字符串列表（可自行增删修改）
    TARGET_STRINGS = ["你好呀～", "今天天气不错！", "在忙吗？", "这个脚本很好用！", "有空聊会儿吗？"]
    # 2. 总运行时间（单位：秒，例如 120 表示运行2分钟）
    TOTAL_RUN_SECONDS = 120
    # 3. 每个字符串输入后，随机等待多久发送（单位：秒，模拟思考时间）
    MIN_WAIT_BEFORE_SEND = 0.5  # 最短等待0.5秒
    MAX_WAIT_BEFORE_SEND = 2    # 最长等待2秒
    # 4. 发送后，随机等待多久开始下一轮输入（单位：秒，模拟对话间隔）
    MIN_INTERVAL_AFTER_SEND = 3  # 最短间隔3秒
    MAX_INTERVAL_AFTER_SEND = 8  # 最长间隔8秒
    # ----------------------------------------------------------------------

    # 提示：运行脚本前，请手动打开微信/QQ聊天窗口，确保窗口在前台（可看到输入框和发送按钮）
    print("⚠️  请在5秒内将微信/QQ聊天窗口切换到前台！")
    time.sleep(5)  # 预留5秒切换窗口时间
    start_time = time.time()  # 记录脚本开始时间

    while True:
        # 1. 检查是否超过总运行时间，是则退出
        elapsed_time = time.time() - start_time
        if elapsed_time >= TOTAL_RUN_SECONDS:
            print("\n✅ 已达到设定总运行时间，脚本结束！")
            break

        # 2. 随机选择一个要输入的字符串
        random_str = random.choice(TARGET_STRINGS)
        # 3. 模拟「打字输入」：逐字符输入（更贴近真人，避免瞬间输入）
        print(f"\n🔤 即将输入：{random_str}")
        pyautogui.typewrite(random_str, interval=random.uniform(0.05, 0.2))  # 每个字符间隔0.05-0.2秒（真人打字速度）

        # 4. 输入后随机等待（模拟思考是否发送）
        wait_time = random.uniform(MIN_WAIT_BEFORE_SEND, MAX_WAIT_BEFORE_SEND)
        print(f"⌛ 等待 {wait_time:.1f} 秒后发送...")
        time.sleep(wait_time)

        # 5. 自动发送：模拟按「Enter键」（微信/QQ默认按Enter发送，若需按发送按钮可替换为鼠标点击）
        pyautogui.press('enter')
        print(f"✓ 已发送：{random_str}")

        # 6. 发送后随机等待（模拟对话间隔，避免连续发送）
        interval_time = random.uniform(MIN_INTERVAL_AFTER_SEND, MAX_INTERVAL_AFTER_SEND)
        print(f"⌛ 等待 {interval_time:.1f} 秒后开始下一轮...")
        time.sleep(interval_time)

if __name__ == "__main__":
    try:
        auto_type_and_send()
    except KeyboardInterrupt:
        print("\n❌ 脚本被手动终止！")



        