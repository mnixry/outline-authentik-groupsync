# coding: utf-8

import pytest
import json
from aiohttp import web

from authentik_openapi.models.cache import Cache
from authentik_openapi.models.detailed_country import DetailedCountry
from authentik_openapi.models.dummy_policy import DummyPolicy
from authentik_openapi.models.dummy_policy_request import DummyPolicyRequest
from authentik_openapi.models.event_matcher_policy import EventMatcherPolicy
from authentik_openapi.models.event_matcher_policy_request import EventMatcherPolicyRequest
from authentik_openapi.models.expression_policy import ExpressionPolicy
from authentik_openapi.models.expression_policy_request import ExpressionPolicyRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.geo_ip_policy import GeoIPPolicy
from authentik_openapi.models.geo_ip_policy_request import GeoIPPolicyRequest
from authentik_openapi.models.paginated_dummy_policy_list import PaginatedDummyPolicyList
from authentik_openapi.models.paginated_event_matcher_policy_list import PaginatedEventMatcherPolicyList
from authentik_openapi.models.paginated_expression_policy_list import PaginatedExpressionPolicyList
from authentik_openapi.models.paginated_geo_ip_policy_list import PaginatedGeoIPPolicyList
from authentik_openapi.models.paginated_password_expiry_policy_list import PaginatedPasswordExpiryPolicyList
from authentik_openapi.models.paginated_password_policy_list import PaginatedPasswordPolicyList
from authentik_openapi.models.paginated_policy_binding_list import PaginatedPolicyBindingList
from authentik_openapi.models.paginated_policy_list import PaginatedPolicyList
from authentik_openapi.models.paginated_reputation_list import PaginatedReputationList
from authentik_openapi.models.paginated_reputation_policy_list import PaginatedReputationPolicyList
from authentik_openapi.models.password_expiry_policy import PasswordExpiryPolicy
from authentik_openapi.models.password_expiry_policy_request import PasswordExpiryPolicyRequest
from authentik_openapi.models.password_policy import PasswordPolicy
from authentik_openapi.models.password_policy_request import PasswordPolicyRequest
from authentik_openapi.models.patched_dummy_policy_request import PatchedDummyPolicyRequest
from authentik_openapi.models.patched_event_matcher_policy_request import PatchedEventMatcherPolicyRequest
from authentik_openapi.models.patched_expression_policy_request import PatchedExpressionPolicyRequest
from authentik_openapi.models.patched_geo_ip_policy_request import PatchedGeoIPPolicyRequest
from authentik_openapi.models.patched_password_expiry_policy_request import PatchedPasswordExpiryPolicyRequest
from authentik_openapi.models.patched_password_policy_request import PatchedPasswordPolicyRequest
from authentik_openapi.models.patched_policy_binding_request import PatchedPolicyBindingRequest
from authentik_openapi.models.patched_reputation_policy_request import PatchedReputationPolicyRequest
from authentik_openapi.models.policy import Policy
from authentik_openapi.models.policy_binding import PolicyBinding
from authentik_openapi.models.policy_binding_request import PolicyBindingRequest
from authentik_openapi.models.policy_test_request import PolicyTestRequest
from authentik_openapi.models.policy_test_result import PolicyTestResult
from authentik_openapi.models.reputation import Reputation
from authentik_openapi.models.reputation_policy import ReputationPolicy
from authentik_openapi.models.reputation_policy_request import ReputationPolicyRequest
from authentik_openapi.models.type_create import TypeCreate
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_policies_all_cache_clear_create(client):
    """Test case for policies_all_cache_clear_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/policies/all/cache_clear/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_all_cache_info_retrieve(client):
    """Test case for policies_all_cache_info_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/all/cache_info/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_all_destroy(client):
    """Test case for policies_all_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/policies/all/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_all_list(client):
    """Test case for policies_all_list

    
    """
    params = [('bindings__isnull', True),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('promptstage__isnull', True),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/all/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_all_retrieve(client):
    """Test case for policies_all_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/all/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_all_test_create(client):
    """Test case for policies_all_test_create

    
    """
    body = {"context":{"key":""},"user":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/policies/all/{policy_uuid}/test'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_all_types_list(client):
    """Test case for policies_all_types_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/all/types/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_all_used_by_list(client):
    """Test case for policies_all_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/all/{policy_uuid}/used_by'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_bindings_create(client):
    """Test case for policies_bindings_create

    
    """
    body = {"negate":True,"failure_result":True,"user":0,"enabled":True,"timeout":314780940,"policy":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","target":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","order":441289069}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/policies/bindings/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_bindings_destroy(client):
    """Test case for policies_bindings_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/policies/bindings/{policy_binding_uuid}'.format(policy_binding_uuid='policy_binding_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_bindings_list(client):
    """Test case for policies_bindings_list

    
    """
    params = [('enabled', True),
                    ('order', 56),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('policy', 'policy_example'),
                    ('policy__isnull', True),
                    ('search', 'search_example'),
                    ('target', 'target_example'),
                    ('target_in', ['target_in_example']),
                    ('timeout', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/bindings/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_bindings_partial_update(client):
    """Test case for policies_bindings_partial_update

    
    """
    body = {"negate":True,"failure_result":True,"user":0,"enabled":True,"timeout":314780940,"policy":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","target":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","order":441289069}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/policies/bindings/{policy_binding_uuid}'.format(policy_binding_uuid='policy_binding_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_bindings_retrieve(client):
    """Test case for policies_bindings_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/bindings/{policy_binding_uuid}'.format(policy_binding_uuid='policy_binding_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_bindings_update(client):
    """Test case for policies_bindings_update

    
    """
    body = {"negate":True,"failure_result":True,"user":0,"enabled":True,"timeout":314780940,"policy":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","target":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","order":441289069}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/policies/bindings/{policy_binding_uuid}'.format(policy_binding_uuid='policy_binding_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_bindings_used_by_list(client):
    """Test case for policies_bindings_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/bindings/{policy_binding_uuid}/used_by'.format(policy_binding_uuid='policy_binding_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_dummy_create(client):
    """Test case for policies_dummy_create

    
    """
    body = {"result":True,"execution_logging":True,"name":"name","wait_min":-1803530559,"wait_max":441289069}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/policies/dummy/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_dummy_destroy(client):
    """Test case for policies_dummy_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/policies/dummy/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_dummy_list(client):
    """Test case for policies_dummy_list

    
    """
    params = [('created', '2013-10-20T19:20:30+01:00'),
                    ('execution_logging', True),
                    ('last_updated', '2013-10-20T19:20:30+01:00'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('policy_uuid', 'policy_uuid_example'),
                    ('result', True),
                    ('search', 'search_example'),
                    ('wait_max', 56),
                    ('wait_min', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/dummy/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_dummy_partial_update(client):
    """Test case for policies_dummy_partial_update

    
    """
    body = {"result":True,"execution_logging":True,"name":"name","wait_min":-1803530559,"wait_max":441289069}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/policies/dummy/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_dummy_retrieve(client):
    """Test case for policies_dummy_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/dummy/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_dummy_update(client):
    """Test case for policies_dummy_update

    
    """
    body = {"result":True,"execution_logging":True,"name":"name","wait_min":-1803530559,"wait_max":441289069}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/policies/dummy/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_dummy_used_by_list(client):
    """Test case for policies_dummy_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/dummy/{policy_uuid}/used_by'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_event_matcher_create(client):
    """Test case for policies_event_matcher_create

    
    """
    body = {"app":"","execution_logging":True,"name":"name","action":"","client_ip":"client_ip","model":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/policies/event_matcher/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_event_matcher_destroy(client):
    """Test case for policies_event_matcher_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/policies/event_matcher/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_event_matcher_list(client):
    """Test case for policies_event_matcher_list

    
    """
    params = [('action', 'action_example'),
                    ('app', 'app_example'),
                    ('client_ip', 'client_ip_example'),
                    ('created', '2013-10-20T19:20:30+01:00'),
                    ('execution_logging', True),
                    ('last_updated', '2013-10-20T19:20:30+01:00'),
                    ('model', 'model_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('policy_uuid', 'policy_uuid_example'),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/event_matcher/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_event_matcher_partial_update(client):
    """Test case for policies_event_matcher_partial_update

    
    """
    body = {"app":"","execution_logging":True,"name":"name","action":"","client_ip":"client_ip","model":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/policies/event_matcher/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_event_matcher_retrieve(client):
    """Test case for policies_event_matcher_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/event_matcher/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_event_matcher_update(client):
    """Test case for policies_event_matcher_update

    
    """
    body = {"app":"","execution_logging":True,"name":"name","action":"","client_ip":"client_ip","model":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/policies/event_matcher/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_event_matcher_used_by_list(client):
    """Test case for policies_event_matcher_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/event_matcher/{policy_uuid}/used_by'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_expression_create(client):
    """Test case for policies_expression_create

    
    """
    body = {"expression":"expression","execution_logging":True,"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/policies/expression/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_expression_destroy(client):
    """Test case for policies_expression_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/policies/expression/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_expression_list(client):
    """Test case for policies_expression_list

    
    """
    params = [('created', '2013-10-20T19:20:30+01:00'),
                    ('execution_logging', True),
                    ('expression', 'expression_example'),
                    ('last_updated', '2013-10-20T19:20:30+01:00'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('policy_uuid', 'policy_uuid_example'),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/expression/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_expression_partial_update(client):
    """Test case for policies_expression_partial_update

    
    """
    body = {"expression":"expression","execution_logging":True,"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/policies/expression/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_expression_retrieve(client):
    """Test case for policies_expression_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/expression/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_expression_update(client):
    """Test case for policies_expression_update

    
    """
    body = {"expression":"expression","execution_logging":True,"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/policies/expression/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_expression_used_by_list(client):
    """Test case for policies_expression_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/expression/{policy_uuid}/used_by'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_geoip_create(client):
    """Test case for policies_geoip_create

    
    """
    body = {"execution_logging":True,"name":"name","asns":[-1803530559,-1803530559],"countries":["AF","AF","AF","AF","AF"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/policies/geoip/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_geoip_destroy(client):
    """Test case for policies_geoip_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/policies/geoip/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_geoip_iso3166_list(client):
    """Test case for policies_geoip_iso3166_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/geoip_iso3166/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_geoip_list(client):
    """Test case for policies_geoip_list

    
    """
    params = [('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/geoip/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_geoip_partial_update(client):
    """Test case for policies_geoip_partial_update

    
    """
    body = {"execution_logging":True,"name":"name","asns":[-1803530559,-1803530559],"countries":["AF","AF","AF","AF","AF"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/policies/geoip/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_geoip_retrieve(client):
    """Test case for policies_geoip_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/geoip/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_geoip_update(client):
    """Test case for policies_geoip_update

    
    """
    body = {"execution_logging":True,"name":"name","asns":[-1803530559,-1803530559],"countries":["AF","AF","AF","AF","AF"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/policies/geoip/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_geoip_used_by_list(client):
    """Test case for policies_geoip_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/geoip/{policy_uuid}/used_by'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_password_create(client):
    """Test case for policies_password_create

    
    """
    body = {"error_message":"error_message","amount_symbols":1280358508,"amount_lowercase":314780940,"execution_logging":True,"check_have_i_been_pwned":True,"check_zxcvbn":True,"amount_uppercase":1294386358,"length_min":1210617418,"password_field":"password_field","amount_digits":171976544,"check_static_rules":True,"symbol_charset":"symbol_charset","name":"name","zxcvbn_score_threshold":1516424369,"hibp_allowed_count":494379917}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/policies/password/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_password_destroy(client):
    """Test case for policies_password_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/policies/password/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_password_expiry_create(client):
    """Test case for policies_password_expiry_create

    
    """
    body = {"execution_logging":True,"deny_only":True,"name":"name","days":-1803530559}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/policies/password_expiry/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_password_expiry_destroy(client):
    """Test case for policies_password_expiry_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/policies/password_expiry/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_password_expiry_list(client):
    """Test case for policies_password_expiry_list

    
    """
    params = [('created', '2013-10-20T19:20:30+01:00'),
                    ('days', 56),
                    ('deny_only', True),
                    ('execution_logging', True),
                    ('last_updated', '2013-10-20T19:20:30+01:00'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('policy_uuid', 'policy_uuid_example'),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/password_expiry/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_password_expiry_partial_update(client):
    """Test case for policies_password_expiry_partial_update

    
    """
    body = {"execution_logging":True,"deny_only":True,"name":"name","days":-1803530559}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/policies/password_expiry/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_password_expiry_retrieve(client):
    """Test case for policies_password_expiry_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/password_expiry/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_password_expiry_update(client):
    """Test case for policies_password_expiry_update

    
    """
    body = {"execution_logging":True,"deny_only":True,"name":"name","days":-1803530559}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/policies/password_expiry/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_password_expiry_used_by_list(client):
    """Test case for policies_password_expiry_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/password_expiry/{policy_uuid}/used_by'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_password_list(client):
    """Test case for policies_password_list

    
    """
    params = [('amount_digits', 56),
                    ('amount_lowercase', 56),
                    ('amount_symbols', 56),
                    ('amount_uppercase', 56),
                    ('check_have_i_been_pwned', True),
                    ('check_static_rules', True),
                    ('check_zxcvbn', True),
                    ('created', '2013-10-20T19:20:30+01:00'),
                    ('error_message', 'error_message_example'),
                    ('execution_logging', True),
                    ('hibp_allowed_count', 56),
                    ('last_updated', '2013-10-20T19:20:30+01:00'),
                    ('length_min', 56),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('password_field', 'password_field_example'),
                    ('policy_uuid', 'policy_uuid_example'),
                    ('search', 'search_example'),
                    ('symbol_charset', 'symbol_charset_example'),
                    ('zxcvbn_score_threshold', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/password/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_password_partial_update(client):
    """Test case for policies_password_partial_update

    
    """
    body = {"error_message":"error_message","amount_symbols":1280358508,"amount_lowercase":314780940,"execution_logging":True,"check_have_i_been_pwned":True,"check_zxcvbn":True,"amount_uppercase":1294386358,"length_min":1210617418,"password_field":"password_field","amount_digits":171976544,"check_static_rules":True,"symbol_charset":"symbol_charset","name":"name","zxcvbn_score_threshold":1516424369,"hibp_allowed_count":494379917}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/policies/password/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_password_retrieve(client):
    """Test case for policies_password_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/password/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_password_update(client):
    """Test case for policies_password_update

    
    """
    body = {"error_message":"error_message","amount_symbols":1280358508,"amount_lowercase":314780940,"execution_logging":True,"check_have_i_been_pwned":True,"check_zxcvbn":True,"amount_uppercase":1294386358,"length_min":1210617418,"password_field":"password_field","amount_digits":171976544,"check_static_rules":True,"symbol_charset":"symbol_charset","name":"name","zxcvbn_score_threshold":1516424369,"hibp_allowed_count":494379917}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/policies/password/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_password_used_by_list(client):
    """Test case for policies_password_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/password/{policy_uuid}/used_by'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_reputation_create(client):
    """Test case for policies_reputation_create

    
    """
    body = {"check_ip":True,"execution_logging":True,"name":"name","check_username":True,"threshold":-1803530559}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/policies/reputation/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_reputation_destroy(client):
    """Test case for policies_reputation_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/policies/reputation/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_reputation_list(client):
    """Test case for policies_reputation_list

    
    """
    params = [('check_ip', True),
                    ('check_username', True),
                    ('created', '2013-10-20T19:20:30+01:00'),
                    ('execution_logging', True),
                    ('last_updated', '2013-10-20T19:20:30+01:00'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('policy_uuid', 'policy_uuid_example'),
                    ('search', 'search_example'),
                    ('threshold', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/reputation/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_reputation_partial_update(client):
    """Test case for policies_reputation_partial_update

    
    """
    body = {"check_ip":True,"execution_logging":True,"name":"name","check_username":True,"threshold":-1803530559}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/policies/reputation/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_reputation_retrieve(client):
    """Test case for policies_reputation_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/reputation/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_reputation_scores_destroy(client):
    """Test case for policies_reputation_scores_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/policies/reputation/scores/{reputation_uuid}'.format(reputation_uuid='reputation_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_reputation_scores_list(client):
    """Test case for policies_reputation_scores_list

    
    """
    params = [('identifier', 'identifier_example'),
                    ('identifier_in', ['identifier_in_example']),
                    ('ip', 'ip_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('score', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/reputation/scores/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_reputation_scores_retrieve(client):
    """Test case for policies_reputation_scores_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/reputation/scores/{reputation_uuid}'.format(reputation_uuid='reputation_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_reputation_scores_used_by_list(client):
    """Test case for policies_reputation_scores_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/reputation/scores/{reputation_uuid}/used_by'.format(reputation_uuid='reputation_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_reputation_update(client):
    """Test case for policies_reputation_update

    
    """
    body = {"check_ip":True,"execution_logging":True,"name":"name","check_username":True,"threshold":-1803530559}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/policies/reputation/{policy_uuid}'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_reputation_used_by_list(client):
    """Test case for policies_reputation_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/policies/reputation/{policy_uuid}/used_by'.format(policy_uuid='policy_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

