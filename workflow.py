from flytekit import workflow
from flytekit.types.file import FlyteFile
from typing import TypeVar, NamedTuple
from flytekitplugins.domino.helpers import Input, Output, run_domino_job_task
from flytekitplugins.domino.task import DominoJobConfig, DominoJobTask, GitRef, EnvironmentRevisionSpecification, EnvironmentRevisionType, DatasetSnapshot

# pyflyte run --remote workflow.py hardcoded_inputs
@workflow
def hardcoded_inputs() -> NamedTuple("final_outputs", adam=FlyteFile[TypeVar("sas7bdat")]):

    results = run_domino_job_task(
        flyte_task_name="Merge data",
        command="prod/adam-hardcoded.py",
        output_spec=[Output(name="adam", type=FlyteFile[TypeVar("sas7bdat")])],
        dataset_snapshots=[
            DatasetSnapshot(Id="66da0221e651b51a171f2e47", Version=1), # DatasetA
            DatasetSnapshot(Id="66da023ee651b51a171f2e4c", Version=1), # DatasetB
            DatasetSnapshot(Id="66da02604d3b8b676a1b9460", Version=1) # DatasetC
        ],
        environment_name="SAS Analytics Pro",
        use_project_defaults_for_omitted=True
    )

    return results["adam"]
