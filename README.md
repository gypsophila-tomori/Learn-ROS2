# ROS2学习与开发仓库

> 从入门到入土的ROS2机器人操作系统学习

## 📋 仓库概述

这是一个用于系统学习ROS2机器人操作系统的个人仓库，包含代码实践、配置文档和学习笔记。仓库结构按照"理论→实践→项目"的渐进式学习路径设计。

## 🛠️ 环境配置

### 系统要求
- **操作系统**: Ubuntu 24.04 LTS (Jammy)
- **ROS2版本**: Jazzy Jalisco
- **Python版本**: 3.12
- **编译器**: GCC 17

### 快速开始
```bash
# 1. 克隆仓库
git clone https://github.com/your-username/ros2-learning.git
cd ros2-learning

# 2. 环境准备（首次使用）
./scripts/setup.sh

# 3. 构建工作空间
cd workspace
colcon build --symlink-install

# 4. 激活环境
source install/setup.bash
