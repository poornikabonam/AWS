import sagemaker
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.steps import TrainingStep
from sagemaker.inputs import TrainingInput
from sagemaker.estimator import Estimator

# Define parameters
training_data_uri = 's3://titanic-dataset/train.csv'
model_output_uri = 's3://titanic-dataset/model/'

# SageMaker Session and Role
sagemaker_session = sagemaker.Session()
role = sagemaker.get_execution_role()

# Define the Estimator
estimator = Estimator(
    image_uri='your_docker_image_uri',
    role=role,
    instance_type='ml.m5.large',
    instance_count=1,
    output_path=model_output_uri,
    sagemaker_session=sagemaker_session
)

# Define the training step
train_step = TrainingStep(
    name='TrainModel',
    estimator=estimator,
    inputs={'train': TrainingInput(s3_data=training_data_uri)}
)

pipeline = Pipeline(
    name='MLPipeline',
    steps=[train_step],
    sagemaker_session=sagemaker_session
)

pipeline_definition = pipeline.definition()
with open('pipeline_definition.json', 'w') as f:
    f.write(pipeline_definition)
