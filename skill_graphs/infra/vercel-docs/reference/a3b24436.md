# ROUTER_EXTERNAL_TARGET_HANDSHAKE_ERROR
Last updated February 9, 2026
The `ROUTER_EXTERNAL_TARGET_HANDSHAKE_ERROR` error occurs when a connection cannot be successfully established with an external target. This error may result from issues during the SSL handshake process or due to a timeout, and is often attributed to one of the following causes:
  * SSL handshake failure: The SSL handshake may fail if the target has an invalid certificate or uses an unsupported Cipher Suite
  * Timeout: The error could also be due to a timeout, which might be caused by issues connecting to the target. Note that proxied requests to external targets have a maximum timeout of 120 seconds (2 minutes).


502
ROUTER_EXTERNAL_TARGET_HANDSHAKE_ERROR:
Unable to establish connection with external target
