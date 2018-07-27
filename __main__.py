from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.workflow.orchestration.teardown.default_teardown_orchestrator import DefaultTeardownWorkflow
import Proc_L1ConnectionController as L1ConnectionController
from Work_Config import WorkConfig


def main():
    # Default Setup Process
    sandbox = Sandbox()
    DefaultTeardownWorkflow().register(sandbox)
    sandbox.execute_teardown()

    # Additional Setup Process
    # Connect All L1 Routes
    L1ConnectionController.ChangeStateOfAllL1Routes("Disconnect")

    # Set Config
    # insert code here
    work_config = WorkConfig()
    work_config.input_config_all("Init Config Path")


# Entry Point
if __name__ == "__main__":
    main()
