from typing import List, Dict
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
from authentik_openapi import util


async def events_events_actions_list(request: web.Request, ) -> web.Response:
    """events_events_actions_list

    Get all actions


    """
    return web.Response(status=200)


async def events_events_create(request: web.Request, body) -> web.Response:
    """events_events_create

    Event Read-Only Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = EventRequest.from_dict(body)
    return web.Response(status=200)


async def events_events_destroy(request: web.Request, event_uuid) -> web.Response:
    """events_events_destroy

    Event Read-Only Viewset

    :param event_uuid: A UUID string identifying this Event.
    :type event_uuid: str
    :type event_uuid: str

    """
    return web.Response(status=200)


async def events_events_list(request: web.Request, action=None, brand_name=None, client_ip=None, context_authorized_app=None, context_model_app=None, context_model_name=None, context_model_pk=None, ordering=None, page=None, page_size=None, search=None, username=None) -> web.Response:
    """events_events_list

    Event Read-Only Viewset

    :param action: 
    :type action: str
    :param brand_name: Brand name
    :type brand_name: str
    :param client_ip: 
    :type client_ip: str
    :param context_authorized_app: Context Authorized application
    :type context_authorized_app: str
    :param context_model_app: Context Model App
    :type context_model_app: str
    :param context_model_name: Context Model Name
    :type context_model_name: str
    :param context_model_pk: Context Model Primary Key
    :type context_model_pk: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param username: Username
    :type username: str

    """
    return web.Response(status=200)


async def events_events_partial_update(request: web.Request, event_uuid, body=None) -> web.Response:
    """events_events_partial_update

    Event Read-Only Viewset

    :param event_uuid: A UUID string identifying this Event.
    :type event_uuid: str
    :type event_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedEventRequest.from_dict(body)
    return web.Response(status=200)


async def events_events_per_month_list(request: web.Request, action=None, query=None) -> web.Response:
    """events_events_per_month_list

    Get the count of events per month

    :param action: 
    :type action: str
    :param query: 
    :type query: str

    """
    return web.Response(status=200)


async def events_events_retrieve(request: web.Request, event_uuid) -> web.Response:
    """events_events_retrieve

    Event Read-Only Viewset

    :param event_uuid: A UUID string identifying this Event.
    :type event_uuid: str
    :type event_uuid: str

    """
    return web.Response(status=200)


async def events_events_top_per_user_list(request: web.Request, action=None, top_n=None) -> web.Response:
    """events_events_top_per_user_list

    Get the top_n events grouped by user count

    :param action: 
    :type action: str
    :param top_n: 
    :type top_n: int

    """
    return web.Response(status=200)


async def events_events_update(request: web.Request, event_uuid, body) -> web.Response:
    """events_events_update

    Event Read-Only Viewset

    :param event_uuid: A UUID string identifying this Event.
    :type event_uuid: str
    :type event_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = EventRequest.from_dict(body)
    return web.Response(status=200)


async def events_events_volume_list(request: web.Request, action=None, brand_name=None, client_ip=None, context_authorized_app=None, context_model_app=None, context_model_name=None, context_model_pk=None, ordering=None, search=None, username=None) -> web.Response:
    """events_events_volume_list

    Get event volume for specified filters and timeframe

    :param action: 
    :type action: str
    :param brand_name: Brand name
    :type brand_name: str
    :param client_ip: 
    :type client_ip: str
    :param context_authorized_app: Context Authorized application
    :type context_authorized_app: str
    :param context_model_app: Context Model App
    :type context_model_app: str
    :param context_model_name: Context Model Name
    :type context_model_name: str
    :param context_model_pk: Context Model Primary Key
    :type context_model_pk: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param search: A search term.
    :type search: str
    :param username: Username
    :type username: str

    """
    return web.Response(status=200)


async def events_notifications_destroy(request: web.Request, uuid) -> web.Response:
    """events_notifications_destroy

    Notification Viewset

    :param uuid: A UUID string identifying this Notification.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def events_notifications_list(request: web.Request, body=None, created=None, event=None, ordering=None, page=None, page_size=None, search=None, seen=None, severity=None, user=None) -> web.Response:
    """events_notifications_list

    Notification Viewset

    :param body: 
    :type body: str
    :param created: 
    :type created: str
    :param event: 
    :type event: str
    :type event: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param seen: 
    :type seen: bool
    :param severity: 
    :type severity: str
    :param user: 
    :type user: int

    """
    created = util.deserialize_datetime(created)
    return web.Response(status=200)


async def events_notifications_mark_all_seen_create(request: web.Request, ) -> web.Response:
    """events_notifications_mark_all_seen_create

    Mark all the user&#39;s notifications as seen


    """
    return web.Response(status=200)


