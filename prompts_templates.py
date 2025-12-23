# prompts_templates.py

TASK_TEMPLATES = {
    "image-class": "这张图像属于物品类型？请用1-3个关键词回答。",
    "visual-question": None,  # 必须由用户自定义问题
    "count-target": "图中有多少个{target}？只输出一个数字。",
    "caption": "用一句话描述这张图像的主要内容。",
    "caption-detailed": "详细描述图像中的物品类型、空间布局、主要结构和环境上下文。",
    "region-caption": "描述该局部区域的物品组成和特征。"
}