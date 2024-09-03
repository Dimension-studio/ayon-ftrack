name = "dim-ftrack"
version = "1.1.14"
previous_version = "1.1.13"
title = "Dim-Ftrack"
client_dir = "ayon_ftrack"

services = {
    "leecher": {"image": f"ghcr.io/dimension-studio/ayon-dim-ftrack-leecher:{version}"},
    "processor": {"image": f"ghcr.io/dimension-studio/ayon-dim-ftrack-processor:{version}"}
}

plugin_for = ["ayon_server"]

ayon_required_addons = {
    "core": ">=0.3.0",
}
ayon_compatible_addons = {
    "applications": ">=0.2.4",
}
