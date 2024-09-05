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
        command="prod/adam-hardcoded.sas",
        environment_name="SAS Analytics Pro",
        dataset_snapshots=[
            DatasetSnapshot(Id="66da0221e651b51a171f2e47", Version=1), # DatasetA
            DatasetSnapshot(Id="66da023ee651b51a171f2e4c", Version=1), # DatasetB
            DatasetSnapshot(Id="66da02604d3b8b676a1b9460", Version=1) # DatasetC
        ],
        inputs=None,
        output_specs=[Output(name="adam", type=FlyteFile[TypeVar("sas7bdat")])],
        use_project_defaults_for_omitted=True
    )

    return results["adam"]

# pyflyte run --remote workflow.py variable_inputs --data_path_a /mnt/data/snapshots/DatasetA/1 --data_path_b /mnt/data/snapshots/DatasetB/1 --data_path_c /mnt/data/snapshots/DatasetC/1
@workflow
def variable_inputs(data_path_a: str, data_path_b: str, data_path_c: str) -> NamedTuple("final_outputs", adam=FlyteFile[TypeVar("sas7bdat")]):

    results = run_domino_job_task(
        flyte_task_name="Merge data",
        command="prod/adam-variable.py",
        environment_name="SAS Analytics Pro",
        inputs=[
            Input(name="data_path_a", type=str, value=data_path_a),
            Input(name="data_path_b", type=str, value=data_path_b),
            Input(name="data_path_c", type=str, value=data_path_c)
        ],
        output_specs=[Output(name="adam", type=FlyteFile[TypeVar("sas7bdat")])],
        use_project_defaults_for_omitted=True
    )

    return results["adam"]