async def events_notifications_partial_update(request: web.Request, uuid, body=None) -> web.Response:
    """events_notifications_partial_update

    Notification Viewset

    :param uuid: A UUID string identifying this Notification.
    :type uuid: str
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedNotificationRequest.from_dict(body)
    return web.Response(status=200)


async def events_notifications_retrieve(request: web.Request, uuid) -> web.Response:
    """events_notifications_retrieve

    Notification Viewset

    :param uuid: A UUID string identifying this Notification.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def events_notifications_update(request: web.Request, uuid, body=None) -> web.Response:
    """events_notifications_update

    Notification Viewset

    :param uuid: A UUID string identifying this Notification.
    :type uuid: str
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = NotificationRequest.from_dict(body)
    return web.Response(status=200)


async def events_notifications_used_by_list(request: web.Request, uuid) -> web.Response:
    """events_notifications_used_by_list

    Get a list of all objects that use this object

    :param uuid: A UUID string identifying this Notification.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def events_rules_create(request: web.Request, body) -> web.Response:
    """events_rules_create

    NotificationRule Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = NotificationRuleRequest.from_dict(body)
    return web.Response(status=200)


async def events_rules_destroy(request: web.Request, pbm_uuid) -> web.Response:
    """events_rules_destroy

    NotificationRule Viewset

    :param pbm_uuid: A UUID string identifying this Notification Rule.
    :type pbm_uuid: str
    :type pbm_uuid: str

    """
    return web.Response(status=200)


async def events_rules_list(request: web.Request, group__name=None, name=None, ordering=None, page=None, page_size=None, search=None, severity=None) -> web.Response:
    """events_rules_list

    NotificationRule Viewset

    :param group__name: 
    :type group__name: str
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param severity: Controls which severity level the created notifications will have.  
    :type severity: str

    """
    return web.Response(status=200)


async def events_rules_partial_update(request: web.Request, pbm_uuid, body=None) -> web.Response:
    """events_rules_partial_update

    NotificationRule Viewset

    :param pbm_uuid: A UUID string identifying this Notification Rule.
    :type pbm_uuid: str
    :type pbm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedNotificationRuleRequest.from_dict(body)
    return web.Response(status=200)


async def events_rules_retrieve(request: web.Request, pbm_uuid) -> web.Response:
    """events_rules_retrieve

    NotificationRule Viewset

    :param pbm_uuid: A UUID string identifying this Notification Rule.
    :type pbm_uuid: str
    :type pbm_uuid: str

    """
    return web.Response(status=200)


async def events_rules_update(request: web.Request, pbm_uuid, body) -> web.Response:
    """events_rules_update

    NotificationRule Viewset

    :param pbm_uuid: A UUID string identifying this Notification Rule.
    :type pbm_uuid: str
    :type pbm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = NotificationRuleRequest.from_dict(body)
    return web.Response(status=200)


async def events_rules_used_by_list(request: web.Request, pbm_uuid) -> web.Response:
    """events_rules_used_by_list

    Get a list of all objects that use this object

    :param pbm_uuid: A UUID string identifying this Notification Rule.
    :type pbm_uuid: str
    :type pbm_uuid: str

    """
    return web.Response(status=200)


async def events_system_tasks_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None, status=None, uid=None) -> web.Response:
    """events_system_tasks_list

    Read-only view set that returns all background tasks

    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param status: 
    :type status: str
    :param uid: 
    :type uid: str

    """
    return web.Response(status=200)


async def events_system_tasks_retrieve(request: web.Request, uuid) -> web.Response:
    """events_system_tasks_retrieve

    Read-only view set that returns all background tasks

    :param uuid: A UUID string identifying this System Task.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def events_system_tasks_run_create(request: web.Request, uuid) -> web.Response:
    """events_system_tasks_run_create

    Run task

    :param uuid: A UUID string identifying this System Task.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def events_transports_create(request: web.Request, body) -> web.Response:
    """events_transports_create

    NotificationTransport Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = NotificationTransportRequest.from_dict(body)
    return web.Response(status=200)


async def events_transports_destroy(request: web.Request, uuid) -> web.Response:
    """events_transports_destroy

    NotificationTransport Viewset

    :param uuid: A UUID string identifying this Notification Transport.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def events_transports_list(request: web.Request, mode=None, name=None, ordering=None, page=None, page_size=None, search=None, send_once=None, webhook_url=None) -> web.Response:
    """events_transports_list

    NotificationTransport Viewset

    :param mode: 
    :type mode: str
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param send_once: 
    :type send_once: bool
    :param webhook_url: 
    :type webhook_url: str

    """
    return web.Response(status=200)


async def events_transports_partial_update(request: web.Request, uuid, body=None) -> web.Response:
    """events_transports_partial_update

    NotificationTransport Viewset

    :param uuid: A UUID string identifying this Notification Transport.
    :type uuid: str
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedNotificationTransportRequest.from_dict(body)
    return web.Response(status=200)


async def events_transports_retrieve(request: web.Request, uuid) -> web.Response:
    """events_transports_retrieve

    NotificationTransport Viewset

    :param uuid: A UUID string identifying this Notification Transport.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def events_transports_test_create(request: web.Request, uuid) -> web.Response:
    """events_transports_test_create

    Send example notification using selected transport. Requires Modify permissions.

    :param uuid: A UUID string identifying this Notification Transport.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def events_transports_update(request: web.Request, uuid, body) -> web.Response:
    """events_transports_update

    NotificationTransport Viewset

    :param uuid: A UUID string identifying this Notification Transport.
    :type uuid: str
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = NotificationTransportRequest.from_dict(body)
    return web.Response(status=200)


async def events_transports_used_by_list(request: web.Request, uuid) -> web.Response:
    """events_transports_used_by_list

    Get a list of all objects that use this object

    :param uuid: A UUID string identifying this Notification Transport.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)
