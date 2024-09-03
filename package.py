name = "dim-ftrack"
dim_version = "build.1"
version = "1.1.10"
service_version = "1.1.10"
package_version = version + "+" + dim_version
docker_version = version + "." + dim_version
previous_version = "1.1.14"
title = "dim-ftrack"
client_dir = "ayon_ftrack"

services = {
    "leecher": {"image": f"ghcr.io/dimension-studio/ayon-dim-ftrack-leecher:{service_version}"},
    "processor": {"image": f"ghcr.io/dimension-studio/ayon-dim-ftrack-processor:{service_version}"}
}

plugin_for = ["ayon_server"]

ayon_required_addons = {
    "core": ">=0.3.0",
}
ayon_compatible_addons = {
    "applications": ">=0.2.4",
}
