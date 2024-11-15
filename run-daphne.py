#!/usr/bin/env python
"""
- List all daphne arguments via "help" command::

    myMachine@johnDoe:~$ daphne -h

- List of all arguments (as of August 2024)::

  --no-server-name
  --proxy-headers                                         Enable parsing and using of X-Forwarded-For and X-Forwarded-Port headers and using that as the client address
  -p PORT, --port PORT                                    Port number to listen on
  -b HOST, --bind HOST                                    The host/address to bind to
  --websocket_timeout WEBSOCKET_TIMEOUT                   Maximum time to allow a websocket to be connected. -1 for infinite.
  --websocket_connect_timeout WEBSOCKET_CONNECT_TIMEOUT   Maximum time to allow a connection to handshake. -1 for infinite
  -u UNIX_SOCKET, --unix-socket UNIX_SOCKET               Bind to a UNIX socket rather than a TCP host/port
  --fd FILE_DESCRIPTOR                                    Bind to a file descriptor rather than a TCP host/port or named unix socket
  -e SOCKET_STRINGS, --endpoint SOCKET_STRINGS            Use raw server strings passed directly to twisted
  -v VERBOSITY, --verbosity VERBOSITY                     How verbose to make the output
  -t HTTP_TIMEOUT, --http-timeout HTTP_TIMEOUT            How long to wait for worker before timing out HTTP connections
  --access-log ACCESS_LOG                                 Where to write the access log (- for stdout, the default for verbosity=1)
  --log-fmt LOG_FMT                                       Log format to use
  --ping-interval PING_INTERVAL                           The number of seconds a WebSocket must be idle before a keepalive ping is sent
  --ping-timeout PING_TIMEOUT                             The number of seconds before a WebSocket is closed if no response to a keepalive ping
  --application-close-timeout APPLICATION_CLOSE_TIMEOUT   The number of seconds an ASGI application has to exit after client disconnect before it is killed
  --root-path ROOT_PATH                                   The setting for the ASGI root_path variable
  --proxy-headers-host PROXY_HEADERS_HOST                 Specify which header will be used for getting the host part. Can be omitted, requires --proxy-headers to be specified when passed. "X-Real-IP" (when passed by your webserver) is a good candidate for this.
  --proxy-headers-port PROXY_HEADERS_PORT                 Specify which header will be used for getting the port part. Can be omitted, requires --proxy-headers to be specified when passed.
  -s SERVER_NAME, --server-name SERVER_NAME               Specify which value should be passed to response header Server attribute
"""
from pathlib import Path

from daphne.cli import CommandLineInterface

PROJECT_DIR = Path(__file__).parent


def _run_on_unix_socket() -> None:
    # ATTENTION: If you change the UNIX socket path, also change it in the docker compose file ("compose.yml")
    CommandLineInterface().run(['-u', '/run/daphne/daphne.sock', '--access-log', '/var/log/daphne/access.log', 'daphne_twisted_error.asgi:application'])


def _run_over_http() -> None:
    CommandLineInterface().run(['-b', '0.0.0.0', '-p', '8000', '--access-log', '/var/log/daphne/access.log', 'daphne_twisted_error.asgi:application'])


if __name__ == '__main__':
    # If you change from HTTP to UNIX (or vice versa) also change the upstreams in both virtual hosts in the "resources/nginx.conf" file

    _run_on_unix_socket()

    # _run_over_http()
