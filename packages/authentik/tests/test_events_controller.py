# coding: utf-8

import pytest
import json
from aiohttp import web

from authentik_openapi.models.coordinate import Coordinate
from authentik_openapi.models.event import Event
from authentik_openapi.models.event_request import EventRequest
from authentik_openapi.models.event_top_per_user import EventTopPerUser
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.notification import Notification
from authentik_openapi.models.notification_request import NotificationRequest
from authentik_openapi.models.notification_rule import NotificationRule
from authentik_openapi.models.notification_rule_request import NotificationRuleRequest
from authentik_openapi.models.notification_transport import NotificationTransport
from authentik_openapi.models.notification_transport_request import NotificationTransportRequest
from authentik_openapi.models.notification_transport_test import NotificationTransportTest
from authentik_openapi.models.paginated_event_list import PaginatedEventList
from authentik_openapi.models.paginated_notification_list import PaginatedNotificationList
from authentik_openapi.models.paginated_notification_rule_list import PaginatedNotificationRuleList
from authentik_openapi.models.paginated_notification_transport_list import PaginatedNotificationTransportList
from authentik_openapi.models.paginated_system_task_list import PaginatedSystemTaskList
from authentik_openapi.models.patched_event_request import PatchedEventRequest
from authentik_openapi.models.patched_notification_request import PatchedNotificationRequest
from authentik_openapi.models.patched_notification_rule_request import PatchedNotificationRuleRequest
from authentik_openapi.models.patched_notification_transport_request import PatchedNotificationTransportRequest
from authentik_openapi.models.system_task import SystemTask
from authentik_openapi.models.type_create import TypeCreate
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_events_events_actions_list(client):
    """Test case for events_events_actions_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/events/actions/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_events_create(client):
    """Test case for events_events_create

    
    """
    body = {"app":"app","expires":"2000-01-23T04:56:07.000+00:00","context":"","action":"login","client_ip":"client_ip","user":"","brand":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/events/events/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_events_destroy(client):
    """Test case for events_events_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/events/events/{event_uuid}'.format(event_uuid='event_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_events_list(client):
    """Test case for events_events_list

    
    """
    params = [('action', 'action_example'),
                    ('brand_name', 'brand_name_example'),
                    ('client_ip', 'client_ip_example'),
                    ('context_authorized_app', 'context_authorized_app_example'),
                    ('context_model_app', 'context_model_app_example'),
                    ('context_model_name', 'context_model_name_example'),
                    ('context_model_pk', 'context_model_pk_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('username', 'username_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/events/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_events_partial_update(client):
    """Test case for events_events_partial_update

    
    """
    body = {"app":"app","expires":"2000-01-23T04:56:07.000+00:00","context":"","action":"login","client_ip":"client_ip","user":"","brand":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/events/events/{event_uuid}'.format(event_uuid='event_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_events_per_month_list(client):
    """Test case for events_events_per_month_list

    
    """
    params = [('action', 'action_example'),
                    ('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/events/per_month/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_events_retrieve(client):
    """Test case for events_events_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/events/{event_uuid}'.format(event_uuid='event_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_events_top_per_user_list(client):
    """Test case for events_events_top_per_user_list

    
    """
    params = [('action', 'action_example'),
                    ('top_n', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/events/top_per_user/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_events_update(client):
    """Test case for events_events_update

    
    """
    body = {"app":"app","expires":"2000-01-23T04:56:07.000+00:00","context":"","action":"login","client_ip":"client_ip","user":"","brand":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/events/events/{event_uuid}'.format(event_uuid='event_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_events_volume_list(client):
    """Test case for events_events_volume_list

    
    """
    params = [('action', 'action_example'),
                    ('brand_name', 'brand_name_example'),
                    ('client_ip', 'client_ip_example'),
                    ('context_authorized_app', 'context_authorized_app_example'),
                    ('context_model_app', 'context_model_app_example'),
                    ('context_model_name', 'context_model_name_example'),
                    ('context_model_pk', 'context_model_pk_example'),
                    ('ordering', 'ordering_example'),
                    ('search', 'search_example'),
                    ('username', 'username_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/events/volume/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_notifications_destroy(client):
    """Test case for events_notifications_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/events/notifications/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_notifications_list(client):
    """Test case for events_notifications_list

    
    """
    params = [('body', 'body_example'),
                    ('created', '2013-10-20T19:20:30+01:00'),
                    ('event', 'event_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('seen', True),
                    ('severity', 'severity_example'),
                    ('user', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/notifications/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_notifications_mark_all_seen_create(client):
    """Test case for events_notifications_mark_all_seen_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/events/notifications/mark_all_seen/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_notifications_partial_update(client):
    """Test case for events_notifications_partial_update

    
    """
    body = {"event":{"app":"app","expires":"2000-01-23T04:56:07.000+00:00","context":"","action":"login","client_ip":"client_ip","user":"","brand":""},"seen":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/events/notifications/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_notifications_retrieve(client):
    """Test case for events_notifications_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/notifications/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_notifications_update(client):
    """Test case for events_notifications_update

    
    """
    body = {"event":{"app":"app","expires":"2000-01-23T04:56:07.000+00:00","context":"","action":"login","client_ip":"client_ip","user":"","brand":""},"seen":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/events/notifications/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_notifications_used_by_list(client):
    """Test case for events_notifications_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/notifications/{uuid}/used_by'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_rules_create(client):
    """Test case for events_rules_create

    
    """
    body = {"severity":"","transports":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/events/rules/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_rules_destroy(client):
    """Test case for events_rules_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/events/rules/{pbm_uuid}'.format(pbm_uuid='pbm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_rules_list(client):
    """Test case for events_rules_list

    
    """
    params = [('group__name', 'group__name_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('severity', 'severity_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/rules/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_rules_partial_update(client):
    """Test case for events_rules_partial_update

    
    """
    body = {"severity":"","transports":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/events/rules/{pbm_uuid}'.format(pbm_uuid='pbm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_rules_retrieve(client):
    """Test case for events_rules_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/rules/{pbm_uuid}'.format(pbm_uuid='pbm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_rules_update(client):
    """Test case for events_rules_update

    
    """
    body = {"severity":"","transports":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/events/rules/{pbm_uuid}'.format(pbm_uuid='pbm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_rules_used_by_list(client):
    """Test case for events_rules_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/rules/{pbm_uuid}/used_by'.format(pbm_uuid='pbm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_system_tasks_list(client):
    """Test case for events_system_tasks_list

    
    """
    params = [('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('status', 'status_example'),
                    ('uid', 'uid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/system_tasks/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_system_tasks_retrieve(client):
    """Test case for events_system_tasks_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/system_tasks/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_system_tasks_run_create(client):
    """Test case for events_system_tasks_run_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/events/system_tasks/{uuid}/run'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_transports_create(client):
    """Test case for events_transports_create

    
    """
    body = {"mode":"local","webhook_url":"https://openapi-generator.tech","name":"name","webhook_mapping":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","send_once":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/events/transports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_transports_destroy(client):
    """Test case for events_transports_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/events/transports/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_transports_list(client):
    """Test case for events_transports_list

    
    """
    params = [('mode', 'mode_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('send_once', True),
                    ('webhook_url', 'webhook_url_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/transports/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_transports_partial_update(client):
    """Test case for events_transports_partial_update

    
    """
    body = {"mode":"local","webhook_url":"https://openapi-generator.tech","name":"name","webhook_mapping":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","send_once":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/events/transports/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_transports_retrieve(client):
    """Test case for events_transports_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/transports/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_transports_test_create(client):
    """Test case for events_transports_test_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/events/transports/{uuid}/test'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_transports_update(client):
    """Test case for events_transports_update

    
    """
    body = {"mode":"local","webhook_url":"https://openapi-generator.tech","name":"name","webhook_mapping":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","send_once":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/events/transports/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_transports_used_by_list(client):
    """Test case for events_transports_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/transports/{uuid}/used_by'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

