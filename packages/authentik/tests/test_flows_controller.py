# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from authentik_openapi.models.cache import Cache
from authentik_openapi.models.challenge_types import ChallengeTypes
from authentik_openapi.models.file_path_request import FilePathRequest
from authentik_openapi.models.flow import Flow
from authentik_openapi.models.flow_challenge_response_request import FlowChallengeResponseRequest
from authentik_openapi.models.flow_diagram import FlowDiagram
from authentik_openapi.models.flow_import_result import FlowImportResult
from authentik_openapi.models.flow_inspection import FlowInspection
from authentik_openapi.models.flow_request import FlowRequest
from authentik_openapi.models.flow_stage_binding import FlowStageBinding
from authentik_openapi.models.flow_stage_binding_request import FlowStageBindingRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.link import Link
from authentik_openapi.models.paginated_flow_list import PaginatedFlowList
from authentik_openapi.models.paginated_flow_stage_binding_list import PaginatedFlowStageBindingList
from authentik_openapi.models.patched_flow_request import PatchedFlowRequest
from authentik_openapi.models.patched_flow_stage_binding_request import PatchedFlowStageBindingRequest
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_flows_bindings_create(client):
    """Test case for flows_bindings_create

    
    """
    body = {"policy_engine_mode":"all","stage":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","evaluate_on_plan":True,"re_evaluate_policies":True,"invalid_response_action":"","target":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","order":-1803530559}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/flows/bindings/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_bindings_destroy(client):
    """Test case for flows_bindings_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/flows/bindings/{fsb_uuid}'.format(fsb_uuid='fsb_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_bindings_list(client):
    """Test case for flows_bindings_list

    
    """
    params = [('evaluate_on_plan', True),
                    ('fsb_uuid', 'fsb_uuid_example'),
                    ('invalid_response_action', 'invalid_response_action_example'),
                    ('order', 56),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('pbm_uuid', 'pbm_uuid_example'),
                    ('policies', ['policies_example']),
                    ('policy_engine_mode', 'policy_engine_mode_example'),
                    ('re_evaluate_policies', True),
                    ('search', 'search_example'),
                    ('stage', 'stage_example'),
                    ('target', 'target_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/flows/bindings/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_bindings_partial_update(client):
    """Test case for flows_bindings_partial_update

    
    """
    body = {"policy_engine_mode":"all","stage":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","evaluate_on_plan":True,"re_evaluate_policies":True,"invalid_response_action":"","target":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","order":-1803530559}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/flows/bindings/{fsb_uuid}'.format(fsb_uuid='fsb_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_bindings_retrieve(client):
    """Test case for flows_bindings_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/flows/bindings/{fsb_uuid}'.format(fsb_uuid='fsb_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_bindings_update(client):
    """Test case for flows_bindings_update

    
    """
    body = {"policy_engine_mode":"all","stage":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","evaluate_on_plan":True,"re_evaluate_policies":True,"invalid_response_action":"","target":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","order":-1803530559}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/flows/bindings/{fsb_uuid}'.format(fsb_uuid='fsb_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_bindings_used_by_list(client):
    """Test case for flows_bindings_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/flows/bindings/{fsb_uuid}/used_by'.format(fsb_uuid='fsb_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_executor_get(client):
    """Test case for flows_executor_get

    
    """
    params = [('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/flows/executor/{flow_slug}'.format(flow_slug='flow_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_executor_solve(client):
    """Test case for flows_executor_solve

    
    """
    body = {"component":"ak-source-oauth-apple"}
    params = [('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/flows/executor/{flow_slug}'.format(flow_slug='flow_slug_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_inspector_get(client):
    """Test case for flows_inspector_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/flows/inspector/{flow_slug}'.format(flow_slug='flow_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_instances_cache_clear_create(client):
    """Test case for flows_instances_cache_clear_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/flows/instances/cache_clear/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_instances_cache_info_retrieve(client):
    """Test case for flows_instances_cache_info_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/flows/instances/cache_info/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_instances_create(client):
    """Test case for flows_instances_create

    
    """
    body = {"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug","authentication":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/flows/instances/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_instances_destroy(client):
    """Test case for flows_instances_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/flows/instances/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_instances_diagram_retrieve(client):
    """Test case for flows_instances_diagram_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/flows/instances/{slug}/diagram'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_instances_execute_retrieve(client):
    """Test case for flows_instances_execute_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/flows/instances/{slug}/execute'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_instances_export_retrieve(client):
    """Test case for flows_instances_export_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/flows/instances/{slug}/export'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_flows_instances_import_create(client):
    """Test case for flows_instances_import_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('clear', False)
    response = await client.request(
        method='POST',
        path='/api/v3/flows/instances/import/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_instances_list(client):
    """Test case for flows_instances_list

    
    """
    params = [('denied_action', 'denied_action_example'),
                    ('designation', 'designation_example'),
                    ('flow_uuid', 'flow_uuid_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('slug', 'slug_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/flows/instances/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_instances_partial_update(client):
    """Test case for flows_instances_partial_update

    
    """
    body = {"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug","authentication":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/flows/instances/{slug}'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_instances_retrieve(client):
    """Test case for flows_instances_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/flows/instances/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_flows_instances_set_background_create(client):
    """Test case for flows_instances_set_background_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('clear', False)
    response = await client.request(
        method='POST',
        path='/api/v3/flows/instances/{slug}/set_background'.format(slug='slug_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_instances_set_background_url_create(client):
    """Test case for flows_instances_set_background_url_create

    
    """
    body = {"url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/flows/instances/{slug}/set_background_url'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_instances_update(client):
    """Test case for flows_instances_update

    
    """
    body = {"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug","authentication":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/flows/instances/{slug}'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flows_instances_used_by_list(client):
    """Test case for flows_instances_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/flows/instances/{slug}/used_by'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

