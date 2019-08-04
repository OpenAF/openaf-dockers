# openaf.io

## copy4GIT

Clones the latest version of a specific branch of a GIT repository and strips all the GIT metadata.

## fbrowser

Provides a simple file browser to quickly browse over a volume contents.

## OAFBuild

Clones a specific OpenAF's GIT branch and builds it. Optionally providing the final version, distribution and executing automated tests.

## OAFDirector

Simple REST API server to coordinate the OpenAF's builds, oPack building and others.

## oLB

Simples local HTTP load-balanced based on HAProxy. An OpenAF oJob rewrites the HAProxy backends list whenever a backend container is started or stopped, from the list of local available containers, given the optional filter options. Useful for testing of a cluster of containers if not deployed as a service.

## opackServer

Complete and simple private oPack server that will serve oPacks from a provided folder. These oPacks can be in the form of oPack files or folders.