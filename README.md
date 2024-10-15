# Outline-Authentik Group Sync

A webhook processing service for synchronizing users and groups between [Outline](https://github.com/outline/outline) and [Authentik](https://goauthentik.io/). This service updates user roles and synchronizes group memberships based on settings and incoming webhook events.

## Overview

`outline-authentik-groupsync` is designed to keep the user roles and group memberships in sync between Outline and Authentik. This service listens for webhook events and performs the necessary updates based on the configured settings.

## Getting Started

### Prerequisites

- Docker
- Outline API Key
- Authentik API Key

### Installation

Pull the Docker image from GitHub Container Registry:

```shell
docker pull ghcr.io/mnixry/outline-authentik-groupsync:latest
```

## Configuration

Configuration is done via environment variables or by using a `.env` file. Below are the settings you can configure:

| Environment Variable              | Description                                                                                             | Default Value                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `OASYNC_OUTLINE_HOST`             | Base URL for the Outline instance.                                                                      |                                 |
| `OASYNC_OUTLINE_API_KEY`          | API key for authenticating with Outline.                                                                |                                 |
| `OASYNC_OUTLINE_WEBHOOK_SECRET`   | Webhook secret for verifying incoming Outline events.                                                   |                                 |
| `OASYNC_OUTLINE_DEFAULT_ROLE`     | Default role to assign if there's no admin mapping. Options: MEMBER, ADMIN. Default: MEMBER.            | `MEMBER`                        |
| `OASYNC_OUTLINE_PAGINATION_LIMIT` | Number of items per page for pagination when fetching groups.                                           | `100`                           |
| `OASYNC_AK_HOST`                  | Base URL for the Authentik instance.                                                                    |                                 |
| `OASYNC_AK_API_KEY`               | API key for authenticating with Authentik.                                                              |                                 |
| `OASYNC_AK_GROUP_ATTRIBUTE`       | Authentik group attribute used for mapping with Outline groups. Default: "app.getoutline.com/group_id". | `"app.getoutline.com/group_id"` |
| `OASYNC_AK_ADMIN_GROUP`           | Name of the admin group in Authentik. If set, maps users in this group to an Admin role in Outline.     |                                 |
| `OASYNC_SKIP_SIGNATURE_CHECK`     | Skip webhook signature verification (not recommended for production).                                   | `False`                         |
| `OASYNC_TIMESDELTA_SECONDS`       | The webhook processing interval time.                                                                   | `60`                            |

Create a `.env` file in the root of your project directory with your configurations:

```dotenv
OASYNC_OUTLINE_HOST=https://outline.example.com
OASYNC_OUTLINE_API_KEY=your-outline-api-key
OASYNC_OUTLINE_WEBHOOK_SECRET=your-webhook-secret
OASYNC_OUTLINE_DEFAULT_ROLE=MEMBER
OASYNC_OUTLINE_PAGINATION_LIMIT=100

OASYNC_AK_HOST=https://authentik.example.com
OASYNC_AK_API_KEY=your-authentik-api-key
OASYNC_AK_GROUP_ATTRIBUTE=app.getoutline.com/group_id
OASYNC_AK_ADMIN_GROUP=Administrators
```

## Usage

Run the Docker container with the following command:

```shell
docker run -d \
    --env-file .env \
    -p 8080:8080 \
    ghcr.io/mnixry/outline-authentik-groupsync
```

The service will start listening for incoming Outline webhook `users.signin` event and process them to synchronize groups with Authentik when a user signs in.

## License

This project is licensed under the [AGPLv3 License](./LICENSE).

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
