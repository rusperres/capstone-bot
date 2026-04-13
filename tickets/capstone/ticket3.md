# Ticket Title  
**[HIGH] Support Gzip Response Handling in Proxy**

## Description  
Compressed HTTP responses (`Content-Encoding: gzip`) are displayed as garbled data in the interceptor. This prevents proper modification and forwarding. The proxy should transparently handle decompression and recompression.

## Potentially Related Files  
- `proxy/HttpResponse.java` — Handles parsing of HTTP responses  
- `proxy/InterceptorPanel.java` — UI for intercepted responses  
- `proxy/ProxyWorker.java` — Reads server socket data  
- `util/CompressionUtils.java` — Contains gzip helper methods  

## Steps  
1. Identify gzip-encoded responses  
2. Decompress content for UI display  
3. Recompress content before sending to the client  

## Acceptance Criteria  
- Interceptor shows gzip responses as readable content  
- Editing and forwarding works without corruption  
- Responses forwarded retain correct gzip encoding
