# oLB

Simple local HTTP load-balancer based on HAProxy. An OpenAF oJob rewrites the HAProxy backends list whenever a backend container is started or stopped, from the list of local available containers, given the optional filter options.

## Environment variables

| Variable | Default   | Description |
|----------|-----------|-------------|
| FILTER_PATH | undefined | Select the variable for which to filter the backends from the list of available containers (for example: Names). Check the opack docker getContainers methods to get a list of the available variables list. |
| FILTER_VALUE | undefined | Regular expression for a filter over the field specified in FILTER_PATH. | 
| BACKEND_PORT | 80 | Port to contact the backend containers. |
| PORT | 80 | Port of entry for the load balancer over backends. |
| HOST | * | Listener for the load balancer. |
| BALANCE | roundrobin | Algorithm to use within haproxy balance option for backends. |

## Example

````yaml
lb-elastic:
  restart       : always
  build         : https://github.com/OpenAF/openaf-dockers.git#:openaf.io/oLB
  ports         :
    - 80
  networks      :
    - somenet
  volumes :
    - /var/run/docker.sock:/var/run/docker.sock:ro
  environment   :
    BACKEND_PORT: 9200
    FILTER_PATH : Names
    FILTER_VALUE: /elastic
    BALANCE     : roundrobin
````