import json
from tools import trim_video, remove_silence, add_subtitles
from planner import Plan

TOOL_MAP = {
    "trim_video": trim_video,
    "remove_silence": remove_silence,
    "add_subtitles": add_subtitles,
}


def execute_plan(state):
    plan: Plan = state.plan

    for step in plan.steps:
        tool_name = step.tool
        params = step.params

        params["input_path"] = state.current_video_path

        output_path = f"output_{tool_name}.mp4"
        params["output_path"] = output_path

        tool_func = TOOL_MAP[tool_name]
        result = tool_func(**params)

        state.current_video_path = result
        state.artifacts.append(result)

    return state
