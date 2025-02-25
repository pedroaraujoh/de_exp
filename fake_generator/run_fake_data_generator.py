from dagster import job, op
import papermill as pm

@op
def execute_fake_data_generator(context):
    input_path = "C:/Users/pedro/Documents/Github/de_exp/de_exp/fake_generator/fake_data_generator.ipynb"
    output_path = "C:/Users/pedro/Documents/Github/de_exp/de_exp/fake_generator/dagster_output/execution_output.ipynb"

    try:
        pm.execute_notebook(input_path=input_path, output_path=output_path)
    except Exception as e:
        context.log.error(f"Erro ao executar o notebook: {str(e)}")
        raise

@job
def execute_pipeline():
    execute_fake_data_generator()