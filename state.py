class AgentState:
    def __init__(self, video_input_path):
        self.video_input_path = video_input_path
        self.current_video_path = video_input_path
        self.artifacts = []
        self.metadata = {}
        self.plan = None
