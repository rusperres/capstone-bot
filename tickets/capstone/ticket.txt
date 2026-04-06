# Ticket Title  
**[HIGH] Fix gzip response decoding in Proxy Interceptor**

## Problem  
Intercepted HTTP responses that use `Content-Encoding: gzip` are displayed as unreadable binary data. This prevents users from viewing, editing, and forwarding responses correctly. The proxy should automatically decompress gzip responses before displaying them and recompress them before forwarding.

## Potentially Related Files  
- `proxy/HttpResponse.java` — Handles response parsing and body storage  
- `proxy/InterceptorPanel.java` — UI that displays intercepted responses  
- `proxy/ProxyWorker.java` — Reads raw socket data from server  
- `util/CompressionUtils.java` — Intended location for gzip helpers  

## What to Fix  
1. Detect `Content-Encoding: gzip` in response headers  
2. Decompress response body before displaying in the interceptor  
3. Recompress response body before forwarding to the client  

## Acceptance Criteria  
- Intercepted gzip responses are displayed in readable form  
- Users can edit and forward decompressed responses without errors  
- Forwarded responses are correctly recompressed and sent to the client
