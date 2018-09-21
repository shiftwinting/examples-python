import client
from workflows.sequential_workflow import SequentialWorkflow
from workflows.parallel_workflow import ParallelWorkflow
from workflows.asynchronous_workflow import AsynchronousWorkflow
from workflows.event_workflow import EventWorkflow
from workflows.wait_workflow import WaitWorkflow
from workflows.version_workflow import VersionWorkflow
from workflows.version_workflow_v0 import VersionWorkflowV0
from workflows.version_workflow_v1 import VersionWorkflowV1
from workflows.version_workflow_v2 import VersionWorkflowV2
from workflows.wait_event_workflow import WaitEventWorkflow
from workflows.recursive.recursive_workflow import RecursiveWorkflow
from workflows.max_processing_time_workflow import MaxProcessingTimeWorkflow
