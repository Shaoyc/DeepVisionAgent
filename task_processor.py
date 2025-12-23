# task_processor.py

from prompts_templates import TASK_TEMPLATES
from api_client import infer_glm4v_flash

def process_task(image_path, user_prompt, task_type):
    if task_type == "visual-question":
        if not user_prompt:
            raise ValueError("visual-question 任务必须提供自然语言问题作为 prompt！")
        final_prompt = user_prompt
    elif task_type == "count-target":
        final_prompt = TASK_TEMPLATES["count-target"].format(target=user_prompt) if user_prompt else "图中有多少个目标？只输出一个数字。"
    else:
        final_prompt = user_prompt if user_prompt else TASK_TEMPLATES[task_type]

    return infer_glm4v_flash(image_path, final_prompt)