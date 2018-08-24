from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.workflow.orchestration.teardown.default_teardown_orchestrator import DefaultTeardownWorkflow
from Work_Config import WorkConfig


def main():
    # Default Setup Process
    sandbox = Sandbox()
    DefaultTeardownWorkflow().register(sandbox)
    sandbox.execute_teardown()

    # Set Config
    # insert code here
    work_config = WorkConfig()
    work_config.input_config_all("Init Config Path")


# Entry Point
if __name__ == "__main__":
    main()
