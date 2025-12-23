# Deep Vision Agent - 深度视觉智能体

> **轻量级 · 零标注成本 · 命令行驱动 · 免费多模态图像理解**

本项目基于智谱 AI 官方提供的 **GLM-4V-Flash** 多模态大模型，通过简洁的命令行接口实现通用图像语义理解。无需训练、无需标注、无需深度学习框架，仅依赖官方 SDK，开箱即用，快速完成多种视觉理解任务。

## ✨ 核心优势

- 🧠 **免费调用**：使用完全免费的 `glm-4v-flash` 多模态模型（截至 2025 年）
- 🚫 **零标注成本**：无需准备训练数据或人工标注，直接利用强大的预训练能力
- 📋 **6 类任务开箱即用**：
  - `image-class`：图像分类（返回关键词）
  - `visual-question`：自定义视觉问答（支持任意问题）
  - `count-target`：指定目标数量统计（如“汽车”“猫”等）
  - `caption`：生成一句话图像描述
  - `caption-detailed`：输出详细场景解析
  - `region-caption`：对局部区域进行语义描述
- 🖼️ **广泛兼容**：支持 JPG / PNG 格式图像（建议分辨率 ≤ 2048×2048）
- 🛠️ **模块化架构**：配置、API 调用、提示模板与任务逻辑解耦，便于二次开发与扩展

## 📦 安装依赖

```bash
pip install zhipuai
```

无需 OpenCV、PyTorch、Transformers 等重型库 —— 纯 API 调用！

## 🔑 配置 API Key

方法一：修改 config.py（快速测试）

```python
# config.py
API_KEY = "your_actual_api_key_here"
```

方法二：使用环境变量（推荐，安全）

```bash
export ZHIPUAI_API_KEY="your_actual_api_key_here"
```

并确保 api_client.py 中使用如下方式初始化：

```python
import os
from zhipuai import ZhipuAI

client = ZhipuAI(api_key=os.getenv("ZHIPUAI_API_KEY"))
```

获取 API Key：智谱开放平台

## 🚀 使用方法

```bash
python main.py <图像路径> [提示词] <任务类型>
```

测试命令

```bash
python main.py test.jpg "" caption-detailed
```

```bash
# 图像分类
python main.py photo.jpg "" image-class

# 视觉问答（必须提供问题）
python main.py street.jpg "图中有几辆自行车？" visual-question

# 目标计数（自动套用模板）
python main.py living_room.jpg "椅子" count-target
# → 实际提问："图中有多少个椅子？只输出一个数字。"

# 详细描述
python main.py test.jpg "" caption-detailed

# 区域描述（需提前裁剪子图）
python main.py cropped_region.jpg "" region-caption
```

## 📁 项目结构

```text
.
├── main.py                # 命令行入口
├── config.py              # API 密钥配置（可选）
├── api_client.py          # GLM-4V-Flash API 封装
├── prompts_templates.py   # 任务提示模板
└── task_processor.py      # 任务路由与 prompt 构建
```

## 📜 许可证

MIT License

## 💖 关于作者
如果你觉得它对你有帮助：

✅ 点个 Star 是最大的鼓励！
💬 欢迎提 Issue 或 PR，一起让它变得更好
📧 联系邮箱：shaoycamore@gmail.com
（可用于合作或反馈建议）

