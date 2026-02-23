from planner import create_plan
from executor import execute_plan
from state import AgentState
from metadata import extract_metadata


def main():
    user_request = "Trim video start=10s and ending at 40s and remove the silence."
    state = AgentState("test.mov")

    metadata = extract_metadata(state.video_input_path)
    state.metadata = metadata

    plan = create_plan(user_request, metadata)
    print("Generated Plan:", plan)
    state.plan = plan

    state = execute_plan(state)


if __name__ == "__main__":
    main()
