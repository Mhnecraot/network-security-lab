#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DDoS 攻击模拟脚本（仅用于学习和本地测试）
"""

import time
from datetime import datetime

def simulate_ddos(target="192.168.1.1", packets=100):
    print(f"[{datetime.now()}] 🚀 开始模拟 DDoS 攻击 -> 目标: {target}")
    print("此脚本仅为学习演示，不会造成真实伤害\n")
    
    for i in range(1, packets + 1):
        print(f"[{datetime.now()}] 发送第 {i} 个伪造数据包...")
        time.sleep(0.05)  # 模拟发送间隔
    
    print(f"\n[{datetime.now()}] ✅ 模拟攻击完成！共发送 {packets} 个数据包")
    print("防御建议：使用 iptables 限流、启用云防护、配置 WAF")

if __name__ == "__main__":
    simulate_ddos()
