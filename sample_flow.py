import prefect
from prefect import task
from prefect import Flow
import requests


@task
def test_api(url):
    """Task to test the API.
    Parameters
    ----------
    url : str
        The URL to test.
    """

    data = None

    logger = prefect.context.get('logger')
    logger.info('Consuming the API')

    response = requests.get(url)
    logger.info(f'Response: {response.status_code}')
    logger.info(f'Data: {response.json()}')

    if response.status_code == 200:
        data = response.json()

    return data


@task
def return_activity(data):
    """Task to return the activity.
    Parameters
    ----------
    data : dict
        The data to return.
    """

    logger = prefect.context.get('logger')
    logger.info('Returning the activity')

    activity = data['activity']
    logger.info(f'Activity: {activity}')

    return activity


with Flow('hello-flow') as flow:
    raw_data = test_api('https://www.boredapi.com/api/activity')
    activity_name = return_activity(raw_data)

# Ejecución de un flujo
state = flow.run()

# Obtención de resultados por tarea
print(state.result[activity_name].result)

# Registro de flujo en la nube de Prefect
# flow.register(project_name='tester')
